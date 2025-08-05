import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

def predict_2035_values(data_2015, data_2025):
    """
    Predict 2035 values based on 2015 and 2025 data using multiple ML approaches
    
    Args:
        data_2015: List or array of 2015 values
        data_2025: List or array of 2025 values
    
    Returns:
        Dictionary with predictions from different algorithms
    """
    
    # Prepare time series data
    years = np.array([2015, 2025]).reshape(-1, 1)
    target_year = np.array([[2035]])
    
    results = {}
    predictions_2035 = []
    
    # Process each data series
    for i, (val_2015, val_2025) in enumerate(zip(data_2015, data_2025)):
        values = np.array([val_2015, val_2025])
        
        print(f"\n--- Series {i+1} Analysis ---")
        print(f"2015 value: {val_2015:.6f}")
        print(f"2025 value: {val_2025:.6f}")
        
        # Calculate basic trend
        trend_change = val_2025 - val_2015
        trend_rate = trend_change / 10  # per year
        print(f"10-year change: {trend_change:.6f}")
        print(f"Annual trend: {trend_rate:.6f}")
        
        # Method 1: Linear Regression (RECOMMENDED)
        lr_model = LinearRegression()
        lr_model.fit(years, values)
        lr_pred = lr_model.predict(target_year)[0]
        
        # Method 2: Simple Linear Extrapolation
        simple_pred = val_2025 + (trend_rate * 10)  # 10 years forward
        
        # Method 3: Exponential Growth Model
        if val_2015 > 0 and val_2025 > 0:
            growth_rate = (val_2025 / val_2015) ** (1/10) - 1  # annual growth rate
            exp_pred = val_2025 * ((1 + growth_rate) ** 10)
        else:
            exp_pred = simple_pred
        
        print(f"\nPredictions for 2035:")
        print(f"Linear Regression: {lr_pred:.6f}")
        print(f"Simple Extrapolation: {simple_pred:.6f}")
        print(f"Exponential Growth: {exp_pred:.6f}")
        
        # Store results
        series_results = {
            'linear_regression': lr_pred,
            'simple_extrapolation': simple_pred,
            'exponential_growth': exp_pred,
            'trend_rate': trend_rate
        }
        results[f'series_{i+1}'] = series_results
        predictions_2035.append(lr_pred)  # Use linear regression as primary
    
    return results, predictions_2035

def visualize_predictions(data_2015, data_2025, predictions_2035):
    """Create visualization of the predictions"""
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    years = [2015, 2025, 2035]
    
    for i, (val_2015, val_2025, pred_2035) in enumerate(zip(data_2015, data_2025, predictions_2035)):
        if i < 6:  # Only plot first 6 series
            values = [val_2015, val_2025, pred_2035]
            
            axes[i].plot([2015, 2025], [val_2015, val_2025], 'bo-', label='Historical', linewidth=2)
            axes[i].plot([2025, 2035], [val_2025, pred_2035], 'ro--', label='Predicted', linewidth=2)
            axes[i].scatter([2035], [pred_2035], color='red', s=100, zorder=5)
            
            axes[i].set_title(f'Series {i+1} Prediction')
            axes[i].set_xlabel('Year')
            axes[i].set_ylabel('Value')
            axes[i].legend()
            axes[i].grid(True, alpha=0.3)
            
            # Add value annotations
            axes[i].annotate(f'{val_2015:.3f}', (2015, val_2015), textcoords="offset points", xytext=(0,10), ha='center')
            axes[i].annotate(f'{val_2025:.3f}', (2025, val_2025), textcoords="offset points", xytext=(0,10), ha='center')
            axes[i].annotate(f'{pred_2035:.3f}', (2035, pred_2035), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.savefig('/workspace/predictions_visualization.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return fig

# Example usage with your data from the spreadsheet
if __name__ == "__main__":
    # Data from your spreadsheet (visible rows)
    data_2015 = [0.333507228, 0.019714456, 1.000521684, 1.334028912, 1.667536139]
    data_2025 = [0.109658329, 0.219316658, 0.328974974, 0.438633299, 0.548291624]
    
    print("=== TIME SERIES PREDICTION FOR 2035 ===")
    print("Based on 2015 and 2025 data points")
    print("=" * 50)
    
    # Run predictions
    results, predictions_2035 = predict_2035_values(data_2015, data_2025)
    
    print(f"\n=== SUMMARY OF 2035 PREDICTIONS ===")
    for i, pred in enumerate(predictions_2035):
        print(f"Series {i+1}: {pred:.6f}")
    
    # Create visualization
    print(f"\nGenerating visualization...")
    visualize_predictions(data_2015, data_2025, predictions_2035)
    
    print(f"\n=== ALGORITHM RECOMMENDATION ===")
    print("BEST ALGORITHM: Linear Regression")
    print("REASONS:")
    print("1. Only 2 data points available - linear is most appropriate")
    print("2. Simple and interpretable")
    print("3. Good for trend extrapolation")
    print("4. Avoids overfitting with limited data")
    
    print(f"\nALTERNATIVE APPROACHES:")
    print("- If you can collect more historical data points, consider ARIMA or LSTM")
    print("- For non-linear patterns, polynomial regression might work")
    print("- For percentage-based growth, exponential models could be useful")