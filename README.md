# 🧠 Personality Type Predictor

A Streamlit web application that predicts whether you are an **Introvert** or **Extrovert** using a pre-trained machine learning model.

## 🚀 Features

- **Interactive Web Interface**: User-friendly form with dropdown selections
- **Machine Learning Model**: Uses a pre-trained logistic regression model
- **Real-time Predictions**: Instant personality type predictions
- **Beautiful UI**: Modern, responsive design with custom styling
- **Error Handling**: Robust error handling for model loading and predictions

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone or download this repository** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd path/to/your/project
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

1. **Ensure the model file is in the correct location**:
   - The model file should be at `model/best_logistic_regression_model.joblib`.

2. **Start the Streamlit application**:
   ```bash
   streamlit run app.py
   ```

3. **Open your web browser** and go to the URL displayed in the terminal (usually `http://localhost:8501`)

4. **Answer the questions**:
   - Do you feel drained after socializing? (Yes/No)
   - Do you experience stage fear? (Yes/No)

5. **Click "Predict My Personality Type"** to get your prediction

## 📊 Model Details

- **Model Type**: Binary Classification (Logistic Regression)
- **Input Features**: 
  - `Drained_after_socializing_No` (float)
  - `Drained_after_socializing_Yes` (float)
  - `Stage_fear_No` (float)
  - `Stage_fear_Yes` (float)
- **Output**: Personality type prediction (Introvert/Extrovert)

## 🏗️ Project Structure

```
├── app.py                              # Main Streamlit application
├── model/
│   └── best_logistic_regression_model.joblib  # Pre-trained model file
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── notebook/                           # (Optional) Jupyter notebooks
├── venv/                               # Python virtual environment
└── .gitignore
```

## 🔧 Customization

### Using a Different Model

If you want to use a different model file (e.g., `best_random_forest_model.joblib`), simply:

1. Replace the model file in the `model/` directory
2. Update the model filename in `app.py`:
   ```python
   model = joblib.load('model/your_model_filename.joblib')
   ```

### Modifying Input Features

If your model expects different features, update the `preprocess_input()` function in `app.py` to match your model's expected input format.

## 🐛 Troubleshooting

### Common Issues

1. **Model loading error**: Ensure the joblib file is in the `model/` directory (i.e., `model/best_logistic_regression_model.joblib`)
2. **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Port already in use**: If port 8501 is busy, Streamlit will automatically use the next available port

### Getting Help

If you encounter any issues:
1. Check that all dependencies are installed correctly
2. Verify the model file exists at `model/best_logistic_regression_model.joblib` and is not corrupted
3. Check the terminal output for error messages

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this application.

---

**Note**: This prediction is based on a machine learning model trained on specific behavioral patterns. Personality is complex and exists on a spectrum - this is just one perspective! 