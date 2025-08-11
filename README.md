<!DOCTYPE html>
<html lang="en">

<body>

<header>
  <h1>Heart Disease Analysis Dashboard</h1>
  <p>Interactive Streamlit app for exploratory data analysis and basic machine learning on heart disease data</p>
 
</header>

<nav>
  <a href="#features">Features</a> |
  <a href="#pics">Screenshots</a> |
  <a href="#dataset">Dataset</a> |
  <a href="#install">Installation</a> |
  <a href="#usage">Usage</a> |
  <a href="#structure">Project Structure</a> 
  
</nav>

<section id="features">
  <h2>Features</h2>
  <ul>
    <li>Data Filtering: Interactive sliders and filters for age and sex (Male/Female/All).</li>
    <li>Visualizations: Scatter plots, logistic regression decision boundaries, boxplots, violin plots, density plots, chest pain countplots, and trends by age groups.</li>
    <li>Machine Learning: Random Forest classifier with feature importance visualization and correlation heatmap.</li>
    <li>Responsive UI: Runs locally via Streamlit at <code>http://localhost:8501</code>.</li>
  </ul>
</section>

<section id="pics">
 
  <h3>Screenshots</h3>
   <img src="assets/Screenshot 2025-08-11 113308.png" alt="Screenshot 1" width="600" />
  <br />
  <img src="assets/Screenshot 2025-08-11 113340.png" alt="Screenshot 2" width="600" />
  <br />
  <img src="assets/Screenshot 2025-08-11 113544.png" alt="Screenshot 3" width="600" />
</section>


<section id="dataset">
  <h2>Dataset</h2>
  <p>File: <code>modified_heart_dataset.csv</code></p>
  <p>Key columns include:</p>
  <ul>
    <li>age</li>
    <li>sex (0 = female, 1 = male)</li>
    <li>cholesterol</li>
    <li>max heart rate</li>
    <li>resting bp s</li>
    <li>oldpeak</li>
    <li>chest pain type</li>
    <li>target (0 = No Disease, 1 = Disease)</li>
  </ul>
</section>

<section id="install">
  <h2>Installation</h2>
  <ol>
    <li>Clone or download this repository to your local machine.</li>
    <li>Create a virtual environment (recommended):
      <pre>python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
      </pre>
    </li>
    <li>Install the required packages:
      <pre>pip install -r requirements.txt</pre>
      </pre>
    </li>
  </ol>
</section>

<section id="usage">
  <h2>Usage</h2>
  <p>Launch the Streamlit app with the following command, then open the displayed URL (default <code>http://localhost:8501</code>):</p>
  <pre>streamlit run data_analysis.py</pre>
  <p>What to expect:</p>
  <ul>
    <li>Interactive filters for age and sex at the top of the dashboard.</li>
    <li>Various plots visualizing trends, distributions, and model results.</li>
    <li>Random Forest model training with feature importance insights.</li>
  </ul>
</section>

<section id="structure">
  <h2>Project Structure</h2>
  <pre>
heart-disease-analysis/
├── data_analysis.py              # Main Streamlit app script
├── modified_heart_dataset.csv    # Dataset file
├── requirements.txt              # Python package dependencies
└── README.html                   # This documentation file
  </pre>
</section>


<footer>
  <p>© rachitneedcse — Heart Disease Analysis</p>
</footer>

</body>
</html>
