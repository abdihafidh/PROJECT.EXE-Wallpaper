#!/usr/bin/env python3
"""
PROJECT.EXE Wallpaper Generator
Generates a pixelated retro wallpaper with PROJECT.EXE overlay
"""

from PIL import Image, ImageDraw, ImageFont
import random

def generate_wallpaper(width=1920, height=1280, output_file="wallpaper.png"):
    """Generate the PROJECT.EXE wallpaper"""
    
    # Create base image with dark background
    img = Image.new('RGB', (width, height), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)
    
    # Create pixelated noise/static background
    pixel_size = 8
    for x in range(0, width, pixel_size):
        for y in range(0, height, pixel_size):
            # Random grayscale values for pixelated effect
            brightness = random.randint(15, 50)
            draw.rectangle([x, y, x + pixel_size, y + pixel_size], 
                          fill=(brightness, brightness, brightness))
    
    # Draw gradient-like effect with white dots
    for _ in range(150):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(2, 8)
        opacity = random.randint(30, 100)
        draw.ellipse([x, y, x + size, y + size], 
                    fill=(200, 200, 200))
    
    # Draw PROJECT.EXE window frame (retro style)
    window_x, window_y = 300, 200
    window_width, window_height = 800, 600
    
    # Window border (cyan/blue classic Windows color)
    border_color = (0, 170, 255)
    draw.rectangle([window_x, window_y, window_x + window_width, window_y + window_height], 
                   outline=border_color, width=3)
    
    # Window title bar
    title_bar_height = 25
    draw.rectangle([window_x, window_y, window_x + window_width, window_y + title_bar_height],
                   fill=border_color)
    
    # Title text
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()
    
    draw.text((window_x + 5, window_y + 3), "PROJECT.EXE", fill=(255, 255, 255), font=font)
    
    # Window close/minimize buttons (retro style)
    button_y = window_y + 3
    button_x = window_x + window_width - 60
    button_size = 18
    
    # Close button (red)
    draw.rectangle([button_x, button_y, button_x + button_size, button_y + button_size],
                   fill=(255, 0, 0))
    
    # Draw some pixelated "Adam" art inside the window
    content_y = window_y + title_bar_height + 20
    
    # Simple pixelated face representation
    face_x = window_x + window_width // 2 - 40
    face_y = content_y
    pixel = 10
    
    # Draw eyes
    draw.rectangle([face_x, face_y, face_x + pixel, face_y + pixel], fill=(255, 255, 0))
    draw.rectangle([face_x + pixel * 4, face_y, face_x + pixel * 5, face_y + pixel], fill=(255, 255, 0))
    
    # Draw smile
    for i in range(1, 4):
        draw.rectangle([face_x + pixel * i, face_y + pixel * 3, 
                       face_x + pixel * (i + 1), face_y + pixel * 4], fill=(255, 255, 0))
    
    # Add some random pixelated decorations
    for _ in range(20):
        px = random.randint(window_x + 20, window_x + window_width - 20)
        py = random.randint(content_y, window_y + window_height - 20)
        size = random.randint(3, 8)
        color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        draw.rectangle([px, py, px + size, py + size], fill=color)
    
    # Add PROJECT.EXE text at bottom right (watermark style)
    try:
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font_small = ImageFont.load_default()
    
    draw.text((width - 150, height - 30), "PROJECT.EXE", fill=(0, 170, 255), font=font_small)
    
    # Save the wallpaper
    img.save(output_file)
    print(f"Wallpaper generated: {output_file}")

if __name__ == "__main__":
    generate_wallpaper()