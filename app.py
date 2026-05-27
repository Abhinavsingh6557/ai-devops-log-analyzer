from flask import Flask, render_template
import random
import requests

app = Flask(__name__)

API_KEY = "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"

logs = [
    "ERROR: Server CPU usage reached 95%",
    "WARNING: Memory usage exceeded threshold",
    "CRITICAL: Kubernetes pod crashed",
    "INFO: Deployment completed successfully",
    "ERROR: Database connection timeout",
    "WARNING: Disk space running low",
    "CRITICAL: Jenkins pipeline failed",
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-log")
def generate_log():

    log = random.choice(logs)

    prompt = f"""
    Analyze this DevOps log.

    Provide:
    1. Issue explanation
    2. Possible cause
    3. Suggested fix

    Log:
    {log}
    """

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()
        print(result)

        if "choices" in result:
            ai_analysis = result["choices"][0]["message"]["content"]
        else:
            ai_analysis = f"API Error: {result}"

    except Exception as e:
        ai_analysis = f"AI Error: {str(e)}"

    return render_template("index.html", log=log, analysis=ai_analysis)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)