# Python and Jupyter Setup

This guide helps you install Python, set up VS Code, and run Jupyter notebooks on Windows, macOS, or Linux.

## What You Need

- Python 3.11
- VS Code
- VS Code extensions for Python and Jupyter
- A terminal:
  - Windows: PowerShell
  - macOS: Terminal
  - Linux: Terminal

## 1. Install Python

### Windows

1. Download Python from <https://www.python.org/downloads/>.
2. Run the installer.
3. Important: tick **Add python.exe to PATH** before clicking install.
4. Open PowerShell and check:

```powershell
python --version
pip --version
```

If `python` does not work, try:

```powershell
py --version
```

### macOS

The simplest option is the official installer:

1. Download Python from <https://www.python.org/downloads/>.
2. Run the installer.
3. Open Terminal and check:

```bash
python3 --version
pip3 --version
```

### Linux

Python is often already installed. Check first:

```bash
python3 --version
pip3 --version
```

If Python or pip is missing, install them with your package manager.

Ubuntu or Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Fedora:

```bash
sudo dnf install python3 python3-pip
```

### Optional: Using pyenv

Some users may already use `pyenv` to manage Python versions.

`pyenv` is useful when you need more than one Python version on the same machine. For example, one project might need Python 3.10 and another might need Python 3.12.

With `pyenv`, you can install multiple Python versions and choose the version for each project:

```bash
pyenv versions
pyenv install 3.11.8
pyenv local 3.11.8
python --version
```

Use `pyenv versions` to see which Python versions are currently installed through `pyenv`.

This creates a `.python-version` file in the project folder so your terminal uses the selected Python version when you are working in that project.

## 2. Install VS Code

Download and install VS Code from <https://code.visualstudio.com/>.

Then open VS Code and install these extensions:

- Python
- Jupyter

You can find them from the Extensions panel in VS Code.

## 3. Open This Project

Open VS Code, then choose:

```text
File > Open Folder
```

Select this project folder.

You can also open the folder from a terminal:

```bash
code .
```

If `code .` does not work, just use **File > Open Folder** in VS Code.

## 4. Create a Virtual Environment

A virtual environment keeps this project's Python packages separate from the rest of your machine.

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

If you use the Python launcher:

```powershell
py -m venv venv
venv\Scripts\activate
```

### macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

When the environment is active, your terminal prompt usually starts with `(venv)`.

## 5. Install Jupyter

With the virtual environment active, run:

### Windows

```powershell
python -m pip install --upgrade pip
python -m pip install notebook ipykernel
```

### macOS and Linux

```bash
python3 -m pip install --upgrade pip
python3 -m pip install notebook ipykernel
```

If this project has a `requirements.txt` file, install it too:

```bash
pip install -r requirements.txt
```

## 6. Run Jupyter Notebooks in VS Code

1. Open a `.ipynb` notebook file in VS Code.
2. Click **Select Kernel** in the top-right corner.
3. Choose the Python environment named `venv`, or the interpreter from this project folder.
4. Click a cell and press the run button.

If VS Code asks to install extra packages, allow it.

## 7. Run Jupyter Notebooks in the Browser

You can also run notebooks in your web browser.

First, make sure your virtual environment is active.

Then run:

```bash
jupyter notebook
```

Your browser should open automatically.

If it does not, copy the URL from the terminal and paste it into your browser.

To stop Jupyter, go back to the terminal and press:

```text
Ctrl + C
```

## Common Problems

### `python` is not found

On Windows, try:

```powershell
py --version
```

On macOS or Linux, try:

```bash
python3 --version
```

### `pip` is not found

Use Python to run pip directly:

```bash
python -m pip --version
```

Or on macOS and Linux:

```bash
python3 -m pip --version
```

### VS Code cannot find the environment

In VS Code:

1. Open the Command Palette:
   - Windows/Linux: `Ctrl + Shift + P`
   - macOS: `Cmd + Shift + P`
2. Search for `Python: Select Interpreter`.
3. Choose the interpreter inside the `venv` folder.

## Quick Start

After Python and VS Code are installed, the usual setup is:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install notebook ipykernel
jupyter notebook
```

### macOS and Linux

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install notebook ipykernel
jupyter notebook
```
