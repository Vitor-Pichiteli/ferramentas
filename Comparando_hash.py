# Creating Def to create hash, save and read to compare.

import hashlib

def gerar_hash(arquivo):
    sha256 = hashlib.sha256()
    with open(arquivo, "rb") as f:
        while chunk := f.read(4096):  # lê de 4k em 4k
            sha256.update(chunk)
    return sha256.hexdigest()

def salvar_hash(hash_gerado, caminho_hash="hash_original.txt"):
    with open(caminho_hash, "w") as f:
        f.write(hash_gerado)

def verificar_integridade(arquivo, caminho_hash="hash_original.txt"):
    hash_atual = gerar_hash(arquivo)
    with open(caminho_hash, "r") as f:
        hash_original = f.read().strip()
    if hash_atual == hash_original:
        print("✅ O arquivo está íntegro.")
    else:
        print("❌ O arquivo foi alterado!")

# starting

if __name__ == "__main__":
    # creating a hash of the file (the name was created in the "keylogger" )
    hash_inicial = gerar_hash("keyfile.txt")
    salvar_hash(hash_inicial)

    # checking the integrity 
    verificar_integridade("keyfile.txt")
