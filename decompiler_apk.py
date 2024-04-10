import os
import subprocess
import pyfiglet

def is_tool_installed(name):
    """Verifica se uma ferramenta está instalada."""
    from shutil import which
    return which(name) is not None

nome = "Nome: Romildo (thuf)    Site: helptecinfo.com"

print("\n\n======================================")
banner = pyfiglet.figlet_format("Decompiler APK")
print(banner)
print(nome)
print("======================================\n")

apk_path = input("Insira o caminho do arquivo .apk: (Ex: /downloads/whatsapp.apk): ")

# Verificar se o apktool está instalado
if not is_tool_installed("apktool"):
    print("O apktool não está instalado. Por favor, instale-o seguindo as instruções em: https://ibotpeaches.github.io/Apktool/install/")
    exit(1)

# Verificar se o openjdk-8-jre-headless está instalado
java_version_output = subprocess.run(["java", "-version"], stderr=subprocess.PIPE, text=True)
if "openjdk version \"1.8" not in java_version_output.stderr:
    print("O openjdk-8-jre-headless não está instalado ou não é a versão padrão. Instale ou configure como padrão seguindo as instruções específicas do seu sistema operacional.")
    exit(1)

# Descompilar o arquivo .apk
result = subprocess.run(["apktool", "d", apk_path], capture_output=True, text=True)

# Verificar se o arquivo .apk foi decompilado com sucesso
if result.returncode == 0:
    print("O arquivo .apk foi decompilado com sucesso!")
else:
    print("Ocorreu um erro ao decompilar o arquivo .apk. Erro: " + result.stderr)

