# Narupa cloud simulation inputs

Simulation inputs for Narupa in the cloud.

All the input files in the repository *must* appear in `manifest.txt` to be
accounted for by the cloud server.

## How to update the manifest

### On Linux

```bash
ls *.xml > manifest.txt
```

### On Windows

```powershell
Get-ChildItem -Path . -Name | Select-String ".xml" | % { $_.Line } | Set-Content -Encoding utf8 manifest.txt
```

The `% { $_.Line }` avoids unwanted empty lines to be added to the file.
See [this stackoverflow answer](https://stackoverflow.com/a/48060726/2799884)
to read more about the issue.