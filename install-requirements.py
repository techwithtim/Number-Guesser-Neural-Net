import subprocess
import sys
import get_pip
import os
import importlib

file = open("requirements.txt", "r")
file_lines = file.readlines()
required = [line.strip().lower() for line in file_lines]
file.close()

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

for package in required:
  try:
      print("[IMPORT] Trying to import", package)
      __import__(package)
  except:
      print("[EXCEPTION]", package, "not installed")

      try:
          print("[LOG] Trying to install", package, "via pip")
          import pip
          install(package)
          print("[LOG]", package, "has been installed")
      except:
          print("[EXCEPTION] Pip not installed on system")
          print("[LOG] Trying to install pip")
          get_pip.main()
          print("[LOG] Pip has been installed")
          try:
              print("[LOG] Trying to install", package)
              import pip
              install(package)
              print("[LOG]", package, "has been installed")
          except:
              print("[ERROR 1]", package, "could not be installed")

      __import__(package)
    
