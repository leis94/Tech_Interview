import os
import pandas as pd

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps

from nba.models import nbaPlayer

from sqlalchemy import create_engine


# create sqlalchemy engine
engine = create_engine('sqlite:///db.sqlite3')


class Command(BaseCommand):
    help = 'Load the nba.xlsx file into the database'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model_name = nbaPlayer
    

    def handle(self, *args, **options):
        app_path = apps.get_app_config('nba').path
        file_path = os.path.join(app_path, 'management',
                                 'commands', 'nba.xlsx')
        df_read = pd.read_excel(file_path)
        df_read.rename(columns={'Height':'Date'}, inplace=True)
        df_read.to_sql('nba_nbaplayer', con=engine, if_exists='append', index=False)