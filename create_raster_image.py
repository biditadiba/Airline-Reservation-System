#!/usr/bin/env python3
"""
Generate a simple raster image representation of the 2035 predictions
"""

def create_pbm_image():
    """
    Create a simple PBM (Portable Bitmap) raster image showing the predictions
    """
    # Data
    data_2015 = [0.333507228, 0.019714456, 1.000521684, 1.334028912, 1.667536139]
    data_2025 = [0.109658329, 0.219316658, 0.328974974, 0.438633299, 0.548291624]
    predictions_2035 = [-0.114191, 0.418919, -0.342572, -0.456762, -0.570953]
    
    # Create a simple bitmap representation
    width = 300
    height = 200
    
    # Initialize bitmap (0 = black, 1 = white)
    bitmap = [[1 for _ in range(width)] for _ in range(height)]
    
    # Scale data to fit image
    max_val = max(max(data_2015), max(data_2025), max([p for p in predictions_2035 if p > 0]))
    min_val = min(min(data_2015), min(data_2025), min(predictions_2035))
    
    def scale_y(value):
        if max_val == min_val:
            return height // 2
        normalized = (value - min_val) / (max_val - min_val)
        return int(height - (normalized * (height - 20)) - 10)
    
    # Draw axes
    for x in range(width):
        bitmap[height - 20][x] = 0  # X-axis
    
    for y in range(height):
        bitmap[y][30] = 0  # Y-axis
    
    # Draw data points and lines for each series
    for i, (val_2015, val_2025, pred_2035) in enumerate(zip(data_2015, data_2025, predictions_2035)):
        # X positions for years
        x_2015 = 50
        x_2025 = 150
        x_2035 = 250
        
        # Y positions (scaled)
        y_2015 = scale_y(val_2015)
        y_2025 = scale_y(val_2025)
        y_2035 = scale_y(pred_2035)
        
        # Draw points (3x3 squares)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if 0 <= y_2015 + dy < height and 0 <= x_2015 + dx < width:
                    bitmap[y_2015 + dy][x_2015 + dx] = 0
                if 0 <= y_2025 + dy < height and 0 <= x_2025 + dx < width:
                    bitmap[y_2025 + dy][x_2025 + dx] = 0
                if 0 <= y_2035 + dy < height and 0 <= x_2035 + dx < width:
                    bitmap[y_2035 + dy][x_2035 + dx] = 0
        
        # Draw lines connecting the points
        # Line from 2015 to 2025
        for t in range(101):
            x = int(x_2015 + (x_2025 - x_2015) * t / 100)
            y = int(y_2015 + (y_2025 - y_2015) * t / 100)
            if 0 <= y < height and 0 <= x < width:
                bitmap[y][x] = 0
        
        # Dashed line from 2025 to 2035 (prediction)
        for t in range(0, 101, 5):  # Dashed line
            x = int(x_2025 + (x_2035 - x_2025) * t / 100)
            y = int(y_2025 + (y_2035 - y_2025) * t / 100)
            if 0 <= y < height and 0 <= x < width:
                bitmap[y][x] = 0
    
    # Add year labels (simple text representation)
    # 2015
    year_patterns = {
        '2': [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]],
        '0': [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]],
        '1': [[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,1]],
        '5': [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]],
        '3': [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
    }
    
    # Write PBM file
    with open('/workspace/predictions_2035.pbm', 'w') as f:
        f.write('P1\n')
        f.write(f'{width} {height}\n')
        for row in bitmap:
            f.write(' '.join(map(str, row)) + '\n')
    
    print("Raster image saved as: predictions_2035.pbm")
    return bitmap

def create_ascii_raster():
    """
    Create ASCII art raster representation
    """
    print("\n" + "=" * 80)
    print("RASTER IMAGE - 2035 PREDICTIONS VISUALIZATION")
    print("=" * 80)
    
    data_2015 = [0.333507228, 0.019714456, 1.000521684, 1.334028912, 1.667536139]
    data_2025 = [0.109658329, 0.219316658, 0.328974974, 0.438633299, 0.548291624]
    predictions_2035 = [-0.114191, 0.418919, -0.342572, -0.456762, -0.570953]
    
    # Create a simple ASCII chart
    width = 60
    height = 20
    
    chart = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Scale values
    all_values = data_2015 + data_2025 + predictions_2035
    max_val = max(all_values)
    min_val = min(all_values)
    
    def scale_value(val, max_height):
        if max_val == min_val:
            return max_height // 2
        normalized = (val - min_val) / (max_val - min_val)
        return int((1 - normalized) * max_height)
    
    # Plot each series
    symbols = ['1', '2', '3', '4', '5']
    
    for i, (val_2015, val_2025, pred_2035) in enumerate(zip(data_2015, data_2025, predictions_2035)):
        symbol = symbols[i]
        
        # Positions
        x_2015 = 10
        x_2025 = 30
        x_2035 = 50
        
        y_2015 = scale_value(val_2015, height - 1)
        y_2025 = scale_value(val_2025, height - 1)
        y_2035 = scale_value(pred_2035, height - 1)
        
        # Place symbols
        if 0 <= y_2015 < height:
            chart[y_2015][x_2015] = symbol
        if 0 <= y_2025 < height:
            chart[y_2025][x_2025] = symbol
        if 0 <= y_2035 < height:
            chart[y_2035][x_2035] = '*'  # Prediction marker
        
        # Draw connecting lines
        for t in range(21):
            x = x_2015 + (x_2025 - x_2015) * t // 20
            y = y_2015 + (y_2025 - y_2015) * t // 20
            if 0 <= y < height and 0 <= x < width and chart[y][x] == ' ':
                chart[y][x] = '-'
        
        # Dashed line for prediction
        for t in range(0, 21, 2):
            x = x_2025 + (x_2035 - x_2025) * t // 20
            y = y_2025 + (y_2035 - y_2025) * t // 20
            if 0 <= y < height and 0 <= x < width and chart[y][x] == ' ':
                chart[y][x] = '.'
    
    # Print the chart
    print("     2015    2025    2035(PRED)")
    print("     |       |       |")
    for row in chart:
        print(''.join(row))
    
    print("\nLEGEND:")
    print("1,2,3,4,5 = Data series")
    print("*         = 2035 predictions")
    print("-         = Historical trend")
    print(".         = Predicted trend")

if __name__ == "__main__":
    create_ascii_raster()
    create_pbm_image()