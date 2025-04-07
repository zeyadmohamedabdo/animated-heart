import tkinter as tk
import random
import math
from PIL import Image, ImageDraw, ImageTk

def create_heart_image(color, angle):
    size = (300, 300)
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    def heart_function(t):
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        return x * 8, -y * 8  # Scale and invert y-axis for correct orientation
    
    points = [heart_function(t) for t in [i * 0.1 for i in range(int(math.pi * 20))]]
    
    # Apply rotation for 3D oscillation effect
    rotated_points = []
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    for x, y in points:
        x_rot = cos_a * x - sin_a * y
        y_rot = sin_a * x + cos_a * y
        rotated_points.append((150 + x_rot, 150 + y_rot))
    
    # Create a gradient effect for a 3D look
    for i in range(10):
        alpha = int(255 * (i / 10))
        shade = (max(0, 255 - i * 20), 50 + i * 10, 50 + i * 10, alpha)  # Softer shading
        offset = i // 2  # Smooth layering effect
        draw.polygon([(x + offset, y - offset) for x, y in rotated_points], fill=shade, outline=None)
    
    draw.polygon(rotated_points, fill=color, outline="black")
    
    return image

def animate_heart():
    global tk_heart_img, angle
    angle += 0.1  # Increment angle for oscillation
    color = random.choice(["red"])
    heart_img = create_heart_image(color, math.sin(angle) * 0.3)  # Apply oscillation
    tk_heart_img = ImageTk.PhotoImage(heart_img)
    canvas.itemconfig(heart_image, image=tk_heart_img)
    root.after(5, animate_heart)

def main():
    global root, canvas, heart_image, tk_heart_img, angle
    root = tk.Tk()
    root.title("Heart GUI")
    root.geometry("320x320")
    
    angle = 0.0  # Initialize oscillation angle
    
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()
    
    heart_img = create_heart_image("red", angle)
    tk_heart_img = ImageTk.PhotoImage(heart_img)
    heart_image = canvas.create_image(150, 150, image=tk_heart_img)
    
    # Add text in the middle of the heart
    canvas.create_text(150, 140, text="",font=("Arial", 16, "bold"), fill="white")
    
    root.after(200, animate_heart)
    root.mainloop()

if __name__ == "__main__":
    main()

