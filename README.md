# Neural-Networks-and-Deep-Learning-CSC-578

This repository contains files for the final project of this class. This project involves using recurrent neural networks and long short-term memory neural networks to train on large corpora of text to identify authors of texts. It also has the ability to generate new content in the writing style of the authors.

Something I want to investigate is whether different flavors of LSTM networks can generate text that is more plausibly in the style of the original author compared to other architectures. For instance, does using a gated recurrent unit improve performance?

Time permitting, I will try to create a generative adversarial network to enhance the performance of the networks so that they will get better at both discriminating between different authors and generating new content in the style of the authors.

The training for these models took place in TensorFlow, with calls to the keras API.
