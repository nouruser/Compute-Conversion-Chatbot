import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        # Forward pass through RNN
        out, _ = self.rnn(x)

        # Reshape the tensor to be 2-dimensional
        out = out.contiguous().view(out.size(0), -1)

        # Pass it through the fully connected layer
        out = self.fc(out)

        # Apply activation
        out = self.relu(out)

        return out
