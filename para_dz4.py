import numpy as np

def pearson_correlation(x, y):
    x = np.array(x)
    y = np.array(y)
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    centered_x = x - mean_x
    centered_y = y - mean_y

    numerator = np.sum(centered_x * centered_y)
    denominator = (np.sum((centered_x)**2)) * (np.sum((centered_y)**2))
    correlation = numerator / np.sqrt(denominator)

    return correlation

if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 8, 9, 10]
    print(pearson_correlation(x, y))