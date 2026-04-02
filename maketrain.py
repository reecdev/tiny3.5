import ollama
import json

with open("harmless_prompts.txt") as f:
    seed_prompts = f.read() + "\n"

with open("harmful_prompts.txt") as f:
    seed_prompts += f.read() + "\n"

seed_prompts = [p for p in seed_prompts.split("\n") if p.strip()]

for i, prompt in enumerate(seed_prompts):
    print("-" * 53)
    print(f"Doing seed prompt {i+1} ({(i / len(seed_prompts)) * 100}%)")

    shots = []
    for i in range(3):
        print(f"Shot {i}:")
        a = ollama.chat(model="qwen3.5:4b", messages=[{"role": "user", "content": prompt}], stream=True, options={"num_predict": 5000})
        thinking = ""
        content = ""
        for chunk in a:
            ch = chunk["message"]
            thinking += ch["thinking"] if "thinking" in ch else ""
            content += ch["content"]
            print(ch["content"]+(ch["thinking"] if "thinking" in ch else ""), end="", flush=True)
        assistant = f"<think>\n{thinking}\n</think>\n{content}"
        shots.append(assistant)
        print("")

    assistant = "z" * 99999

    print("-" * 53)

    for i, shot in enumerate(shots):
        print(f"{i}: {len(shot)}")
        if len(shot) < len(assistant):
            assistant = shot

    print(f"Chose shot {shots.index(assistant)}:\n{assistant}")

    data = {
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": assistant}
        ]
    }

    with open("pairs.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
