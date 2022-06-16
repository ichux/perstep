## Perstep
Just to learn how to organise by Django Apps

```bash
mkdir -p apps/perstep && touch apps/__init__.py
python manage.py startapp perstep ./apps/perstep

OR

mkdir -p apps && touch apps/__init__.py
cd apps && django-admin startapp common && cd ..

# Then do the following

1. In settings.py "INSTALLED_APPS" add "apps.common.apps.CommonConfig" to it.

├── apps
│   ├── __init__.py
│   └── perstep
│       ├── apps.py

2. Change `name = 'apps.perstep'` in 'apps > perstep > apps.py' PerstepConfig
```