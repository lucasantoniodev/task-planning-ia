python -m venv venv                  

.\python-ia-linear-regression\Scripts\Activate.ps1 <- veja qual a extensão para seu terminal

pip install fastapi uvicorn scikit-learn pandas numpy 

para rodar a api na pasta src: uvicorn app:app --host 0.0.0.0 --port 8000     