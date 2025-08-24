
import pandas
import numpy
import matplotlib.pyplot as pyplot


class LinearRegression:
    """
    Implements simple linear regression using a brute-force approach to fit a line to training data.
    """
    def __init__(self, x_train: pandas.Series, y_train: pandas.Series):
        """
        Initialize the LinearRegression object with training data.
        Args:
            x_train (pandas.Series): Feature values.
            y_train (pandas.Series): Target values.
        """
        self.x_train = x_train
        self.y_train = y_train
        self.m = len(self.x_train)
        self.base_line = numpy.linspace(x_train.min(), x_train.max(), 50)
        self.best_line = None
        self.best_line_id = None
        self.all_lines = []
        self.min_mse, self.best_slope, self.best_intercept = None, None, None

    def compute_slope(self, x1: float, x2: float, y1: float, y2: float) -> float:
        """
        Compute the slope (w) of the line passing through two points.
        """
        w = (y2 - y1) / (x2 - x1)
        return w

    def compute_intercept(self, m: float, x1: float, y1: float) -> float:
        """
        Compute the intercept (b) of the line given slope and a point.
        """
        b = y1 - m * x1
        return b

    def predict_y(self, x_value: float, w: float, b: float) -> float:
        """
        Predict the y value for a given x using the line equation.
        """
        y_predict = w * x_value + b
        return y_predict

    def compute_cost_function(self, w: float, b: float) -> float:
        """
        Compute the mean squared error cost function for given slope and intercept.
        """
        total_error = 0
        for i in range(self.m):
            y_predict = self.predict_y(self.x_train[i], w, b)
            error = y_predict - self.y_train[i]
            squared_error = error ** 2
            total_error += squared_error
        j_wb = ((1.0) / (self.m * 2.0)) * total_error
        return j_wb

    def compute_sum_squared_error(self, w: float, b: float) -> float:
        """
        Compute the sum of squared errors for the given line parameters.
        """
        J_wb = 2.0 * self.m * self.compute_cost_function(w=w, b=b)
        return J_wb
    
    def get_linear_function(self, do_plot=True):
        """
        Find the best-fit line for the training data by brute-force search over all pairs of points.
        Optionally plot the dataset and the best-fit line.
        """
        for i in range(1, len(self.x_train)):
            # Get two consecutive points
            x1, y1 = (self.x_train[i], self.y_train[i])
            x2, y2 = (self.x_train[i - 1], self.y_train[i - 1])
            # Compute slope and intercept for the line through these points
            slope = self.compute_slope(x1, x2, y1, y2)
            intercept = self.compute_intercept(m=slope, x1=x1, y1=y1)
            # Calculate mean squared error for this line
            mse = self.compute_sum_squared_error(w=slope, b=intercept)
            self.all_lines.append(slope * self.base_line + intercept)
            # Update best line if this one is better
            if self.best_line is None or mse < self.best_line[0]:
                self.best_line = (mse, slope, intercept)
                self.best_line_def = slope * self.base_line + intercept
                self.best_line_id = i - 1
        if self.best_line is not None:
            self.min_mse, self.best_slope, self.best_intercept = self.best_line
            self.linear_function_def = f"Best line: y = {self.best_slope:.3f}x + {self.best_intercept:.3f}, MSE = {self.min_mse:.3f}, id = {self.best_line_id}"
            print(self.linear_function_def)
            if do_plot:
                self.plot_dataset()
                # Plot the best-fit line
                pyplot.plot(self.base_line, self.best_line_def, color='r', linestyle='--')
                pyplot.savefig("./plot.png", dpi=150.0)
                pyplot.show()
        else:
            print("Warning: No best line found. Check if x_train and y_train have enough data.")

    def plot_dataset(self, clear=True):
        """
        Plot the training dataset as a scatter plot.
        """
        if clear:
            pyplot.clf()
        pyplot.scatter(self.x_train, self.y_train)
        pyplot.grid(True)
        pyplot.savefig("./plot.png")




        

