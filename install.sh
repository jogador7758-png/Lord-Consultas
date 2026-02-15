#!/bin/bash
# Script de instalação Lord Consultas para Termux

clear
echo "
╔════════════════════════════════════════╗
║     LORD CONSULTAS - INSTALADOR        ║
║     Desenvolvido para Termux           ║
╚════════════════════════════════════════╝
"

echo "[*] Atualizando pacotes..."
pkg update -y && pkg upgrade -y

echo "[*] Instalando Python..."
pkg install python -y

echo "[*] Instalando dependências..."
pip install -r requirements.txt

echo "[*] Dando permissão ao script..."
chmod +x lord_consultas.py

echo "
╔════════════════════════════════════════╗
║     ✓ INSTALAÇÃO CONCLUÍDA!            ║
╚════════════════════════════════════════╝

Para executar:
    python lord_consultas.py

Ou:
    ./lord_consultas.py
"

echo "[*] Criando atalho..."
echo "alias lord='python $(pwd)/lord_consultas.py'" >> ~/.bashrc
echo "[+] Atalho 'lord' criado! Reinicie o Termux ou execute: source ~/.bashrc"
