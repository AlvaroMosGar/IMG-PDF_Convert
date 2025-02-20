import subprocess
import sys


def install_dependencies():
    """Instala las bibliotecas necesarias con pip"""
    print("📦 Instalando dependencias: Pillow y PyPDF2...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pillow", "pypdf2"], check=True)
    print("✅ Dependencias instaladas correctamente.")

def main():
    install_dependencies()

if __name__ == "__main__":
    main()
