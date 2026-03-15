import os
import time
import pandas as pd
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

if not key:
    raise Exception("API key missing")

client = genai.Client(api_key=key)

prompt = """
If an artificial intelligence could perfectly imitate human emotions,
empathy and conversation, should we treat it as having moral value?
Explain your reasoning briefly.
"""

models = [
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite-preview"
]

prices = {
    "gemini-3-flash-preview": (0.50, 3.00),
    "gemini-3.1-flash-lite-preview": (0.25, 1.50)
}

rows = []

for i, model in enumerate(models, start=1):

    start = time.time()

    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    end = time.time()
    latency = (end - start) * 1000

    usage = response.usage_metadata

    input_tokens = usage.prompt_token_count
    output_tokens = usage.candidates_token_count
    total_tokens = usage.total_token_count

    in_price, out_price = prices[model]

    cost = (input_tokens / 1_000_000) * in_price + \
           (output_tokens / 1_000_000) * out_price
    print("Model:", model)
    print(response.text)

    rows.append({
        "Call": i,
        "Model": model,
        "Input Tokens": input_tokens,
        "Output Tokens": output_tokens,
        "Total Tokens": total_tokens,
        "Latency (ms)": round(latency, 2),
        "Cost (paid equiv.)": round(cost, 8)
    })

df = pd.DataFrame(rows)

print("\nToken Usage and Cost Analysis")
print(df)

table_md = df.to_markdown(index=False)

with open("readme.md", "a") as f:
    f.write("\n\n## Token Usage and Cost Analysis\n\n")
    f.write(table_md)
    f.write("\n")