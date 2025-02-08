# Model Card


## Model Details
**Model Type:** Random Forest Classifier  
**Developed By:** Sean Sasser  
**Version:** 1.0  
**License:** Open-source  
**Frameworks Used:** Scikit-learn, FastAPI  
**Python Version:** 3.10  

## Intended Use
This model is designed to predict whether an individual's income is greater than $50K or not based on demographic and work-related attributes. The model is used for educational purposes to demonstrate deploying a machine learning pipeline with FastAPI.

## Training Data
The model was trained using the **UCI Adult Census Income Dataset**, which consists of structured tabular data containing features such as age, work class, education, occupation, relationship status, and income level. The dataset was preprocessed to encode categorical variables and remove null values.

## Evaluation Data
A separate validation set, derived from the same UCI Adult Census Income dataset, was used to evaluate the model's performance. The data split was **80% training and 20% testing**.

## Metrics
The following performance metrics were used to evaluate the model:
- **Precision:** Measures the proportion of true positive predictions among all positive predictions made by the model.
- **Recall:** Measures the proportion of actual positive cases correctly identified by the model.
- **F1 Score:** The harmonic mean of precision and recall, balancing both.
- **Accuracy:** The proportion of total correct predictions.

**Model Performance:**
- **Precision:** 0.74
- **Recall:** 0.63
- **F1 Score:** 0.68
- **Accuracy:** 0.78

## Ethical Considerations
- **Bias in Data:** Since the model is trained on census data, it may inherit biases related to race, gender, or socioeconomic factors. 
- **Fairness:** The model’s predictions should not be used for discriminatory decision-making processes. 
- **Privacy Concerns:** The data contains sensitive information; ensure compliance with privacy regulations when handling personal data.
- **Transparency:** Users should be aware of the model’s limitations and not use it for high-stakes decision-making.

## Caveats and Recommendations
- The model is a simple classification model and may not generalize well beyond the dataset it was trained on.
- The data is based on the U.S. Census, so predictions may not be applicable in other countries or time periods.

