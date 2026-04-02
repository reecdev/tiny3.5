# Tiny3.5
An attempt to compress Qwen3.5 into 500M and 1.5B parameters.

## What is this?
This is the repo I use to organize my code and keep files for distillation. If you want to do something like this yourself, pairs.jsonl (The actual user-assistant pairs) and maketrain.py (Training data collection script) are included.

## My Distillation Approach
The base model I'll be using for Tiny3.5 is Qwen2.5-Coder-0.5B. I use multi-shot distillation to fix issues like overthinking, looping, exc. because with a model this small, these issues can be silent killers.

Regular distillation is like: "Emulate the model perfectly."


Multi shot disillation is like: "Emulate the model **at it's best behavior** perfectly."
