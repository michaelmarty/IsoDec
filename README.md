# IsoDec

IsoDec assigns charge states and deconvolves isotopically resolved mass
spectrometry data. Its native core uses [IsoGen](https://github.com/michaelmarty/IsoGen)
for peptide and RNA isotope distributions.

## Installation

Install a published wheel:

```shell
python -m pip install isodec
```

IsoDec supports Python 3.9 and newer on 64-bit Windows, Linux, and macOS.
Compatible wheels include the native IsoDec and IsoGen libraries. A source
build requires CMake 3.22.1 or newer, a C/C++ compiler, FFTW, and an initialized
IsoGen submodule:

```shell
git clone --recurse-submodules https://github.com/michaelmarty/IsoDec.git
python -m pip install ./IsoDec
```

## Python usage

```python
import numpy as np
from isodec import IsoDecRuntime

spectrum = np.loadtxt("spectrum.txt")
engine = IsoDecRuntime()
peaks = engine.batch_process_spectrum(spectrum, centroided=True)

for peak in peaks:
    print(peak.mz, peak.z, peak.monoiso, peak.matchedintensity)
```

TXT, DAT, CSV, and NPZ single-scan spectra are supported without UniDec. Raw
vendor files, mzML/mzXML, and I2MS import use UniDec's extensive importer stack:

```shell
python -m pip install "isodec[unidec]"
```

## Command line

```shell
isodec spectrum.txt --centroided -o assigned_peaks.tsv
python -m isodec --help
```

## Development

```shell
git submodule update --init --recursive
python -m pip install -e ".[test]"
python -m pytest
```

Documentation sources live in `docs/` and are built with MkDocs. Release and
wheel-building details are in [PUBLISHING.md](PUBLISHING.md).

## License and citation

IsoDec is released under the BSD 3-Clause License. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for IsoGen, FFTW, and Intel
runtime notices. When using IsoDec, please cite Pavek et al.,
“[A Fast Neural Network for Isotopic Charge State Assignment](https://doi.org/10.1021/jacs.5c03162),”
*J. Am. Chem. Soc.* **2025**, *147*, 21610–21620. Machine-readable metadata is
provided in [CITATION.cff](CITATION.cff).

## Change Log

### 2.0.1

Changes to improve performance.

Added bin folder with built files and changed install paths to there.

### 2.0.0

Developing the ability to assign charge state directly to profile data. Ongoing experimental features here.

Split into a standalone package with IsoGen as a submodule. IsoDec now has its own versioning and release cycle.

Added many tests and automated deployment generation.

### 1.0.0
- Initial release of IsoDec with IsoGen integration for isotopic charge state assignment and deconvolution of mass spectrometry data. Was released as part of the UniDec package.