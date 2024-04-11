# Human cytotoxicity endpoints

The authors tested the dataset of 39312 compounds from the antibiotics-ai model (eos18ie) against several cytotoxicity endpoints; human liver carcinoma cells (HepG2), human primary skeletal muscle cells (HSkMCs) and human lung fibroblast cells (IMR-90). Cellular viability was measured after 20133 days of treatment with each compound at 10 μM and activities were binarized using a 90% cell viability cut-off. 341 (8.5%), 490 (3.8%) and 447 (8.8%) compounds classified as cytotoxic for HepG2 cells, HSk-MCs and IMR-90 cells

## Identifiers

* EOS model ID: `eos42ez`
* Slug: `antibiotics-ai-cytotox`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Predicting cytotoxicity in  human liver carcinoma cells (HepG2), human primary skeletal muscle cells (HSkMCs) and human lung fibroblast cells (IMR-90)

## References

* [Publication](https://www.nature.com/articles/s41586-023-06887-8)
* [Source Code](https://github.com/felixjwong/antibioticsai)
* Ersilia contributor: [Richiio](https://github.com/Richiio)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos42ez)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos42ez.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos42ez) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s41586-023-06887-8) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!