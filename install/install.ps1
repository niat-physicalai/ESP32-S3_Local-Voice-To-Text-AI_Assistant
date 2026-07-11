Write-Host ""
Write-Host "============================================"
Write-Host " ESP32-S3 Local Voice AI Installer"
Write-Host "============================================"
Write-Host ""

# Check PowerShell Version
Write-Host "[1/5] Checking PowerShell..."

if ($PSVersionTable.PSVersion.Major -lt 5)
{
    Write-Host "PowerShell 5 or newer required."
    exit
}

Write-Host "PowerShell OK"

Write-Host ""
Write-Host "[2/5] Checking Python..."

$python = Get-Command python -ErrorAction SilentlyContinue

if ($python)
{
    python --version
}
else
{
    Write-Host ""
    Write-Host "Python not found."
    Write-Host "Installing Python..."

    winget install Python.Python.3.12

    Write-Host ""
    Write-Host "Restart installer after installation."
    exit
}

Write-Host ""
Write-Host "[3/5] Launching installer..."

python install/install.py