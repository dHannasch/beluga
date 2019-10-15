import pytest
import subprocess
import os

AscentVehicles = [r'BFR', r'GoddardRocket', r'Titan-II-SSTO']
AtmosphericFlight = [r'HangGlider', r'HypersonicNose', r'SpaceShuttle']
Classic = [r'Brachistochrone', r'BrysonDenham', r'Moonlander', r'ZermelosProblem']
ElectricityandMagnetism = [r'OneLoopCircuit']
Oscillators = [r'FinancialOscillator', r'MallsOscillator', r'Rayleigh']


@pytest.mark.parametrize("file", AscentVehicles)
def test_AscentVehicles(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AscentVehicles/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


def test_AstrodynamicsHT():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/HighThrust.py')
    assert subprocess.call(['python', path]) == 0


def test_AstrodynamicsLT():
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Astrodynamics/OrbitRaising/LowThrust.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", AtmosphericFlight)
def test_AtmosphericFlight(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/AtmosphericFlight/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Classic)
def test_Classic(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Classic/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", ElectricityandMagnetism)
def test_ElectricityandMagnetism(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/ElectricityandMagnetism/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0


@pytest.mark.parametrize("file", Oscillators)
def test_Oscillators(file):
    fpath = os.path.dirname(__file__)
    path = os.path.realpath(fpath + r'/../../examples/Oscillators/' + file + '/' + file + '.py')
    assert subprocess.call(['python', path]) == 0