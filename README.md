# Customer Churn Prediction App

This Streamlit application predicts customer churn based on various customer characteristics and service usage patterns.

## Features

- Interactive web interface for customer churn prediction
- Real-time predictions using machine learning model
- Detailed insights and recommendations
- User-friendly input forms for customer data

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
# On Windows
run_app.bat
# On Unix/MacOS
streamlit run streamlit_app.py
```

## Deployment

This app is configured for deployment on Streamlit Community Cloud. To deploy:

1. Push your code to GitHub
2. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy the app

## Project Structure

```
customer-churn-prediction/
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
├── run_app.bat          # Windows startup script
├── models/              # Directory for model files
└── data/               # Directory for data files
```

## Dependencies

- streamlit==1.32.0
- pandas==2.2.0
- numpy==1.26.4
- scikit-learn==1.4.0
- joblib==1.3.2

## License

MIT License 