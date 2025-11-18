"""
DIAGNOSTIC TASK - Complete as many levels as you can

LEVEL 1: Get this working (required)
LEVEL 2: Expand it (tests Python skills)
LEVEL 3: Pick a challenge (tests thinking)
LEVEL 4: Build something new (tests creativity)

DUE: Wednesday 11:59 PM
Submit via: GitHub PR (preferred) or Teams #architecture channel.
See submission_format.txt for details.
"""
""" LEVEL 1: Basic generation"""

from transformers import pipeline
import time
"""
# LEVEL 1: Basic generation
print("=== LEVEL 1: BASIC GENERATION ===")
generator = pipeline('text-generation', model='distilgpt2')

prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is"
]

for prompt in prompts:
    output = generator(prompt, max_length=30)
    print(f"\nPrompt: {prompt}")
    print(f"Generated: {output[0]['generated_text']}")
    print("-" * 50)
"""

# LEVEL 2: Your code here
generator = pipeline('text-generation', model='distilgpt2')

prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is"
    "Once upon a time",
    "The meaning of life is"

]
with open("generation_results.txt", "w",encoding='utf-8') as f: # automatically closes the file after writing
    for prompt in prompts:
        start_time = time.time() # Start the timer to measure the generation time
        output = generator(prompt, min_new_tokens=100,max_new_tokens=100, num_return_sequences=1, do_sample=True, temperature=0.85, top_p=0.8, top_k=40) # Generate text with specified parameters
        end_time = time.time() # stop the timer once generation is complete
        generation_time = end_time - start_time #calculate generation time
        print(output)
        token_count = len(generator.tokenizer.encode(output[0]['generated_text'])) # Count the number of tokens in the generated text
        # Save results to file
        f.write(f"\nPrompt: {prompt}\n")
        f.write(f"Generated: {output[0]['generated_text']}\n")
        f.write(f"Generation Time: {generation_time:.4f} seconds\n")
        f.write(f"Token Count: {token_count}\n")
        f.write("-" * 50 + "\n")

# TODO: Save to file
# TODO: Try different parameters
# TODO: Time generation
# TODO: Count tokens

# LEVEL 3: Your code here
# TODO: Pick Option A, B, C, or D. maybe all of them?
# TODO: Implement your challenge

# LEVEL 4: Your code here
# TODO: Build something new