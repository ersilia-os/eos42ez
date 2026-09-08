import os
import csv
import sys

import chemprop
from chemprop.train.make_predictions import load_model

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# one checkpoint directory per cytotoxicity endpoint, in output column order
MODELS = [
    os.path.join(checkpoints, "cytotox_hepg2"),
    os.path.join(checkpoints, "cytotox_primary"),
    os.path.join(checkpoints, "cytotox_imr90"),
]


def predict(checkpoint_dir, smiles_list):
    """Predict for every molecule with one ensemble, loading it only once.

    The ensemble is loaded up front with load_model() and handed to
    make_predictions() as model_objects, so the 11 checkpoints are read once for
    the whole batch instead of once per molecule.
    """
    arguments = [
        "--test_path", "/dev/null",
        "--preds_path", "/dev/null",
        "--checkpoint_dir", checkpoint_dir,
        "--features_generator", "rdkit_2d_normalized",
        "--no_features_scaling",
        "--num_workers", "0",
    ]
    args = chemprop.args.PredictArgs().parse_args(arguments)
    model_objects = load_model(args, generator=False)
    preds = chemprop.train.make_predictions(
        args=args,
        smiles=[[smiles] for smiles in smiles_list],
        model_objects=model_objects,
    )
    return preds


def as_float_string(prediction):
    """Return the prediction as a string, or "" if it is not a number.

    Invalid SMILES come back from chemprop as the string "Invalid SMILES".
    """
    try:
        return str(float(prediction[0]))
    except (TypeError, ValueError, IndexError):
        return ""


# Read SMILES from .csv file
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# Run each ensemble over the whole batch, freeing it before loading the next one
columns = []
for checkpoint_dir in MODELS:
    try:
        preds = predict(checkpoint_dir, smiles_list)
        column = [as_float_string(p) for p in preds]
        column += [""] * (len(smiles_list) - len(column))  # never write a short column
        columns.append(column)
    except Exception:
        columns.append([""] * len(smiles_list))

with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["cytotoxicity_hepg2", "cytotoxicity_hskmc", "cytotoxicity_imr90"])  # header with column names
    for i in range(len(smiles_list)):
        writer.writerow([column[i] for column in columns])
