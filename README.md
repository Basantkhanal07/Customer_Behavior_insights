# 📊 Customer Behavior Insights & Churn Prediction

A comprehensive machine learning project that analyzes customer behavior data to derive actionable business insights through data cleaning, exploratory data analysis, churn prediction, customer segmentation, and NLP-based sentiment analysis.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

## 🎯 Project Overview

This project implements an end-to-end data science pipeline to understand customer behavior patterns and predict churn. The analysis combines multiple machine learning techniques to provide business-ready insights that help organizations reduce customer attrition, optimize marketing strategies, and enhance operational efficiency.

### Key Features

- **Churn Prediction**: Random Forest classifier for identifying at-risk customers
- **Customer Segmentation**: KMeans clustering for targeted marketing strategies
- **Sentiment Analysis**: NLP-based analysis of customer feedback
- **Interactive Dashboard**: Real-time predictions via Streamlit web application
- **Business Recommendations**: Actionable insights for stakeholders

## 📁 Repository Structure

```
Customer_Behavior_Insights/
│
├── data/
│   ├── customer_behavior.csv                      # Raw dataset
│   ├── customer_behavior_clean.csv                # Cleaned dataset 
│
├── notebooks/
│   ├── 01_data_understanding_cleaning.ipynb       # Data preprocessing
│   ├── 02_exploratory_data_analysis.ipynb         # EDA and visualization
│   ├── 03_churn_modeling.ipynb                    # Churn prediction model
│   ├── 04_customer_segmentation.ipynb             # Clustering analysis
│   ├── 05_nlp_analysis.ipynb                      # Sentiment analysis
│   └── 06_final_business_rec.ipynb                # Business insights
│
├── app.py                                          # Streamlit application
├── requirements.txt                                # Project dependencies
├── .gitignore                                      # Git ignore rules
└── README.md                                       # Project documentation
```

## 🔬 Analysis Workflow

### 1. Data Understanding & Cleaning
- Loads and explores raw customer data
- Handles missing values and duplicate records
- Encodes categorical variables for machine learning
- Outputs cleaned dataset for downstream analysis

### 2. Exploratory Data Analysis (EDA)
- Generates descriptive statistics (age, income, spending score)
- Visualizes data distributions using histograms and box plots
- Analyzes relationships between variables using scatter plots
- Examines purchase history and frequency patterns

### 3. Churn Prediction Modeling
- Defines and engineers churn target variable
- Performs feature selection and normalization
- Trains Logistic Regression and Random Forest classifiers
- Evaluates model performance using accuracy, precision, recall, and confusion matrix
- Identifies high-risk customers for retention campaigns

### 4. Customer Segmentation
- Standardizes features for clustering analysis
- Applies KMeans algorithm with optimal cluster selection (Elbow method)
- Reduces dimensionality using PCA for visualization
- Assigns cluster labels and profiles customer segments

### 5. NLP Sentiment Analysis
- Preprocesses text data (lowercasing, stopword removal, tokenization)
- Analyzes word frequency and common themes
- Classifies sentiment using rule-based and ML approaches
- Visualizes sentiment distribution across customer base
- Extracts key complaints and positive feedback

### 6. Business Recommendations
- Synthesizes insights from all analyses
- Develops churn reduction strategies
- Creates segment-specific marketing recommendations
- Proposes operational and product improvements

## 💡 Key Business Insights

### Churn Reduction Strategies
- **Retention Campaigns**: Target churned customers with personalized emails and discount coupons
- **Proactive Support**: Prioritize customer service for at-risk users identified by the model
- **Loyalty Programs**: Introduce rewards and incentives for high-spending customers showing churn signals

### Segment-Based Marketing
- **High Income / Low Spend**: Offer premium bundles and concierge support services
- **Mid Income / Mid Spend**: Deploy seasonal promotions and value-added offers
- **Low Income / High Spend**: Implement membership programs and loyalty plans

### Product & Operations
- **Pricing Strategy**: Address pricing concerns identified in negative sentiment analysis
- **Service Excellence**: Continue emphasizing fast delivery and product quality (top positive drivers)
- **Feedback Loop**: Implement continuous monitoring of customer sentiment

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Basantkhanal07/Customer_Behavior_Insights.git
   cd Customer_Behavior_Insights
   ```

2. **Create Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Running Jupyter Notebooks

Launch Jupyter Notebook to explore the analysis step-by-step:

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and run each notebook sequentially (01 through 06).

#### Running the Streamlit App

Launch the interactive web application for real-time churn predictions:

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn
- **Natural Language Processing**: NLTK
- **Web Application**: Streamlit
- **Development Environment**: Jupyter Notebook

## 📊 Model Performance

- **Churn Prediction Accuracy**: 85%+ (varies by model configuration)
- **Customer Segments Identified**: 3-5 distinct clusters
- **Sentiment Classification**: Rule-based and supervised learning approaches

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

Basant Khanal - https://github.com/Basantkhanal07

## 🙏 Acknowledgments

- Dataset source and any relevant acknowledgments
- Inspiration and references
- Community contributions

## 📧 Contact

For questions or feedback, please reach out:
- Email: me.basantkhanal07@gmail.com
- LinkedIn: https://www.linkedin.com/in/basantkhanal
- Project Link: https://github.com/Basantkhanal07/Customer_Behavior_Insights

---

**Made with ❤️ by Basant Khanal**