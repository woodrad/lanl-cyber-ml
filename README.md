# lanl-cyber
Let's use LANL Cyber-Security data to detect fishy workstation processes.

# Data
Source data taken from A. D. Kent, “Comprehensive, Multi-Source Cybersecurity Events,” Los Alamos National Laboratory, http://dx.doi.org/10.17021/1179829, 2015. Data dictionary for enriched data can be found [here](https://github.com/woodrad/lanl-cyber/blob/master/DATA_DICTIONARY.csv). Enriched data generated using the Scala code found in this project.

# Hardware and OS
- Intel(R) Core(TM) i3-5010U CPU @ 2.10GHz with 16GB of RAM and 1TB of pure, spinning rust.
- Fedora Core 23 GNU/Linux with a 4.3.5 kernel.

# Reproducing the development environment
1. Clone this repository locally with `git clone git@github.com:woodrad/lanl-cyber.git`.
2. If you have a copy of [LANL's Cyber-Security data](http://csr.lanl.gov/data/cyber1) already, copy or link the tarballs to `data/`.
3. `build.sh` will check your environment, download data if you do not have it, resolve dependencies, and build the model.
3. If you are missing `pyenv`, [install `pyenv`](https://github.com/yyuu/pyenv#installation).
4. If you are missing `javac`, install Oracle or OpenJDK.
5. If you are missing `sbt`, [install `sbt`](http://www.scala-sbt.org/0.13/docs/Setup.html).
6. `build.sh` will now download the data needed with `./src/main/python/download.py`. This will take some time.
7. After you have the data, `build.sh` will run the model.

# About the model
Documentation for this model is in [`MODEL.md`](https://github.com/woodrad/lanl-cyber/blob/master/MODEL.md).

# License
GPLv3 as in respects your GNU/Freedom. Can't tivoize this.

![Dreamy gif of RMS](https://media.giphy.com/media/XXVYCLbrhlr5m/giphy.gif)