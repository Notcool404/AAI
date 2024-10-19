import pandas as pd
def bayes_theorem(prior_A, likelihood_B_given_A, marginal_B):
    """
    Calculate the posterior probability using Bayes' Theorem
    :param prior_A: P(A) - Prior probability of A
    :param likelihood_B_given_A: P(B|A) - Likelihood of B given A
    :param marginal_B: P(B) - Marginal probability of B
    6
    :return: P(A|B) - Posterior probability of A given B
    """
    return (likelihood_B_given_A * prior_A) / marginal_B

# Load the Iris dataset
def load_iris_dataset(file_path):
    return pd.read_csv(file_path)

# Calculate prior probability P(A)
def calculate_prior(data, class_col, class_value):
    return len(data[data[class_col] == class_value]) / len(data)

# Calculate likelihood P(B|A)
def calculate_likelihood(data, class_col, class_value, feature_col,feature_condition):
    subset = data[data[class_col] == class_value]
    return len(subset[subset[feature_col] > feature_condition]) / len(subset)

# Calculate marginal probability P(B)
def calculate_marginal(data, feature_col, feature_condition):
    return len(data[data[feature_col] > feature_condition]) / len(data)

# Apply Bayes' Theorem on the Iris dataset
def apply_bayes_to_iris(file_path, class_col, class_value, feature_col, feature_condition):
    # Load dataset
    data = load_iris_dataset(file_path)
    # Calculate prior P(A)
    prior_A = calculate_prior(data, class_col, class_value)
    # Calculate likelihood P(B|A)
    likelihood_B_given_A = calculate_likelihood(data, class_col,
    class_value, feature_col, feature_condition)
    # Calculate marginal probability P(B)
    marginal_B = calculate_marginal(data, feature_col, feature_condition)
    # Apply Bayes' Theorem
    posterior_A_given_B = bayes_theorem(prior_A, likelihood_B_given_A,
    marginal_B)
    return posterior_A_given_B

# Example usage:
# Assume we want to calculate the probability P(Class='setosa' | SepalLength > 5.0)
file_path = 'iris.csv' # Path to the iris dataset file
class_col = 'species' # The column representing the class (A)
class_value = 'virginica' # The class value we're interested in (A)
feature_col = 'sepal_length' # The feature we're using (B)
feature_condition = 5.0 # The condition on the feature (B > 5.0)

# Calculate posterior probability P(setosa|sepal_length > 5.0)
posterior_probability = apply_bayes_to_iris(file_path, class_col,
class_value, feature_col, feature_condition)
print(f"P({class_value} | {feature_col} > {feature_condition}) = {posterior_probability:.4f}")
print()
