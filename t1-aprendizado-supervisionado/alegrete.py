import numpy as np

def compute_mse(b, w, data):
    land_area = data.iloc[:, 0]
    real_land_price = data.iloc[:, 1]

    predicted_land_price = b + w*land_area

    return np.mean((predicted_land_price - real_land_price) ** 2)


def step_gradient(b, w, data, alpha):
    land_area = data.iloc[:, 0]
    real_land_price = data.iloc[:, 1]

    predicted_land_price = b + w*land_area

    error = predicted_land_price - real_land_price

    gradient_w = (1 / len(real_land_price)) * np.sum(error * land_area)
    gradient_b = (1 / len(real_land_price)) * np.sum(error)

    return w - alpha * gradient_w, b - alpha * gradient_b


def fit(data, b, w, alpha, num_iterations):
    w_list = []
    b_list = []

    for i in range(num_iterations):
        buffer_w, buffer_b = step_gradient(b, w, data, alpha)
        w_list.append(buffer_w)
        b_list.append(buffer_b)
        
    return w_list, b_list
