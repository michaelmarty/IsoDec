from pathlib import Path

import numpy as np
import pytest

from isodec import IsoDecConfig, IsoDecWrapper, __version__
from isodec.c_interface import default_dll_path, example


def test_version_and_native_library_are_packaged():
    assert __version__ == "2.0.0"
    assert Path(default_dll_path).is_file()


def test_default_configuration_is_standalone_and_valid():
    config = IsoDecConfig()
    assert config.phaseres == 8
    assert config.minpeaks == 3
    assert config.adductmass == pytest.approx(1.007276467)
    assert config.mzwindowlb < 0 < config.mzwindowub


def test_native_example_charge_and_deconvolution():
    wrapper = IsoDecWrapper()
    assert wrapper.predict_charge(example) == 11

    peaks = wrapper.process_spectrum(example)
    assert [peak.z for peak in peaks] == [11, 5]
    np.testing.assert_allclose(
        [peak.monoiso for peak in peaks],
        [6250.5923, 2832.5012],
        rtol=0,
        atol=0.02,
    )
    assert all(peak.matchedintensity > 0 for peak in peaks)
