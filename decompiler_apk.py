import subprocess
import pyfiglet
import re
from shutil import which
import os
import sys

def is_tool_installed(name):
    """Verifica se uma ferramenta está instalada."""
    return which(name) is not None

def verificar_dependencias():
    """Verifica dependências essenciais (apktool e Java 8)."""
    if not is_tool_installed("apktool"):
        print("Erro: apktool não está instalado. Instale-o em: https://ibotpeaches.github.io/Apktool/install/")
        sys.exit(1)

    try:
        java_version_output = subprocess.run(
            ["java", "-version"], stderr=subprocess.PIPE, text=True
        )
        if not re.search(r'"1\.8\..*"', java_version_output.stderr):
            print("Erro: Java 8 não está configurado como padrão. Configure e tente novamente.")
            sys.exit(1)
    except FileNotFoundError:
        print("Erro: Java não está instalado. Instale o Java 8.")
        sys.exit(1)

def descompilar_apk(apk_path):
    """Descompila o arquivo APK fornecido."""
    try:
        output_dir = os.path.splitext(os.path.basename(apk_path))[0]
        print("Processando... Isso pode levar algum tempo para APKs maiores.")
        result = subprocess.run(["apktool", "d", apk_path, "-o", output_dir], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Sucesso! O APK foi descompilado em: {os.path.abspath(output_dir)}")
        else:
            print(f"Erro ao descompilar o APK: {result.stderr}")
    except Exception as e:
        print(f"Erro ao executar o apktool: {e}")

def main():
    # Banner
    print("\n\n======================================")
    banner = pyfiglet.figlet_format("Decompiler APK")
    print(banner)
    print("Nome: Romildo (thuf)    Site: helptecinfo.com")
    print("======================================\n")

    # Entrada do Usuário
    apk_path = input("Insira o caminho do arquivo .apk (Ex: /downloads/whatsapp.apk): ").strip()

    # Validações
    if not os.path.exists(apk_path):
        print("Erro: O arquivo .apk especificado não existe. Verifique o caminho e tente novamente.")
        sys.exit(1)

    if not apk_path.endswith(".apk"):
        print("Erro: O arquivo especificado não é um APK válido. Forneça um arquivo com extensão '.apk'.")
        sys.exit(1)

    # Normalização do caminho do arquivo
    apk_path = os.path.abspath(apk_path)

    # Verificar dependências e descompilar
    verificar_dependencias()
    descompilar_apk(apk_path)

if __name__ == "__main__":
    main()
