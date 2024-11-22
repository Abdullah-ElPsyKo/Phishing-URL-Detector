import re
import requests
import markdown

# Shared feature extraction function
def extract_features(url):
    features = []
    features.append(len(url))  # URL length
    features.append(1 if "@" in url else 0)  # '@' symbol presence
    features.append(1 if "-" in url else 0)  # '-' symbol presence
    features.append(url.count("."))  # Number of dots
    features.append(1 if url.startswith("https") else 0)  # HTTPS usage

    try:
        domain_parts = url.split('/')[2].split('.')
        features.append(len(domain_parts))  # Number of subdomains
        features.append(1 if any(len(part) > 10 for part in domain_parts) else 0)
    except IndexError:
        features.append(0)
        features.append(0)

    phishing_keywords = ["login", "verify", "secure", "account", "update", "bank", "password"]
    features.append(1 if any(keyword in url.lower() for keyword in phishing_keywords) else 0)

    suspicious_tlds = [".tk", ".ml", ".ga", ".cf", ".gq"]
    features.append(1 if any(url.endswith(tld) for tld in suspicious_tlds) else 0)

    try:
        ip_address = re.match(r"^\d+\.\d+\.\d+\.\d+$", url.split('/')[2])
        features.append(1 if ip_address else 0)
    except IndexError:
        features.append(0)

    return features

def ai_predict(url):
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama-3.2-3b-instruct", # Change the model name if needed
        "messages": [{"role": "user", "content": f"Classify this URL: {url}. Keep it short and simple. Start with 'Phishing', 'Legitimate', or 'Uncertain' and provide the top 3 reasons why."}],
        "temperature": 0.7,
    }

    # Send request to AI server
    try:
        response = requests.post("http://127.0.0.1:1234/v1/chat/completions", headers=headers, json=payload) # Change the URL if needed
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        # Extract AI-generated content and convert Markdown to HTML
        ai_response = data["choices"][0]["message"]["content"].strip()
        return markdown.markdown(ai_response)

    except requests.exceptions.RequestException as e:
        print(f"Error while communicating with AI server: {e}")
        return "<p>Error: AI could not process the request.</p>"