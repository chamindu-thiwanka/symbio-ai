import subprocess

#using ollama qwen3:1.7b model
MODEL_NAME = 'qwen3:1.7b'

def query_llm(prompt:str) -> str:
    result = subprocess.run(
        ['ollama', 'run', MODEL_NAME],
        input = prompt,
        text = True,
        encoding='utf-8',
        errors='replace',
        capture_output = True
    )
    
    return result.stdout.strip()