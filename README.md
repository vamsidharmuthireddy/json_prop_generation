# Pure Code

## Problem Statement

Using a dataset of HTML components as images and their corresponding json codes, devise a machine learning approach to generate json code for an input image.

## Sources

Dataset: Provided in the assignment.
All the data is present in 5 folders catagorised according to the component type.

## Approach

- Classify the input image for the component type
- Used a ResNet50 network for the same

## Reproducibility

## Directory Tree

├─── README.md <- The top-level README for developers using this project.
├───data
│ ├───raw <- The original, immutable data dump
│ │ ├───Button
│ │ ├───Card
│ │ ├───Card
│ │ ├───Icon
│ │ └───Switch
│ ├───external <- Data from third party sources (empty)
│ ├───interim <- Intermediate data that has been transformed
│ └───outputs
├───reports <- Generated analysis as HTML, PDF, LaTeX, etc.
│ └── figures <- Generated graphics and figures to be used in reporting
├───models
├───notebooks
├───src <- Source code for use in this project
├───requirements.txt <- The requirements file for reproducing the analysis environment, e.g.
│ generated with `pip freeze > requirements.txt`
└───references <- Data dictionaries, manuals, and all other explanatory materials

## Technologies Used

All coding has been done in python. Major libraries/frameworks used are listed below, for the exhaustive list, refer to requirements.txt

- pandas
- numpy
- Scikit Learn
- Keras
- Tensorflow
- Pytorch
- transformers
- weights and bias
