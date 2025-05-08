# Human cytotoxicity endpoints

The authors tested the dataset of 39312 compounds used to train the antibiotics-ai model (eos18ie) against several cytotoxicity endpoints; human liver carcinoma cells (HepG2), human primary skeletal muscle cells (HSkMCs) and human lung fibroblast cells (IMR-90). Cellular viability was measured after 20133 days of treatment with each compound at 10 μM and activities were binarized using a 90% cell viability cut-off. 341 (8.5%), 490 (3.8%) and 447 (8.8%) compounds classified as cytotoxic for HepG2 cells, HSk-MCs and IMR-90 cells

This model was incorporated on 2024-02-05.

## Information
### Identifiers
- **Ersilia Identifier:** `eos42ez`
- **Slug:** `antibiotics-ai-cytotox`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Cytotoxicity`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `3`
- **Output Consistency:** `Fixed`
- **Interpretation:** Predicting cytotoxicity in  human liver carcinoma cells (HepG2), human primary skeletal muscle cells (HSkMCs) and human lung fibroblast cells (IMR-90)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| cytotoxicity_hepg2 | float | low | Predicted cytotoxicity of the compound against human liver carcinoma cells (HepG2). The value is between 0 and 1 where 0 means non-toxic and 1 means toxic |
| cytotoxicity_hskmc | float | low | Predicted cytotoxicity of the compound against human primary skeletal muscle cells (HSkMC). The value is between 0 and 1 where 0 means non-toxic and 1 means toxic |
| cytotoxicity_imr90 | float | low | Predicted cytotoxicity of the compound against human lung fibroblast cells (IMR-90). The value is between 0 and 1 where 0 means non-toxic and 1 means toxic |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos42ez](https://hub.docker.com/r/ersiliaos/eos42ez)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos42ez.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos42ez.zip)

### Resource Consumption
- **Model Size (Mb):** `1401`
- **Environment Size (Mb):** `5637`
- **Image Size (Mb):** `7157.17`

**Computational Performance (seconds):**
- 10 inputs: `104.66`
- 100 inputs: `237.17`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/felixjwong/antibioticsai](https://github.com/felixjwong/antibioticsai)
- **Publication**: [https://www.nature.com/articles/s41586-023-06887-8](https://www.nature.com/articles/s41586-023-06887-8)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2023`
- **Ersilia Contributor:** [Richiio](https://github.com/Richiio)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos42ez
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos42ez
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
