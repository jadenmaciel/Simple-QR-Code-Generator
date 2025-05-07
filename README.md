# Python QR Code Generator

This Python script is a simple yet effective QR code generator. Provide it with any text or URL, and it will generate a corresponding QR code image, saving it as a PNG file.

## Problem Statement/Motivation

QR codes have become ubiquitous for quickly sharing information, from website links and contact details to Wi-Fi passwords and event tickets. This project provides a straightforward way to generate these useful codes programmatically using Python. It eliminates the need for online services or complex software for basic QR code creation.

## Features Implemented

* Generates QR codes from text or URLs.
* Allows customization of error correction level.
* Offers control over the size of the individual boxes within the QR code.
* Enables setting the border size around the QR code.
* Saves the generated QR code as a PNG image file.
* Provides options for setting the fill and background colors of the QR code.

## Technologies Used

* **Python:** The primary programming language used.
* **qrcode:** A Python library for generating QR codes.

## Setup and Installation Instructions

1.  **Prerequisites:** Ensure you have Python installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2.  **Install the `qrcode` library:** Open your terminal or command prompt and run the following command:
    ```bash
    pip install qrcode
    ```
3.  **Save the code:** Copy the provided Python code and save it as a `.py` file (e.g., `qr_generator.py`).

## Usage/Examples

1.  **Basic Usage:** To generate a QR code for a website, simply run the script. The provided code is already set up to generate a QR code for "[https://www.neuralnine.com/books](https://www.neuralnine.com/books)" and save it as "advanced.png".
    ```bash
    python qr_generator.py
    ```
    This will create an image file named `advanced.png` in the same directory as the script.

2.  **Modifying the Data:** To generate a QR code for different content, change the string passed to the `qr.add_data()` method. For example, to create a QR code for the text "Hello World!":
    ```python
    import qrcode

    qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=50,
                        border=10)

    qr.add_data("Hello World!")
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("hello_world_qr.png")
    ```

3.  **Customizing Parameters:** You can adjust various parameters when creating the `QRCode` object:
    * `version`: Controls the complexity of the QR code (integer from 1 to 40).
    * `error_correction`: Sets the error correction level (`ERROR_CORRECT_L`, `ERROR_CORRECT_M`, `ERROR_CORRECT_Q`, `ERROR_CORRECT_H`). Higher levels provide more redundancy but result in larger QR codes.
    * `box_size`: Controls the size of each box (pixel) in the QR code.
    * `border`: Controls the width of the quiet border around the QR code.
    * `fill_color`: Sets the color of the QR code modules.
    * `back_color`: Sets the background color of the QR code.

## Live Demo Link

This is a script for local use and does not have a live demo link.

## Challenges & Learnings

One challenge encountered was understanding the different error correction levels and their impact on the QR code's size and resilience. Learning how to choose the appropriate level based on the intended use case was insightful. Additionally, exploring the various customization options offered by the `qrcode` library broadened the understanding of QR code generation.
```
