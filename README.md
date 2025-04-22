# Projeto - Aplicação Web Fullstack com Python e Django  

## Configuração do Ambiente

### Criação do ambiente virtual:  

**Linux**  
```bash
python3 -m venv venv
```
**Windows**
```bash
python -m venv venv
```

## Ativação do ambiente:

**Linux**
```bash
source venv/bin/activate
```
**Windows**
```bash
venv\Scripts\Activate
```

### Solução para erro de permissão no Windows:
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
 
## Instalação e Configuração
```bash
pip install django  
pip install pillow
```

## Rodar a aplicação

### Preparar migrações
```bash
python manage.py makemigrations
```

### Aplicar migrações
```bash
python manage.py migrate
```

### Rodar servidor
```bash
python manage.py runserver
```
