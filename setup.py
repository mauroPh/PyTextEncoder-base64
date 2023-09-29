import sys
from cx_Freeze import setup, Executable

# Dependências do projeto
build_exe_options = {"packages": ["base64"], "excludes": []}

# Configuração do executável
setup(name="PyTextEncoder",
      version="0.1",
      description="Conversor Base64",
      options={"build_exe": build_exe_options},
      executables=[Executable("PyTextEncoder.py", base=None)])