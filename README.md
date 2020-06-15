# Narupa cloud simulation inputs

Simulation inputs for Narupa in the cloud.

Simulations are described by a simulation input file and a set of metadata. The metadata file follows the following format:

```json
{
    "name": "neuraminidase-ase",
    "description": "Lorem ipsum dolor sit amet.",
    "runner": "ase",
    "simulation": "neuraminidase.xml"
}
```

The `runner` field can be "ase" for the ASE-based runner, or "omm" for the OpenMM one. If an simulation is compatible with more than one runner, then there can be more than one metadata file for that system.

All the metadata files in the repository *must* appear in `manifest.txt` to be
accounted for by the cloud server.

## How to update the manifest

### On Linux

```bash
ls *.json > manifest.txt
```

### On Windows

```powershell
Get-ChildItem -Path . -Name | Select-String ".json" | % { $_.Line } | Set-Content -Encoding utf8 manifest.txt
```

The `% { $_.Line }` avoids unwanted empty lines to be added to the file.
See [this stackoverflow answer](https://stackoverflow.com/a/48060726/2799884)
to read more about the issue.