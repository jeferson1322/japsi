# Run this script from PowerShell to install reportlab (if necessário) and generate the PDFs
# Usage: Open PowerShell, navigate to this folder and run: .\run_generate_pdfs.ps1

Set-Location -Path "$PSScriptRoot"

if (Get-Command py -ErrorAction SilentlyContinue) {
    py -m pip install --user reportlab
    py generate_pdfs.py
    exit $LASTEXITCODE
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
    python -m pip install --user reportlab
    python generate_pdfs.py
    exit $LASTEXITCODE
} else {
    Write-Host "Python não encontrado no PATH. Baixe e instale Python em https://www.python.org/downloads/windows e marque 'Add Python to PATH'."
    Write-Host "Depois execute este script novamente: .\run_generate_pdfs.ps1"
    exit 1
}