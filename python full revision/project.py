import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate synthetic data (y = 2x + 3 + some noise)
np.random.seed(42)  # for reproducibility
X = np.random.rand(100, 1) * 10  # 100 points between 0-10
y = 2 * X + 3 + np.random.randn(100, 1) * 2  # slope=2, intercept=3, noise=2

print(f"Data shape: X {X.shape}, y {y.shape}")
print(f"First 5 X values: {X[:5].flatten()}")
print(f"First 5 y values: {y[:5].flatten()}")
plt.figure(figsize=(8, 5))
plt.scatter(X, y, alpha=0.6, color='blue', label='Data points')
plt.xlabel('X (Feature)', fontsize=12)
plt.ylabel('y (Target)', fontsize=12)
plt.title('Our Synthetic Data (Real line: y = 2x + 3)', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.m = None  # slope (weight)
        self.c = None  # intercept (bias)
        self.costs = []  # store cost history for visualization
        
    def fit(self, X, y):
        """Train the model using gradient descent"""
        n_samples = X.shape[0]
        
        # Initialize parameters
        self.m = np.random.randn()  # random starting slope
        self.c = np.random.randn()  # random starting intercept
        
        # Gradient descent loop
        for i in range(self.n_iterations):
            # Forward pass: calculate predictions
            y_pred = self.m * X + self.c
            
            # Calculate cost (MSE)
            cost = (1/n_samples) * np.sum((y - y_pred) ** 2)
            self.costs.append(cost)
            
            # Calculate gradients
            dm = (-2/n_samples) * np.sum(X * (y - y_pred))
            dc = (-2/n_samples) * np.sum(y - y_pred)
            
            # Update parameters
            self.m = self.m - self.lr * dm
            self.c = self.c - self.lr * dc
            
            # Print progress every 100 iterations
            if i % 100 == 0:
                print(f"Iteration {i:4d} | Cost: {cost:.4f} | m: {self.m:.4f} | c: {self.c:.4f}")
    
    def predict(self, X):
        """Make predictions"""
        return self.m * X + self.c

# Create and train model
model = LinearRegressionScratch(learning_rate=0.02, n_iterations=500)
model.fit(X, y)

print("\n" + "="*50)
print(f"Final parameters:")
print(f"  Learned m (slope): {model.m:.4f}")
print(f"  Learned c (intercept): {model.c:.4f}")
print(f"  Actual should be: m=2.00, c=3.00")
print("="*50)
# Plot 1: Data with fitted line
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X, y, alpha=0.6, color='blue', label='Data points')
X_line = np.array([[0], [10]])
y_line = model.predict(X_line)
plt.plot(X_line, y_line, color='red', linewidth=2, label='Fitted line')
plt.xlabel('X', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Linear Regression Result', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

# Plot 2: Cost reduction over time
plt.subplot(1, 2, 2)
plt.plot(model.costs, color='green', linewidth=2)
plt.xlabel('Iterations', fontsize=12)
plt.ylabel('Cost (MSE)', fontsize=12)
plt.title('Cost Function Decreasing', fontsize=14)
plt.grid(True, alpha=0.3)
plt.yscale('log')  # log scale to see improvement better

plt.tight_layout()
plt.show()
Step 6: 🔥 LIVE Animation (Babbal part)
python
# This shows the line moving during training
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X, y, alpha=0.6, color='blue', label='Data')
line, = ax.plot([], [], color='red', linewidth=2, label='Fitting line')
ax.set_xlim(0, 10)
ax.set_ylim(0, 25)
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Gradient Descent in Action')
ax.legend()
ax.grid(True, alpha=0.3)

# Store iteration info
iteration_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, 
                         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

def animate(frame):
    """Animate one step of training"""
    if frame == 0:
        # Reset model
        model.m = np.random.randn()
        model.c = np.random.randn()
        model.costs = []
    
    # Do one iteration of training
    n_samples = X.shape[0]
    y_pred = model.m * X + model.c
    cost = (1/n_samples) * np.sum((y - y_pred) ** 2)
    model.costs.append(cost)
    
    # Calculate gradients
    dm = (-2/n_samples) * np.sum(X * (y - y_pred))
    dc = (-2/n_samples) * np.sum(y - y_pred)
    
    # Update parameters
    model.m = model.m - model.lr * dm
    model.c = model.c - model.lr * dc
    
    # Update visualization
    X_line = np.array([[0], [10]])
    y_line = model.m * X_line + model.c
    line.set_data(X_line, y_line)
    iteration_text.set_text(f'Iter: {frame+1} | m={model.m:.3f} | c={model.c:.3f} | Cost={cost:.3f}')
    
    return line, iteration_text

# Create anima
anim = FuncAnimation(fig, animate, frames=200, interval=50, repeat=False)
plt.tight_layout()
plt.show()
from sklearn.datasets import make_regression

# Generate more complex data
X_real, y_real = make_regression(n_samples=200, n_features=1, noise=20, random_state=42)
y_real = y_real.reshape(-1, 1)

# Train
model_real = LinearRegressionScratch(learning_rate=0.01, n_iterations=1000)
model_real.fit(X_real, y_real)

# Predict
y_pred_real = model_real.predict(X_real)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(X_real, y_real, alpha=0.5, label='Actual data')
plt.scatter(X_real, y_pred_real, alpha=0.5, color='red', label='Predictions')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Linear Regression on Synthetic Dataset')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()