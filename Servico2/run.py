import os
import sys

# Adiciona o diretório raiz ao PYTHONPATH
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_path)

from Servico2.src.main import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
