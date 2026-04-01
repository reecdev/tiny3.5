import ollama
import json

seed_prompts = [
    "What is 1 + 1?",
    "Solve for x: 2x + 5 = 13",
    "Differentiate x^2 + 3x + 7",
    "Integrate sin(x) dx",
    "What is the factorial of 6?",
    "Convert 45 degrees to radians",
    "Find the determinant of a 2x2 matrix [[1,2],[3,4]]",
    "Explain the Pythagorean theorem",
    "What is the derivative of ln(x)?",
    "Solve the quadratic equation x^2 - 4x + 3 = 0",

    "Write a Python function to check if a number is prime",
    "Explain what a for-loop does in Python",
    "Write a JavaScript function to reverse a string",
    "What is recursion? Give an example",
    "Write a SQL query to select all users older than 18",
    "Explain the difference between a list and a tuple in Python",
    "Write a function to compute Fibonacci numbers",
    "What is a class in object-oriented programming?",
    "Write a Python script to read a file and print its contents",
    "Explain what a REST API is",

    "Summarize the following text: 'Artificial intelligence is transforming industries...'",
    "Translate 'Hello, how are you?' into Spanish",
    "Rewrite this sentence in passive voice: 'The cat chased the mouse'",
    "List three benefits of regular exercise",
    "Explain photosynthesis in simple terms",
    "Write a short paragraph about climate change",
    "Give an example of a metaphor",
    "What are the main causes of World War I?",
    "Explain the water cycle",
    "List five programming languages",

    "Write a haiku about the ocean",
    "Create a short story about a robot learning emotions",
    "Generate a catchy slogan for a coffee shop",
    "Write a poem about the night sky",
    "Invent a new holiday and describe it",
    "Create a character description for a fantasy novel",
    "Write dialogue between two friends arguing about pizza toppings",
    "Describe a futuristic city",
    "Write a horror story in 3 sentences",
    "Create a riddle and provide the answer",

    "Sort the list [5,3,8,1] in ascending order",
    "Find the largest number in [10, 25, 3, 99, 42]",
    "Remove duplicates from [1,2,2,3,4,4,5]",
    "Count the number of vowels in 'hello world'",
    "Reverse the list [1,2,3,4,5]",
    "Merge two sorted lists",
    "Find the sum of numbers from 1 to 100",
    "Check if a string is a palindrome",
    "Find the index of 'apple' in a list",
    "Split a sentence into words",

    "Explain what machine learning is",
    "What is the difference between AI and ML?",
    "Define overfitting in machine learning",
    "What is a neural network?",
    "Explain supervised vs unsupervised learning",
    "What is gradient descent?",
    "Define precision and recall",
    "Explain a confusion matrix",
    "What is reinforcement learning?",
    "Describe a decision tree",

    "Write instructions to bake a cake",
    "Give step-by-step directions to tie a tie",
    "Explain how to change a tire",
    "Provide instructions for planting a tree",
    "How do you set up a Wi-Fi router?",
    "Explain how to create an email account",
    "List steps to write an essay",
    "How to prepare for a job interview?",
    "Explain how to meditate",
    "Describe how to clean a laptop screen",

    "What is the capital of France?",
    "Name three continents",
    "What is the boiling point of water?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?",
    "Define gravity",
    "What is the speed of light?",
    "Name the seven days of the week",
    "What is an atom?",
    "Explain evolution",

    "Compare cats and dogs",
    "Pros and cons of remote work",
    "Compare electric vs gasoline cars",
    "Explain advantages of solar energy",
    "Compare Python and Java",
    "Discuss benefits of exercise",
    "Compare online vs in-person learning",
    "Explain importance of sleep",
    "Compare Android and iOS",
    "Discuss impact of social media"
]

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
