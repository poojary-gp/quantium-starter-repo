# Exit if any error occurs
$ErrorActionPreference = "Stop"

# Activate virtual environment (Windows path)
. .\venv\Scripts\Activate.ps1

# Run tests
pytest -q
if ($LASTEXITCODE -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Host "Some tests failed!"
    exit 1
}
