# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## What This Installer Does

The Equation Paradise CAD Setup installer performs the following actions:

1. **Downloads Miniconda** from `https://repo.anaconda.com/miniconda/`
2. **Installs Miniconda** to `%USERPROFILE%\miniconda3\`
3. **Creates a conda environment** named `pyocc`
4. **Installs pythonocc-core** from conda-forge
5. **Creates folders** at `%USERPROFILE%\EquationParadise\`

## What This Installer Does NOT Do

- ❌ Modify system files or registry
- ❌ Require administrator privileges
- ❌ Install system-wide software
- ❌ Collect or transmit any user data
- ❌ Run background services or daemons
- ❌ Connect to any servers other than Anaconda/conda-forge

## Verification

You can verify the installer contents by:

1. Renaming `EquationParadise_CAD_Setup.exe` to `.cab`
2. Extracting with any archive tool
3. Reviewing the PowerShell script inside

Or review the source scripts in this repository.

## Reporting a Vulnerability

If you discover a security vulnerability, please email security@equationparadise.com.

We will respond within 48 hours and work to address the issue promptly.
