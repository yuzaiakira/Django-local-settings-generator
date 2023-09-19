from django.core.management.utils import get_random_secret_key

from pathlib import Path
import os


class ProjectInit:
    BASE_DIR = Path(__file__).resolve().parent
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, 'core/local_settings.py')

    def __init__(self):
        self._SECRET_KEY = self.generate_secret_key()

    def tasks(self):
        """call all task for making local_settings.py"""

        if self._make_file():
            self._add_database()
            self._add_secret_key()
            print("Everything was done successfully.")

    def _make_file(self) -> bool:
        """Check local_settings.py is exists or not

        Returns
        -------
        True -> if is not exists local_settings.py file created file and return True
        False -> if local_settings.py is existed do nothing and return False
        """

        if not os.path.exists(self.LOCAL_SETTINGS_PATH):
            with open(self.LOCAL_SETTINGS_PATH, "wt"):
                print("local_settings.py is created.")

            return True
        else:
            print('The local_settings.py is exist. \n',
                  'I cant make it new for you.')

            return False

    def _add_secret_key(self):
        """Add SECRET_KEY in local_settings.py"""

        with open(self.LOCAL_SETTINGS_PATH, "a") as file:
            file.write("# SECURITY WARNING: keep the secret key used in production secret! \n")
            file.write(f"SECRET_KEY = '{self.get_secret_key}' \n")

        print("SECRET_KEY is added to local_settings.py.")

    def _add_database(self):
        """Get user choose database and call the database method"""

        switcher = {
            1: self._add_sqlite,
            2: self._add_mysql
        }

        func = switcher.get(self._database_input_validation())
        func()

    def _add_sqlite(self):
        """Add SQLite engine to local_settings.py"""

        with open(self.LOCAL_SETTINGS_PATH, "a") as file:
            lines = [
                "from pathlib import Path\n\n\n",
                "BASE_DIR = Path(__file__).resolve().parent.parent\n\n\n",
                "# Database\n",
                "# https://docs.djangoproject.com/en/3.2/ref/settings/#databases\n",
                "DATABASES = {\n",
                "    'default': {\n",
                "        'ENGINE': 'django.db.backends.sqlite3',\n",
                "        'NAME': BASE_DIR / 'db.sqlite3',\n",
                "    }\n",
                "}\n\n\n"]

            file.writelines(lines)

        print("SQLite is added to local_settings.py.")

    def _add_mysql(self):
        """Add MySQL engine to local_settings.py"""

        with open(self.LOCAL_SETTINGS_PATH, "a") as file:
            lines = [
                "# Database\n",
                "# https://docs.djangoproject.com/en/3.2/ref/settings/#databases\n",
                "DATABASES = {\n",
                "    'default': {\n",
                "        'ENGINE': 'django.db.backends.mysql',\n",
                f"        'NAME': '{input('give me MySQL NAME: ')}',\n",
                f"        'USER': '{input('give me MySQL USER: ')}',\n",
                f"        'PASSWORD': '{input('give me MySQL PASSWORD: ')}',\n",
                f"        'HOST': '{input('give me MySQL HOST (ex: 127.0.0.1): ')}',\n",
                f"        'PORT': '{input('give me MySQL PORT (ex: 5432): ')}',\n",
                "    }\n",
                "}\n\n\n"]

            file.writelines(lines)

        print("MySQL is added to local_settings.py.")

    def _database_input_validation(self) -> int:
        """check user input and validation input from user

        Returns
        -------
        int(1) -> for SQLite3
        int(2) -> for MySQL

        """

        while True:
            print('\n \nfor add SQLite3 database to project (1) ')
            print('for add MySQL database to project (2) ')
            try:
                option = int(input('select your database: '))
            except ValueError:
                print("your input is not valid, please try again.")
                continue

            if option in range(1, 3):
                return option

            print("your input is not valid, please try again.")

    @property
    def get_secret_key(self) -> str:
        """Get Django SECRET_KEY from generate_secret_key() method and save it in instance of class"""

        return self._SECRET_KEY

    @classmethod
    def generate_secret_key(cls) -> str:
        """Generate Django SECRET_KEY for every time to call method"""

        return f"django-insecure-{get_random_secret_key()}"


if __name__ == '__main__':
    a = ProjectInit()
    a.tasks()
