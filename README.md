# Aliaser: Audio Processing Tool

Aliaser is a Python-based tool designed to introduce aliasing into your sound for a creative effect. It allows users to downsample stereo WAV files to a desired sample rate and optionally upsample them back to the original rate. The tool offers various interpolation methods for upsampling, including simple repeat, linear, and cubic interpolation. Additionally, it can be used as a raw down sampler. As of version 1, Aliaser specifically requires stereo 16-bit WAV files.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Licensing Agreement](#licensing-agreement)
- [Third-Party Libraries and Licenses](#third-party-libraries-and-licenses)

## Requirements

- Python
- Stereo 16-bit WAV files

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository.
3. Install the required libraries using pip:
   ```
   pip install numpy scipy
   ```

## Usage

Run the Aliaser script using Python:
```
python Aliaser.py
```
Follow the on-screen prompts to select the input WAV file, specify the desired sample rate, and choose whether to upsample the audio back to its original rate.

## Licensing Agreement

### 1. License

MIT License

Copyright (c) 2023 Hikari

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Third-Party Libraries and Licenses

In the development of Aliaser, the following third-party libraries have been utilized:

1. **numpy**
   - *Description*: A library for numerical computing in Python.
   - *License*: BSD 3-Clause License

2. **tkinter and its associated modules (filedialog, simpledialog, messagebox, ttk)**
   - *Description*: The standard Python interface to the Tk GUI toolkit and its associated modules providing various dialog boxes and themed widgets.
   - *License*: Python Software Foundation License

3. **scipy.interpolate**
   - *Description*: A module within `scipy` that provides functions and classes for interpolation.
   - *License*: BSD 3-Clause License

4. **sys**
   - *Description*: Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
   - *License*: Python Software Foundation License

5. **os**
   - *Description*: Provides a way of using operating system-dependent functionality like reading or writing to the file system.
   - *License*: Python Software Foundation License

Users are advised to review the respective licenses of these libraries to understand their terms and conditions. All rights and credits for these libraries belong to their respective authors and contributors. Aliaser acknowledges the use of these libraries and extends gratitude to the open-source community for their contributions.

---

Developed by Hikari.

---
