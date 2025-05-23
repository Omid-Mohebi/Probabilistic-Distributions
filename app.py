import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def generate_data(dist_name, params, size):
    if dist_name == 'Gaussian':
        return np.random.normal(loc=params['mean'], scale=params['std'], size=size)
    elif dist_name == 'Poisson':
        return np.random.poisson(lam=params['lam'], size=size)
    elif dist_name == 'Exponential':
        return np.random.exponential(scale=params['scale'], size=size)
    elif dist_name == 'Weibull':
        return np.random.weibull(a=params['shape'], size=size)
    elif dist_name == 'Uniform':
        return np.random.uniform(low=params['low'], high=params['high'], size=size)

def plot_data(data, bins):
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Sample Distribution Histogram')
    return fig

def main():
    st.title("Interactive Distribution Explorer")

    dist = st.sidebar.selectbox(
        "Select distribution",
        ['Gaussian', 'Poisson', 'Exponential', 'Weibull', 'Uniform']
    )
    size = st.sidebar.slider(
        "Sample size", 100, 10000, 1000, step=100
    )

    params = {}
    if dist == 'Gaussian':
        params['mean'] = st.sidebar.slider("Mean (μ)", -10.0, 10.0, 0.0)
        params['std']  = st.sidebar.slider("Std dev (σ)", 0.1, 10.0, 1.0)
    elif dist == 'Poisson':
        params['lam']  = st.sidebar.slider("Rate (λ)", 0.0, 20.0, 5.0)
    elif dist == 'Exponential':
        params['scale']= st.sidebar.slider("Scale (β)", 0.1, 10.0, 1.0)
    elif dist == 'Weibull':
        params['shape']= st.sidebar.slider("Shape (a)", 0.1, 10.0, 1.0)
    elif dist == 'Uniform':
        params['low']  = st.sidebar.slider("Lower bound", -10.0, 0.0, -1.0)
        params['high'] = st.sidebar.slider("Upper bound", 0.0, 10.0, 1.0)

    bins = st.sidebar.slider("Number of bins", 10, 100, 30)

    data = generate_data(dist, params, size)
    fig = plot_data(data, bins)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
