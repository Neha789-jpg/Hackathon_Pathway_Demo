print("HELLO FROM PYTHON")
print("SCRIPT STARTED")

# -----------------------------
# Imports
# -----------------------------
import os
import random

# -----------------------------
# Read files
# -----------------------------
with open("novel_1.txt", "r", encoding="utf-8") as f:
    novel = f.read()

with open("backstory_1.txt", "r", encoding="utf-8") as f:
    backstory = f.read()

print("FILES LOADED ✅")

# -----------------------------
# REDUCE INPUT FOR DEMO
# -----------------------------
demo_novel = novel[:1000]  # first 1000 chars for safe demo
chunk_size = 250           # characters per chunk
chunks = [demo_novel[i:i+chunk_size] for i in range(0, len(demo_novel), chunk_size)]

predictions = []

# -----------------------------
# MOCK GPT RESPONSES
# -----------------------------
for idx, chunk in enumerate(chunks):
    # Instead of calling OpenAI, we simulate predictions
    # For demo, randomly assign CONSISTENT or CONTRADICT
    answer = random.choice(["CONSISTENT", "CONTRADICT"])
    prediction = 1 if "CONSISTENT" in answer else 0
    predictions.append(prediction)

    print(f"Processed chunk {idx+1}/{len(chunks)} → Mock Prediction: {prediction}")

# -----------------------------
# Combine predictions
# -----------------------------
final_prediction = 1 if all(predictions) else 0

# -----------------------------
# Save results
# -----------------------------
with open("results.csv", "w") as f:
    f.write("story_id,prediction\n")
    f.write(f"1,{final_prediction}\n")

print("DONE ✅ Final Prediction:", final_prediction)
print("Results saved to results.csv")
