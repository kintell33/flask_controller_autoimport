### primera forma para implementar el auto import de los modulos del package, pero no es recomendable usar funciones que son para el interprete

# import os
# for module in os.listdir(os.path.dirname(__file__)):
#     if module == '__init__.py' or module[-3:] != '.py':
#         continue
#     __import__("controller."+module[:-3], locals(), globals())
# del module

### segunda forma podria ser el __all__ que es un array de strings con los modulos a utilizar

# import os, glob

# modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
# __all__ = [os.path.basename(f)[:-3] for f in modules if not f.endswith("__init__.py")]

### otra manera bastante elegante es recorrer todos los .py del package y usar la libreria importlib que si es para esto
### se importan todos los modulos y agregamos el nombre del package concatenado al modulo

import os
import importlib

actual_package = os.path.dirname(__file__).replace(os.getcwd()+"/","")
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    importlib.import_module("{}.{}".format(actual_package, module[:-3]))
del module