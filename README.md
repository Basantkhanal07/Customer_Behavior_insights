📊 Customer Behavior Insights
Project Overview:
This project analyzes customer behavior data to derive actionable business insights using data cleaning, exploratory data analysis (EDA), churn prediction, customer segmentation, and NLP-based sentiment analysis.
The final outcome includes business recommendations to reduce churn, improve marketing, and enhance operations.
________________________________________
Customer Behavior & Churn Prediction App

A machine learning web application that predicts customer churn based on
demographics, income, spending behavior, and purchase history.

Features:
- Churn prediction using Random Forest
- Interactive Streamlit UI
- Real-time predictions
- Business-ready insights
________________________________________
📂 Repository Structure
Customer_Behavior_Insights/
│
├── data/
│   ├── customer_behavior.csv
│   ├── customer_behavior_clean.csv
│   └── customer_behavior_project_instructions.md
│
├── notebooks/
│   ├── 01_data_understanding_cleaning.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_churn_modeling.ipynb
│   ├── 04_customer_segmentation.ipynb
│   ├── 05_nlp_analysis.ipynb
│   └── 06_final_business_rec.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
________________________________________
Notebook Descriptions:
01_data_understanding_cleaning.ipynb
•	Loads raw customer data
•	Handles missing values and duplicates
•	Encodes categorical variables
•	Saves cleaned dataset for downstream analysis
________________________________________
02_exploratory_data_analysis.ipynb
•	Descriptive statistics (age, income, spending score)
•	Distribution analysis using histograms
•	Relationship analysis using scatter plots
•	Purchase history frequency analysis
________________________________________
03_churn_modeling.ipynb
•	Defines churn target variable
•	Feature selection and scaling
•	Trains classification model (Logistic Regression)
•	Evaluates model using accuracy and confusion matrix
•	Identifies at-risk customers
________________________________________
04_customer_segmentation.ipynb
•	Feature standardization
•	KMeans clustering
•	Elbow method to select optimal clusters
•	PCA for 2D visualization
•	Assigns cluster labels to customers
________________________________________
05_nlp_analysis.ipynb
•	Text preprocessing (lowercasing, stopword removal)
•	Word frequency analysis
•	Rule-based sentiment classification
•	Visualizes sentiment distribution
•	Extracts key complaints and positive highlights
________________________________________
06_final_business_recommendation.ipynb
Integrates results from all analyses
•	Churn reduction strategies
•	Segment-specific marketing actions
•	Operational & product improvement insights
________________________________________
Key Business Recommendations
Churn Reduction:
•	Target churned customers with retention emails and coupons
•	Prioritize support for at-risk users
•	Introducing loyalty rewards for high-spending churned users
Segment-Based Marketing:
•	High-income / Low-spend: Premium bundles & concierge support
•	Mid-income / Mid-spend: Seasonal promotions
•	Low-income / High-spend: Membership and loyalty plans
Product & Operations:
•	Address pricing complaints from negative reviews
•	Continue emphasizing fast delivery and product quality
________________________________________
Installation & Setup:
pip install -r requirements.txt
________________________________________
Technologies Used:
•	Python
•	Pandas, NumPy
•	Matplotlib, Seaborn
•	Scikit-learn
•	NLTK
________________________________________
How to Run the Project
1. Clone Repository
git clone <your-repo-url>
cd Customer_Behavior_Insights
2. Setup Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Notebooks
•	Open Jupyter Notebook and run each notebook step-by-step:
jupyter notebook
5. Run Streamlit App
streamlit run app.py
•	Open the URL in your browser to interact with the app.

