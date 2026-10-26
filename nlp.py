
from transformers import pipeline

# Create fill-mask pipeline
fill_mask = pipeline(
    "fill-mask",
    model="bert-base-uncased"
)

text = "I drink a cup of [MASK]."

results = fill_mask(text)

for result in results:
    print("Word:", result["token_str"])
    print("Probability:", result["score"])
    print()
