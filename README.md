# Vim & Neovim Workshop

Welcome to the Neovim workshop! This workshop will help you get started with Neovim, a hyperextensible Vim-based text editor that's focused on extensibility and usability.

# Prerequisites

For comprehensive installation instructions for your platform, please refer to the official [Neovim installation guide](https://github.com/neovim/neovim/blob/master/INSTALL.md).

**Important Note**: This workshop requires Neovim version 0.10.0 or higher. You can check your current version by running:
```bash
nvim --version
```

### On Linux
**Warning**: Using `sudo apt-get install neovim` might install an outdated version that won't work for this workshop. Instead, please follow the installation instructions for pre-built archives in the [official installation guide](https://github.com/neovim/neovim/blob/master/INSTALL.md#pre-built-archives-2).

### On Windows
While Neovim can run on Windows PowerShell, we strongly recommend using Windows Subsystem for Linux (WSL) instead. WSL provides a more native Unix-like environment which works better with Neovim and its ecosystem. You can [install WSL following Microsoft's guide](https://learn.microsoft.com/en-us/windows/wsl/install).

### On macOS

Find installation instructions here: https://github.com/neovim/neovim/blob/master/INSTALL.md#macos--os-x

## Installing languages

We will be trying out Rust and/or Python. You will need at least one of them installed.

### Installing Rust

https://www.rust-lang.org/tools/install

**Linux/macOS**:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
After installation, restart your terminal or run:
```bash
source "$HOME/.cargo/env"
```

**Windows (Using WSL)**:
- Follow the Linux instructions above within WSL

**Windows (PowerShell)**:
1. Download and run rustup-init.exe from https://rustup.rs/
2. Follow the on-screen instructions

Verify installation:
```bash
rustc --version
cargo --version
```

### Installing Python3

**Linux**:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora
sudo dnf install python3 python3-pip

# Arch Linux
sudo pacman -S python python-pip
```

**macOS**:
1. Using Homebrew:
```bash
brew install python3
```
2. Or download the installer from [Python's official website](https://www.python.org/downloads/macos/)

**Windows**:
1. **WSL (Recommended)**:
   - Follow the Linux instructions above within WSL

2. **PowerShell**:
   - Download and run the installer from [Python's official website](https://www.python.org/downloads/windows/)
   - Make sure to check "Add Python to PATH" during installation

Verify Python installation:
```bash
python3 --version
pip3 --version
```

After installing Python, install Neovim's Python provider:
```bash
pip3 install pynvim
```

# Vim Motions

## Exercise

Hop into `vim_motions.py` and start following the instructions.

```bash
nvim vim_motions.py
```


## Vim Motions Cheat Sheet
For a comprehensive overview of Vim motions, check out this [Vim Motion Cheat Sheet](https://vim.rtorr.com/).

# Configure Neovim

This step we will do together.

## Install LazyVim

Instructions from [LazyVim's official website](https://www.lazyvim.org/installation)

Make a backup of your current Neovim files:

```bash
# required
mv ~/.config/nvim{,.bak}

# optional but recommended
mv ~/.local/share/nvim{,.bak}
mv ~/.local/state/nvim{,.bak}
mv ~/.cache/nvim{,.bak}
```

Clone the starter

```bash
git clone https://github.com/LazyVim/starter ~/.config/nvim
```

Remove the .git folder, so you can add it to your own repo later

```bash
rm -rf ~/.config/nvim/.git
```

Start Neovim (might need to start and stop it a couple of times)!

```bash
nvim
```

## Configure Neovim

```bash
cp -r lua/* ~/.config/nvim/lua/
```
