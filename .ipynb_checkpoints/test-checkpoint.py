import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from io import BytesIO
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# Load data
df = pd.read_csv('modified_heart_dataset.csv')
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    /* Main content area */
    .block-container {
        width: 90%;
        background-color: black;
        padding: 100px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
# Sidebar 
st.title(":blue[Heart-Disease Analysis]")
age_filter = st.slider("Age", int(df['age'].min()), int(df['age'].max()), 
                               (int(df['age'].min()), int(df['age'].max())))
sex_filter = st.selectbox("Sex", options=['All', 'Male', 'Female'])


filtered_data = df[(df['age'] >= age_filter[0]) & (df['age'] <= age_filter[1])]
if sex_filter != 'All':
    filtered_data = filtered_data[filtered_data['sex'] == (1 if sex_filter == 'Male' else 0)]


col1, col2 ,col3= st.columns(3)



with col1:
    st.subheader("Scatter Plot of Age vs. Cholesterol")
    y = plt.figure(figsize=(5.6, 4))  # Larger size
    # sns.scatterplot(data=filtered_data, x="age", y="cholesterol", hue="target")
    sns.regplot(data=filtered_data, x='age', y='cholesterol', scatter_kws={'alpha':0.6}, line_kws={"color":"red"})
    st.pyplot(y)

with col2:
    st.subheader("Age vs Max Heart Rate with Decision Boundary")

    
    X = filtered_data[['age', 'max heart rate']].values
    y = filtered_data['target'].values

    
    model = LogisticRegression()
    model.fit(X, y)

    # Generate a mesh grid for plotting decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

   
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    
    plt.figure(figsize=(6, 4))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    colors = {0: 'blue', 1: 'red'}
    for class_value in np.unique(y):
        if class_value == 0:
            label = "Not Infected"  # For class 0
        else:
            label = "Infected"  # For class 1
    
        plt.scatter(
            X[y == class_value, 0], X[y == class_value, 1],
            color=colors[class_value], edgecolor='k', s=50,
            label=label
        )    
    plt.xlabel("Age")
    plt.ylabel("Max Heart Rate")
    plt.title("Decision Boundary (Age vs. Max Heart Rate)")
     
    plt.legend(loc=1)

    
    st.pyplot(plt)


with col3:
    st.subheader("Cholesterol Levels by Heart Disease Status")
    z = plt.figure(figsize=(5.6, 4))  # Larger size
    sns.boxplot(data=filtered_data, x="target", y="cholesterol")
    st.pyplot(z)


st.markdown("<hr style='border: 1px solid #FF6347;'>", unsafe_allow_html=True)
st.subheader("Chest Pain Type vs. Heart Disease Status")


option = st.selectbox(
    "Select Heart Disease Status to Display:",
    ("Both", "Disease", "No Disease")
)
palette = {0: "blue", 1: "red"}


if option == "Disease":
    filtered_df = df[df['target'] == 1]
elif option == "No Disease":
    filtered_df = df[df['target'] == 0]
else:
    filtered_df = df  


fig4, ax4 = plt.subplots(figsize=(9, 6))
sns.countplot(data=filtered_df, x='chest pain type', hue='target', palette=palette, ax=ax4)
ax4.set_xlabel("Chest Pain Type")
ax4.set_ylabel("Count")
ax4.set_title("Chest Pain Type vs. Target (Heart Disease)")


if option == "Both":
    ax4.legend(title="Heart Disease", labels=["No Disease", "Disease"])
elif option == "Disease":
    ax4.legend(title="Heart Disease", labels=["Disease"])
else:
    ax4.legend(title="Heart Disease", labels=["No Disease"])


buf = BytesIO()
fig4.savefig(buf, format="png")
buf.seek(0)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image(buf,use_column_width=True)
#---------------------------------------------------------
st.markdown("<hr style='border: 1px solid #FF6347;'>", unsafe_allow_html=True)

st.header("Violin Plot")
feature = st.selectbox(
    "Select Feature to Plot",
    ('age', 'cholesterol', 'resting bp s')
)
st.subheader(f"{feature.capitalize()} by Heart Disease Status")

if feature=='age':
    
    age_range = st.slider("Select Age Range", int(df['age'].min()), int(df['age'].max()), 
                              (int(df['age'].min()), int(df['age'].max())))


    filtered_df = df[(df['age'] >= age_range[0]) & (df['age'] <= age_range[1])]
else:
    filtered_df=df



fig, ax = plt.subplots(figsize=(9, 6))
sns.violinplot(data=filtered_df, x='target', y=feature, palette="Set2", split=True, ax=ax)
ax.set_title(f"Violin Plot of {feature.capitalize()} by Heart Disease Status")
ax.set_xlabel("Heart Disease Status (0 = No, 1 = Yes)")
ax.set_ylabel(feature.capitalize())
buf = BytesIO()
fig.savefig(buf, format="png")
buf.seek(0)
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image(buf,use_column_width=True)

st.markdown("<hr style='border: 1px solid #FF6347;'>",    unsafe_allow_html=True
)

col1,col2=st.columns(2,gap="medium")

with col1:

    
    features = ['age', 'max heart rate', 'cholesterol', 'resting bp s', 'oldpeak']


    x_limits = {
        'cholesterol': (df['cholesterol'].min(), df['cholesterol'].max()),
        'oldpeak': (df['oldpeak'].min(), df['oldpeak'].max())
    }
    
    
    selected_feature = st.selectbox("Choose a feature to display:", features)
    st.subheader(f"Density Plot of {selected_feature.capitalize()} ")
    
    
    fig, ax = plt.subplots(figsize=(5.6, 4))
    sns.kdeplot(data=df, x=selected_feature, hue='target', fill=True, common_norm=False, palette="coolwarm", ax=ax)
    
   
    ax.set_xlabel(selected_feature.capitalize())
    ax.set_ylabel("Density")
    
    
    if selected_feature in x_limits:
        ax.set_xlim(x_limits[selected_feature])
    elif selected_feature == 'resting bp s':
        ax.set_xlim(50, df['resting bp s'].max()) 
    
    
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    
    
    st.image(buf, use_column_width=True)

with col2:
    age_bins = list(range(20, 90, 5))
    age_labels = [f"{age}-{age+4}" for age in age_bins[:-1]]
    
   
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    age_group_data = df.groupby(['age_group', 'target'])[['cholesterol', 'max heart rate']].mean().reset_index()
    
    
    sns.set(style="whitegrid")
    
   
    plot_option = st.selectbox(
        "Select a Plot to Display",
        ("Cholesterol Level Trend", "Max Heart Rate Trend")
    )
    st.subheader(f"{plot_option.capitalize()} by Age Groups")
    age_group_data['target'] = age_group_data['target'].map({0: 'Not Infected', 1: 'Infected'})
    if plot_option == "Cholesterol Level Trend":
        
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=age_group_data, x='age_group', y='cholesterol', hue='target', marker='o', palette={'Not Infected': 'blue', 'Infected': 'red'}, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
       
        ax.set_xlabel("Age Group")
        ax.set_ylabel("Average Cholesterol")
        ax.legend(title="Heart Disease Status:",loc=1)
        st.pyplot(fig)
    
    elif plot_option == "Max Heart Rate Trend":
       
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=age_group_data, x='age_group', y='max heart rate', hue='target', marker='o', palette={'Not Infected': 'blue', 'Infected': 'red'}, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title("Max Heart Rate Trend Across Age Groups by Heart Disease Status")
        ax.set_xlabel("Age Group")
        ax.set_ylabel("Average Max Heart Rate")
        ax.legend(title="Heart Disease Status")
        st.pyplot(fig)

st.markdown("<hr style='border: 1px solid #FF6347;'>",    unsafe_allow_html=True
)


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


df = pd.read_csv('modified_heart_dataset.csv')


X = df.drop(columns=['target'])
y = df['target']  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


rf_model = RandomForestClassifier(n_estimators=100, random_state=42)


rf_model.fit(X_train, y_train)


feature_importances = rf_model.feature_importances_


feature_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': feature_importances
})


feature_df = feature_df.sort_values(by='Importance', ascending=False)


def plot_feature_importance():
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_df, ax=ax, palette='viridis')
    ax.set_title("Feature Importance for Predicting Heart Disease")
    ax.set_xlabel("Importance")
    ax.set_ylabel("Feature")
    st.pyplot(fig)


def plot_correlation_heatmap():
    
    correlation_matrix = df.corr()
    
   
    plt.figure(figsize=(9, 6))
    
   
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm_r', vmin=-1, vmax=1, square=True, fmt=".2f", linewidths=0.5)
    
    
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        # Show the plot
        st.pyplot(plt)

st.subheader("Correlation/Importance between features:")


plot_option = st.selectbox(
    "Choose a graph to display:",
    ("Feature Importance", "Correlation Heatmap")
)

# Display the selected plot
if plot_option == "Feature Importance":
    plot_feature_importance()
elif plot_option == "Correlation Heatmap":
    plot_correlation_heatmap()
