
import cx_Freeze

executables = [
    cx_Freeze.Executable(script= 'main.py', icon='recursos/icone.ico')
]
cx_Freeze.setup(
    name = 'Corrida Maluca',
    options= {
        'build_exe':{
            'packages':['pygame'],
            'include_files':['recursos', 'README.md']
        }
    }, executables = executables    
)

