import cx_Freeze

# Definindo o executável
executables = [
    cx_Freeze.Executable(
        script="main.py",  # Caminho para o seu script principal
        icon="recursos/icone.ico",  # Caminho para o ícone do seu jogo
        target_name="speedrace.exe"  # Nome do executável gerado
    )
]

# Configuração do cx_Freeze
cx_Freeze.setup(
    name="Speed Race",
    description="Jogo de Corrida Maluca",  # Descrição do jogo
    options={
        "build_exe": {
            "packages": ["pygame"],  # Inclui o pygame, que é uma dependência externa
            "include_files": ["recursos", "README.md"]  # Inclui o README.md da pasta principal
        }
    },
    executables=executables
