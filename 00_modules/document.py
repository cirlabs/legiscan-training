import pandas as pd
import json

from IPython.display import display, Markdown
from pathlib import Path


class DataDictionary:

    def __init__(self, file):
        with open(file) as fp:
            self.data = json.load(fp)

    def tabulate(self, field):
        source_data = self.data[field]
        table_data = []

        caption = f'{field} (<span style="color:green">{source_data["data_type"]}</span>): {source_data["description"]}'
        for k, v in source_data.items():
            if k not in ['description', 'data_type']:
                row_data = {'value': k}
                row_data.update(v)
                table_data.append(row_data)
        df = pd.DataFrame.from_dict(table_data)
        df['description'] = df['description'].str.wrap(50)
        s = df.style.set_caption(caption)
        s.format(na_rep='')
        s.set_table_styles(
            [
                {'selector': 'caption', 'props': 'font-size:1.25em;margin-bottom:10px'},
                {'selector': 'td', 'props': 'white-space:pre-wrap;text-align:left'},
                {'selector': 'th.col_heading', 'props': 'text-align: left;'},
            ],
            overwrite=False,
        )
        s.set_table_styles(
            {('lookup'): [
                {'selector': 'td', 'props': 'border-left: 1px solid #000066;font-family:courier'}]},
            overwrite=False,
            axis=0,
        )
        return s

    def lookup(self, field, values=False):
        if values:
            return self.tabulate(field)
        else:
            display(
                Markdown(
                    f'**Data type** of `{field}`: <span style="color:green">{self.data[field]["data_type"]}</span>'
                )
            )
            display(
                Markdown(f'**Description**: {self.data[field]["description"]}'))


class StaticTables:

    def __init__(self):
        self.data = {x.stem: x for x in Path(
            '../01_inputs/legiscan_static_lookup_tables').glob('*.csv')}

    def load(self, table):
        return pd.read_csv(self.data[table])