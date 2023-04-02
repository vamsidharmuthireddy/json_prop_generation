# Pure Code

## Problem Statement

Using a dataset of HTML components as images and their corresponding json codes, devise a machine learning approach to generate json code for an input image.

## Sources

Dataset: Provided in the assignment.
All the data is present in 5 folders categorised according to the component type.

## Approach

### Classification

- Classify the input image for the component type
- Used a ResNet50 network for the same

#### Reproducibility

- Notebook available at notebooks/classification/

### Text Generation

- Generate the text given an input image
- Used Vision transformer(vit) to encode images
- Used gpt-2 to generate text from the encoded images
- Used Huggingface seq2seqtrainer

#### Reproducibility

- Notebook available at notebooks/generation/

## Directory Tree

├─── README.md <- The top-level README for developers using this project.
├───data
│ └─── outputs <- EDA outputs
│ └─── paths <- train, test dataframes containing image path, json path, flattened json properties as string
├───reports <- Generated analysis as HTML, PDF, LaTeX, etc.
│ └── figures <- Generated graphics and figures to be used in reporting
├───models
│ └── generation <- Models trained for text generation. Used to generate text from image
│ └── classification <- Models trained for classification. Used to classify an image into a component class
├───notebooks
│ └── classification <- Notebook used to train the classification model. Contains conda requirements file
│ └── generation <- Notebook used to train the text generation model. Contains prediction notebook. Contains conda requirements file
│ └── eda <- EDA on the json file properties
│ └── reports <- Contains EDA, and classification report

## Technologies Used

All coding has been done in python. Major libraries/frameworks used are listed below, for the exhaustive list, refer to yml files in notebooks folder and sub-folder

- pandas
- numpy
- Scikit Learn
- Keras
- Tensorflow
- Pytorch
- transformers
- weights and bias
