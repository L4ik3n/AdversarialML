#  Indirect Prompt Injection Lab

Lab for exploring **indirect prompt injection** attacks.

---


Clone the repository and install dependencies:

```bash
pip3 install -r requirements.txt
```

Start the ollama docker container:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Choose model to run: 
```bash
docker exec ollama ollama run gemma3:4b
```

Start the web app:
```bash
python3 app.py
```
