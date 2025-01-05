import os
import csv
import sys

import chemprop

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
hepg_model = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "cytotox_hepg2"))
HSK_model = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "cytotox_primary"))
IMR_model = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "cytotox_imr90"))

def my_model1(smiles_list):
    
    smiles_list_list= [[smiles] for smiles in smiles_list]  
    arguments = [
    '--test_path', '/dev/null',
    '--preds_path', '/dev/null',
    '--checkpoint_dir', hepg_model,
    '--features_generator', 'rdkit_2d_normalized',
    '--no_features_scaling'
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args, smiles=smiles_list_list)
    return preds

def my_model2(smiles_list):
    
    smiles_list_list= [[smiles] for smiles in smiles_list]  
    arguments = [
    '--test_path', '/dev/null',
    '--preds_path', '/dev/null',
    '--checkpoint_dir', HSK_model,
    '--features_generator', 'rdkit_2d_normalized',
    '--no_features_scaling'
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args, smiles=smiles_list_list)
    return preds

def my_model3(smiles_list):
    
    smiles_list_list= [[smiles] for smiles in smiles_list]  
    arguments = [
    '--test_path', '/dev/null',
    '--preds_path', '/dev/null',
    '--checkpoint_dir', IMR_model,
    '--features_generator', 'rdkit_2d_normalized',
    '--no_features_scaling'
    ]

    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args, smiles=smiles_list_list)
    return preds

# Function to extract desired values from model predictions
def extract_values(predictions):
    return [str(prediction[0]) for prediction in predictions]

# Read SMILES from .csv file
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# Run models and extract desired values
outputs1 = extract_values(my_model1(smiles_list))
outputs2 = extract_values(my_model2(smiles_list))
outputs3 = extract_values(my_model3(smiles_list))

with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["cytotoxicity_hepg2", "cytotoxicity_hskmc", "cytotoxicity_imr90"])  # header with column names
    for o1, o2, o3 in zip(outputs1, outputs2, outputs3):
        writer.writerow([o1, o2, o3])