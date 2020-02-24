import copy
import json
from pathlib import Path

import click
from deepdiff import DeepDiff


@click.command()
def app():
    """
    App that plays with using https://deepdiff.readthedocs.io/en/latest/ to compare two zoltar3 project definition
    configuration dicts/files.
    """
    with open(Path('docs-project.json')) as fp:
        in_project_dict = json.load(fp)
    click.echo("diffing...")

    #
    # locations
    #

    # remove
    edited_project_dict = copy.deepcopy(in_project_dict)
    del (edited_project_dict['locations'][0])
    dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True)
    # dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True, view='tree')
    print('l1', dd)
    # {'iterable_item_removed': {"root['locations'][0]": {'name': 'location1'}}}

    # add
    edited_project_dict = copy.deepcopy(in_project_dict)
    edited_project_dict['locations'].append({"name": "location4"})
    dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True)
    print('l2', dd)
    # {'iterable_item_added': {"root['locations'][3]": {'name': 'location4'}}}

    #
    # timezeros
    #

    # remove
    edited_project_dict = copy.deepcopy(in_project_dict)
    del (edited_project_dict['timezeros'][0])
    dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True)
    print('tz1', dd)
    # {'iterable_item_removed': {"root['timezeros'][0]": {'timezero_date': '2011-10-02', 'is_season_start': True, 'season_name': '2011-2012'}}}

    # add
    edited_project_dict = copy.deepcopy(in_project_dict)
    edited_project_dict['timezeros'].append({"timezero_date": "2011-10-02x",
                                             "is_season_start": True,
                                             "season_name": "2011-2012"})
    dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True)
    print('tz2', dd)
    # {'iterable_item_added': {"root['timezeros'][3]": {'timezero_date': '2011-10-02x', 'is_season_start': True, 'season_name': '2011-2012'}}}

    # edit: is_season_start
    edited_project_dict = copy.deepcopy(in_project_dict)
    edited_project_dict['timezeros'][0]['is_season_start'] = False
    del(edited_project_dict['timezeros'][0]['season_name'])
    dd = DeepDiff(in_project_dict, edited_project_dict, ignore_order=True)
    print('tz3', dd)
    # {'iterable_item_added':   {"root['timezeros'][0]": {'timezero_date': '2011-10-02', 'is_season_start': False}},
    #  'iterable_item_removed': {"root['timezeros'][0]": {'timezero_date': '2011-10-02', 'is_season_start': True, 'season_name': '2011-2012'}}}~~

    #
    # targets: xx
    #
    pass

    # done
    click.echo("done")


if __name__ == '__main__':
    app()
