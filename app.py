import json
from pathlib import Path

import click
from jsonschema import validate


@click.command()
def app():
    """
    App that plays with using https://python-jsonschema.readthedocs.io to validate a) zoltar3 project
    definition json files, and b) forecast json files.
    """
    with open(Path('inferred-schema.json')) as schema_fp, \
            open(Path('docs-project.json')) as docs_instance_fp:
        schema_dict = json.load(schema_fp)
        docs_instance_dict = json.load(docs_instance_fp)
    click.echo("validating...")
    validate(instance=docs_instance_dict, schema=schema_dict)
    click.echo("valid!")


if __name__ == '__main__':
    app()
