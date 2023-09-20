# Django local settings generator
made automatic `local_settings.py` file in your Django project 

## How to use
- First add `settings_build.py` file in root of project, Next to the `manage.py` file
- Then add main app and name of local_settings.py file name in `LOCAL_SETTINGS_PATH` attribute like this:

```python
class ProjectInit:
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, 'core/local_settings.py')
    
    # other code :)

```

- At the last run `settings_build.py` file
```bash
Akira@yuzai:~/Django-project$ python settings_build.py

```

## TODO

- [ ] make python library
