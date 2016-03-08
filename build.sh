#!/bin/sh
function requirements_installed() {
  echo "Checking to see if build environment is sane."

  for c in "$@"; do
    if ! command -v "${c}" >/dev/null 2>&1 ; then
      echo "${c} is required but not installed."
      return 1
    fi
  done

  echo "Build environment is sane."
}

function python_installed() {
 if ! [ -d "${PYENV_ROOT}/versions/3.5.1" ]; then
   echo "Python is not installed. Installing python."
   pyenv install 
 else
   echo "Python is installed."
   return 0
 fi 
}

function install_deps() {
  pip3 install -r requirements.txt
}

function run_model() {
  echo "Preparing data for modeling."
  ./src/main/python/com/woodrad/lanl_data/prepare.py
  echo "Running model"
  sbt run
}

if requirements_installed javac pyenv sbt; then
  if python_installed; then
    install_deps
    run_model
  fi
else
  exit 1
fi
