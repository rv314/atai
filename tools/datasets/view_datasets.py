"""
Sample code to view dataset format and samples used to train an LLM model.
Replace the dataset name with the one you want to view.
"""
from datasets import load_dataset

# Load the dataset with a specific split
# Replace the dataset name with the one you want to view, eg. instead of "oieieio/OpenR1-Math-220k" any other dataset name can be used.
dataset = load_dataset("oieieio/OpenR1-Math-220k",
                       name="all", split="default", streaming=True)

# Print a few samples
num_samples = 1
for i, sample in enumerate(dataset):
    print(f"\nExample {i+1}:")
    for key, value in sample.items():
        print(f"{key}: {value}")

    if i + 1 >= num_samples:
        break  # Stop after a few examples
