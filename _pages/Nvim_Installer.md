---
layout: page
title: Nvim Installer
permalink: /pages/Nvim_Installer/
date: 2021-07-16
---

# How to install Nvim & Nvchad

## Dependencies:

 - Git/GitHub
 - Powershell > PowerShell 7.4.7

## 1. Install nvim lst version.

- Go to https://github.com/neovim/neovim/releases

    ```txt
    Download nvim-win64.zip
    Extract the zip
    Run nvim.exe on your CLI of choiceDownload nvim-win64.zip
    Extract the zip
    Run nvim.exe on your CLI of choice
    ```
    - Add the nvim.exe to the system variables.

## 2. Install NvChad lst version:

- Go to desired folder installation: c:/MyInstallations/

    ```ps1
    git clone https://github.com/NvChad/NvChad "$env:LOCALAPPDATA\nvim" --depth 1
    ```

- NvChad will automatically install all plugins on first launch. Give it a moment to finish bootstrapping.


