## what does this program do?

The program loads the API key from a .env file, sends
the same philosophical question about consciousness to both gemini-3-flash-preview and
gemini-3.1-flash-lite-preview, and prints the responses returned by each model.

For every API call the script measures the latency, reads the token usage
reported by the API (input, output, and total tokens), and calculates the
equivalent paid cost based on the official pricing per million tokens.

The results are collected into a pandas DataFrame and exported below as a
table.

## what surprised me:

What surprised me in this experiment the most was how similar the overall reasoning of the two models
was even though they are different variants. Both models structured their answers
into philosophical perspectives, referencing similar philosophical ideas like functionalism and 
sentience,which suggests they rely on similar training knowledge when discussing 
ethical questions. also noticed that the gemini-3-flash-preview 
model was actually slower than the lite model in this run, which I did not expect 
given that it is described as the faster model. 

## How to run it:

just provide valid API key in .env file, and run the main.py file.

## Token Usage and Cost Analysis:

|   Call | Model                         |   Input Tokens |   Output Tokens |   Total Tokens |   Latency (ms) |   Cost (paid equiv.) |
|-------:|:------------------------------|---------------:|----------------:|---------------:|---------------:|---------------------:|
|      1 | gemini-3-flash-preview        |             34 |             333 |            873 |        6573.77 |             0.001016 |
|      2 | gemini-3.1-flash-lite-preview |             34 |             557 |            591 |        3754.11 |             0.000844 |
