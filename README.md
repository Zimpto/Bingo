# 🎱 Bingo

**Bingo** is a Python-based tool that generates custom Bingo sheets using a unique format of **five 3×9 rectangles** instead of the traditional six. It's perfect for custom games, classroom activities, or just having fun with a twist on the classic Bingo layout.

## 📌 Features

- 📄 Generates **any number** of Bingo sheets by passing the desired count as an argument.
- 🧩 Each sheet contains **five 3×9 rectangles**, differing from the standard six-grid layout.
- 🖼️ Outputs the Bingo sheets as images, ready for printing or sharing.

## 🛠️ How It Works

Simply call the main function in your script and specify how many Bingo sheets you'd like to generate.

```python
from Bingo import BingoSheet

# Generate 10 Bingo sheets
BingoSheet(10)
```

## 🧾 Requirements
Make sure you have the following Python libraries installed:

- `Pillow` (for image creation)
- `Numpy` (for array handling)

You can install Pillow using pip:

```bash
pip install Pillow
```
You can install Numpy using pip:

```bash
pip install Numpy
```
## ✅ To-Do

- [ ] Stabilize the free spaces
- [ ] Add customization options for colors and fonts  
- [ ] Support exporting to PDF format