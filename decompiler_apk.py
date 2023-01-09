import os
import subprocess
import pkg_resources
import pyfiglet

nome = ("Nome: Romildo (thuf)    Site: helptecinfo.com")

print("")
print("")
print("======================================")
banner = pyfiglet.figlet_format("Decompiler APK")
print(banner)
print(nome)
print("======================================")
print("")

# Solicitar o caminho do arquivo .apk ao usuário
apk_path = input("Insira o caminho do arquivo .apk: (Ex: /downloads/whatsapp.apk): ")

# Verificar se o apktool está instalado
try:
    pkg_resources.require("apktool")
except pkg_resources.DistributionNotFound:
    subprocess.run(["pip", "install", "apktool"])

# Verificar se o openjdk-8-jre-headless está instalado
if not os.path.exists("/usr/bin/java"):
    subprocess.run(["apt-get", "install", "openjdk-8-jre-headless"])

# Descompilar o arquivo .apk
result = subprocess.run(["apktool", "d", apk_path])

# Verificar se o arquivo .apk foi decompilado com sucesso
if result.returncode == 0:
    print("O arquivo .apk foi decompilado com sucesso!")
else:
    print("Ocorreu um erro ao decompilar o arquivo .apk.")
