# PassCheck 🔐

![Screenshot](ScreenShot.jpg)

A simple yet powerful password strength checker made for Termux and Python.

## 🔧 Features

- ✅ Password strength analysis with detailed scoring
- 🔢 Score from 0 to 10 based on length, case, digits, and special characters
- ⚠️ Detection of common and leaked passwords with colored alerts
- 🔐 Strong password generator (future addition)
- 🌈 Colored output for quick readability
- 📝 Real-time password checking with instant advice

---

## 📚 Required Libraries

This tool requires Python 3 and the following Python packages installed via pip: colorama for colorful terminal output, requests to fetch leaked password data, and termcolor for additional colored text support. Install them all at once using the command:

```bash
pip install colorama requests termcolor
