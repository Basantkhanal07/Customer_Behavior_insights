# 📊 Customer Behavior Insights & Churn Prediction

A comprehensive machine learning project that analyzes customer behavior data to derive actionable business insights through data cleaning, exploratory data analysis, churn prediction, customer segmentation, and NLP-based sentiment analysis.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://customer-behavior-insights-basant.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)

## 🎯 Project Overview

This project implements an end-to-end data science pipeline to understand customer behavior patterns and predict churn. The analysis combines multiple machine learning techniques to provide business-ready insights that help organizations reduce customer attrition, optimize marketing strategies, and enhance operational efficiency.

**Note:** This project uses a synthetic dataset designed for educational purposes and machine learning practice.

---

## 🌐 Live Application & Repository

- 🚀 **Live Demo:** [customer-behavior-insights-basant.streamlit.app](https://customer-behavior-insights-basant.streamlit.app/)
- 💻 **GitHub:** [github.com/Basantkhanal07/Customer_Behavior_Insights](https://github.com/Basantkhanal07/Customer_Behavior_insights)

---

## ✨ Key Features

- **Churn Prediction**: Multi-model comparison (Random Forest, Logistic Regression, Decision Tree, KNN) achieving 72% accuracy
- **Customer Segmentation**: KMeans clustering identifying 3-5 distinct customer segments
- **Sentiment Analysis**: NLP-based analysis extracting insights from customer feedback
- **Interactive Dashboard**: Real-time predictions via deployed Streamlit web application
- **Model Evaluation**: Comprehensive performance analysis using accuracy, precision, recall, and F1-score
- **Business Recommendations**: Data-driven actionable insights for stakeholders

## 📊 Dataset Overview

### Dataset Characteristics
- **Size:** 300 customer records
- **Features:** 8 columns
- **ID Range:** Customer IDs from 1001 to 1300
- **Type:** Synthetic dataset (educational/practice purpose)

### Feature Description

| Column | Type | Description |
|--------|------|-------------|
| `CustomerID` | Integer | Unique identifier (1001-1300) |
| `Age` | Integer | Customer age |
| `Gender` | Categorical | Male/Female |
| `AnnualIncome` | Float | Annual income in currency units |
| `SpendingScore` | Integer | Spending behavior score (1-100) |
| `PurchaseHistory` | Categorical | Product categories: Electronics, Sports, Groceries, Home Decor, Fashion |
| `ReviewText` | Text | Customer feedback/reviews |
| `Churned` | Binary | Churn status (0 = Active, 1 = Churned) |

### Dataset Notes
- Synthetically generated for machine learning practice
- Review text contains representative feedback patterns
- Income and spending scores simulate realistic customer distributions
- Perfect for demonstrating end-to-end ML pipeline development

## 📁 Repository Structure

```
Customer_Behavior_Insights/
│
├── data/
│   ├── customer_behavior.csv              # Raw dataset (300 records)
│   └── customer_behavior_clean.csv        # Preprocessed dataset
│
├── notebooks/
│   ├── 01_data_understanding_cleaning.ipynb    # Data preprocessing
│   ├── 02_exploratory_data_analysis.ipynb      # EDA and visualization
│   ├── 03_churn_modeling.ipynb                 # Churn prediction models
│   ├── 04_customer_segmentation.ipynb          # KMeans clustering
│   ├── 05_nlp_analysis.ipynb                   # Sentiment analysis
│   └── 06_final_business_rec.ipynb             # Business insights
│
├── app.py                                  # Streamlit application
├── requirements.txt                        # Python dependencies
├── .gitignore                             # Git ignore rules
└── README.md                              # Project documentation
```

## 🔬 Analysis Workflow

### 1. Data Understanding & Cleaning
- Loads and explores 300 customer records across 8 features
- Handles missing values and duplicate records
- Encodes categorical variables (Gender, PurchaseHistory) for machine learning
- Feature engineering and data type optimization
- Outputs cleaned dataset for downstream analysis

### 2. Exploratory Data Analysis (EDA)
- Generates descriptive statistics (age, income, spending score)
- Visualizes data distributions using histograms and box plots
- Analyzes relationships between variables using scatter plots and correlation matrices
- Examines purchase history patterns across product categories
- Identifies churn patterns by demographic and behavioral features

### 3. Churn Prediction Modeling
- Defines and engineers binary churn target variable
- Performs feature selection and standardization
- Trains and compares 4 classification algorithms:
  - **Logistic Regression** - 72% accuracy (baseline)
  - **Random Forest** - 70.67% accuracy, 44.44% precision
  - **Decision Tree** - 66.67% accuracy
  - **K-Nearest Neighbors** - 70.67% accuracy
- Evaluates models using accuracy, precision, recall, F1-score, and confusion matrices
- Analyzes class imbalance challenges in churn prediction
- Identifies high-risk customers for retention campaigns

### 4. Customer Segmentation
- Standardizes features for clustering analysis
- Applies KMeans algorithm with optimal cluster selection (Elbow method)
- Identifies 3-5 distinct customer segments based on:
  - Demographics (Age, Gender)
  - Financial profile (Annual Income)
  - Behavior (Spending Score, Purchase History)
- Reduces dimensionality using PCA for 2D visualization
- Assigns cluster labels and creates customer segment profiles

### 5. NLP Sentiment Analysis
- Preprocesses review text data (lowercasing, stopword removal, tokenization)
- Analyzes word frequency and common feedback themes
- Classifies sentiment using rule-based approaches
- Visualizes sentiment distribution across customer base
- Extracts key complaints (pricing, service quality) and positive highlights (product quality, delivery)

### 6. Business Recommendations
- Synthesizes insights from all analytical components
- Develops churn reduction strategies based on predictive models
- Creates segment-specific marketing recommendations
- Proposes operational improvements based on sentiment analysis
- Delivers actionable roadmap for customer retention and revenue optimization

## 💡 Key Business Insights

### Churn Reduction Strategies
- **Targeted Retention Campaigns**: Personalized emails and discount coupons for at-risk customers identified by Random Forest model (44% precision)
- **Proactive Support**: Priority customer service for customers flagged by churn prediction system
- **Loyalty Programs**: Rewards and incentives for high-spending customers showing early churn signals
- **Win-Back Campaigns**: Re-engagement strategies for churned customers in high-value segments

### Segment-Based Marketing
- **High Income / Low Spend**: Premium product bundles, concierge support, exclusive experiences
- **Mid Income / Mid Spend**: Seasonal promotions, value-added offers, referral incentives
- **Low Income / High Spend**: Membership programs, loyalty points, volume discounts
- **Category-Specific**: Targeted campaigns by purchase history (Electronics, Fashion, etc.)

### Product & Operations Improvements
- **Pricing Strategy**: Address pricing concerns identified in negative sentiment feedback
- **Service Excellence**: Continue emphasizing fast delivery and product quality (top positive sentiment drivers)
- **Feedback Loop**: Implement continuous sentiment monitoring system
- **Quality Assurance**: Focus on Electronics and Fashion categories based on review patterns

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)
- Jupyter Notebook (for exploring analysis notebooks)

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

Explore the complete analysis pipeline step-by-step:

```bash
jupyter notebook
```

Navigate to the `notebooks/` directory and run each notebook sequentially:
1. `01_data_understanding_cleaning.ipynb` - Data preprocessing
2. `02_exploratory_data_analysis.ipynb` - Statistical analysis and visualization
3. `03_churn_modeling.ipynb` - Model training and evaluation
4. `04_customer_segmentation.ipynb` - Clustering analysis
5. `05_nlp_analysis.ipynb` - Sentiment analysis
6. `06_final_business_rec.ipynb` - Business recommendations

#### Running the Streamlit App Locally

Launch the interactive web application for real-time churn predictions:

```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

**Or access the live deployment:** [customer-behavior-insights-basant.streamlit.app](https://customer-behavior-insights-basant.streamlit.app/)

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn
- **Natural Language Processing**: NLTK
- **Web Application**: Streamlit
- **Development Environment**: Jupyter Notebook
- **Version Control**: Git, GitHub
- **Deployment**: Streamlit Cloud

## 📈 Model Performance Summary

### Churn Prediction Models

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Logistic Regression** | **72.00%** | 0.00% | 0.00% | 0.00% |
| **Random Forest** | 70.67% | **44.44%** | **19.05%** | **26.67%** |
| **Decision Tree** | 66.67% | 38.89% | 33.33% | 35.90% |
| **KNN** | 70.67% | 40.00% | 9.52% | 15.38% |

**Key Findings:**
- Logistic Regression achieved highest accuracy (72%) but shows class imbalance issues
- Random Forest demonstrates best balanced performance for minority class (churned customers)
- Class imbalance is a key challenge - typical in real-world churn prediction scenarios
- Future improvements: SMOTE, class weighting, ensemble methods

### Customer Segmentation
- **Clusters Identified**: 3-5 distinct customer segments
- **Segmentation Features**: Age, Income, Spending Score, Purchase History
- **Validation**: Elbow method for optimal cluster selection
- **Visualization**: PCA-based 2D representation

### Sentiment Analysis
- **Approach**: Rule-based sentiment classification
- **Text Processing**: Tokenization, stopword removal, frequency analysis
- **Insights**: Identified key themes in positive and negative feedback
- **Business Value**: Actionable insights for product and service improvement

## 🎯 Key Learnings & Technical Highlights

1. **End-to-End ML Pipeline**: Complete workflow from data cleaning to deployment
2. **Model Evaluation**: Comprehensive analysis using multiple metrics beyond accuracy
3. **Class Imbalance Handling**: Identified and documented real-world ML challenge
4. **Multi-Model Comparison**: Systematic evaluation of 4 different algorithms
5. **Business Translation**: Converting technical insights into actionable recommendations
6. **Deployment**: Production-ready Streamlit application on cloud platform
7. **Unsupervised Learning**: KMeans clustering for customer segmentation
8. **NLP Implementation**: Text preprocessing and sentiment analysis pipeline

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Basant Khanal**
- GitHub: [@Basantkhanal07](https://github.com/Basantkhanal07)
- LinkedIn: [basantkhanal](https://www.linkedin.com/in/basantkhanal)
- Email: me.basantkhanal07@gmail.com

## 🙏 Acknowledgments

- Synthetic dataset created for educational and machine learning practice purposes
- Inspiration from real-world customer analytics and churn prediction use cases
- Open-source community for tools and libraries (Scikit-learn, Streamlit, NLTK)
- Data science community for best practices and methodologies

## 📧 Contact

For questions, feedback, or collaboration opportunities:
- **Email**: me.basantkhanal07@gmail.com
- **LinkedIn**: [linkedin.com/in/basantkhanal](https://www.linkedin.com/in/basantkhanal)
- **Project Link**: [github.com/Basantkhanal07/Customer_Behavior_Insights](https://github.com/Basantkhanal07/Customer_Behavior_Insights)

---

**⭐ If you found this project helpful, please consider giving it a star!**

**Made with ❤️ by Basant Khanal**