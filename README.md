# Phishing URL Detector

This is a simple and modern web-based application to detect phishing URLs. It uses:
- **Machine Learning**: A Random Forest model trained on URL features.
- **AI (Language Model)**: A local AI server to analyze and classify URLs.

You can toggle between Machine Learning, AI, or both for predictions.

## Features
- Analyze URLs for potential phishing risks.
- View AI explanations in a clean and styled format.
- Easy-to-use web interface with modern design.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/phishing-url-detector.git
   cd phishing-url-detector
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the machine learning model (if not already trained):
   ```bash
   python model_training.py
   ```

4. Start the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter the URL you want to classify.
2. Select the mode:
   - **Machine Learning**: Uses the trained Random Forest model.
   - **AI**: Queries the local AI server for predictions and explanations.
   - **Both**: Displays results from both Machine Learning and AI.
3. View the results and explanations.

## Notes for Using the AI Feature
- Ensure you are running a **local AI server**. This can be easily set up using **LM Studio**.
- Update the model name and the URL in the `ai_predict` function inside `app.py` to match your setup:
  - Replace the `"model": "llama-3.2-3b-instruct"` with your actual model name.
  - Update the URL (e.g., `http://127.0.0.1:1234/v1/chat/completions`) to the correct endpoint for your AI server.

## Project Structure
- `model_training.py`: Script to train the Random Forest model.
- `app.py`: Flask app for serving predictions.
- `utils.py`: Shared logic for feature extraction.
- `templates/`: HTML templates for the app interface.
- `static/`: CSS.

## Notes
- Ensure your local AI server is running and accessible at `http://127.0.0.1:1234`.
- Adjust dataset paths and model configurations as needed.

## License
Feel free to use and modify this project as you like!
