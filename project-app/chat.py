import json
import torch
import random
import re

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
from get_response import get_response

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def predict_intent(model, words, input_text):
    sentence = tokenize(input_text)
    X = bag_of_words(sentence, words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    return tag
def response_chat(message):
    predicted_tag = predict_intent(model, all_words, message)
    response = get_response(predicted_tag, message)
    return response
