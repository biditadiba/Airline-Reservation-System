#!/usr/bin/env python3
"""
Simple Time Series Prediction for 2035
Based on 2015 and 2025 data points using Linear Regression
"""

def linear_regression_prediction(x1, y1, x2, y2, target_x):
    """
    Simple linear regression between two points
    """
    # Calculate slope (m) and intercept (b) for y = mx + b
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    
    # Predict target value
    target_y = m * target_x + b
    return target_y, m, b

def predict_2035_values():
    """
    Predict 2035 values based on your spreadsheet data
    """
    # Your data from the spreadsheet
    data_2015 = [0.333507228, 0.019714456, 1.000521684, 1.334028912, 1.667536139]
    data_2025 = [0.109658329, 0.219316658, 0.328974974, 0.438633299, 0.548291624]
    
    print("=" * 60)
    print("TIME SERIES PREDICTION FOR 2035")
    print("Best Algorithm: LINEAR REGRESSION")
    print("=" * 60)
    
    predictions_2035 = []
    
    for i, (val_2015, val_2025) in enumerate(zip(data_2015, data_2025)):
        print(f"\n--- Series {i+1} Analysis ---")
        print(f"2015 value: {val_2015:.6f}")
        print(f"2025 value: {val_2025:.6f}")
        
        # Calculate trend
        trend_change = val_2025 - val_2015
        annual_trend = trend_change / 10
        print(f"10-year change: {trend_change:.6f}")
        print(f"Annual trend: {annual_trend:.6f}")
        
        # Linear regression prediction
        pred_2035, slope, intercept = linear_regression_prediction(2015, val_2015, 2025, val_2025, 2035)
        predictions_2035.append(pred_2035)
        
        # Alternative: Simple extrapolation
        simple_pred = val_2025 + (annual_trend * 10)
        
        print(f"Linear Regression: {pred_2035:.6f}")
        print(f"Simple Extrapolation: {simple_pred:.6f}")
        print(f"Equation: y = {slope:.6f}x + {intercept:.2f}")
    
    print("\n" + "=" * 60)
    print("FINAL 2035 PREDICTIONS")
    print("=" * 60)
    
    for i, pred in enumerate(predictions_2035):
        print(f"Series {i+1}: {pred:.6f}")
    
    return predictions_2035

def create_ascii_visualization(data_2015, data_2025, predictions_2035):
    """
    Create ASCII visualization of the predictions
    """
    print("\n" + "=" * 60)
    print("VISUALIZATION - TREND ANALYSIS")
    print("=" * 60)
    
    for i, (val_2015, val_2025, pred_2035) in enumerate(zip(data_2015, data_2025, predictions_2035)):
        print(f"\nSeries {i+1} Trend:")
        print(f"2015: {val_2015:.3f} |" + "█" * min(int(val_2015 * 20), 50))
        print(f"2025: {val_2025:.3f} |" + "█" * min(int(val_2025 * 20), 50))
        print(f"2035: {pred_2035:.3f} |" + "█" * min(int(pred_2035 * 20), 50) + " ← PREDICTION")
        
        # Show trend direction
        if pred_2035 > val_2025:
            trend = "↗ INCREASING"
        elif pred_2035 < val_2025:
            trend = "↘ DECREASING"
        else:
            trend = "→ STABLE"
        
        print(f"Trend: {trend}")

def generate_summary_report():
    """
    Generate final summary with algorithm recommendation
    """
    print("\n" + "=" * 60)
    print("ALGORITHM RECOMMENDATION REPORT")
    print("=" * 60)
    
    print("BEST ALGORITHM: LINEAR REGRESSION")
    print("\nREASONS:")
    print("✓ Only 2 data points available - linear is most statistically sound")
    print("✓ Simple and interpretable results")
    print("✓ Good for trend extrapolation over time")
    print("✓ Avoids overfitting with limited data")
    print("✓ Provides consistent, reliable predictions")
    
    print("\nALTERNATIVE ALGORITHMS (if more data available):")
    print("• ARIMA - For complex time series with seasonality")
    print("• LSTM Neural Networks - For non-linear patterns")
    print("• Polynomial Regression - For curved growth patterns")
    print("• Exponential Smoothing - For exponential growth/decay")
    
    print("\nCONFIDENCE LEVEL:")
    print("Medium - Limited to 2 data points, but linear trend is appropriate")
    
    print("\nRECOMMENDATIONS:")
    print("1. Collect more historical data points for better accuracy")
    print("2. Consider external factors that might influence trends")
    print("3. Validate predictions with domain expertise")
    print("4. Update model as new data becomes available")

if __name__ == "__main__":
    # Run the prediction
    predictions = predict_2035_values()
    
    # Create visualization
    data_2015 = [0.333507228, 0.019714456, 1.000521684, 1.334028912, 1.667536139]
    data_2025 = [0.109658329, 0.219316658, 0.328974974, 0.438633299, 0.548291624]
    
    create_ascii_visualization(data_2015, data_2025, predictions)
    
    # Generate final report
    generate_summary_report()