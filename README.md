# Tiny3.5
An attempt to compress Qwen3.5 into 500M and 1.5B parameters.

## What is this?
Tiny3.5 is my community effort to create tiny and more efficient versions of Qwen3.5.
The strengths of Tiny3.5 include very low inference latency, minimal overthinking, and being able to run on much weaker hardware.
However, it's important to realize that Tiny3.5 is sub-2B parameters. Don't expect a 99% score on every single benchmark.

## How do I use this?
~~Weights will be released on Ollama soon, once I'm done collecting data and finetuning. A link will be added here.~~


500M model (HuggingFace): https://huggingface.co/reecdev/Tiny3.5-Coder-500M/


Ollama page: https://ollama.com/reecdev/tiny3.5

## My Distillation Approach
The base models I'll be using for Tiny3.5 are Qwen2.5-Coder-0.5B and Qwen2.5-Coder-1.5B. I use multi-shot distillation to fix issues like overthinking, looping, exc. because with a model this small, these issues can be silent killers.

Regular distillation is like: "Emulate the model perfectly."


Multi shot disillation is like: "Emulate the model **at it's best behavior** perfectly."
