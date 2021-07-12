import sys
import json
import torch
import numpy as np
import torchvision.models as models

from utils import (
    add_handler,
    download_image,
    init_logger,
    preprocess_image,
    model_prediction,
    number_output,
)

# Open labels
with open("model/imagenet_classes.txt") as f:
    labels = [line.strip() for line in f.readlines()]

# # Load pretrained model
PATH = "model/mobilenetv2.pth"

mobilenet_v2 = models.mobilenet_v2()
mobilenet_v2.load_state_dict(torch.load(PATH))
mobilenet_v2.eval()


def lambda_handler(event, context):
    # Retrieve inputs
    input_url, n_predictions = event["input_url"], event["n_predictions"]

    # # Download image
    input_image = download_image(input_url)

    # # Process input image
    batch = preprocess_image(input_image)

    # # Generate prediction
    pred = model_prediction(input_batch=batch, mdl=mobilenet_v2)

    # # Top n results
    n_results = number_output(mdl_output=pred, mdl_labels=labels, top_n=n_predictions)

    # prediction = model.predict(url)
    response = {"statusCode": 200, "body": json.dumps(n_results)}

    return response
