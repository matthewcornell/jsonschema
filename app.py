import json
from pathlib import Path

import click
import jsonschema


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
    try:
        click.echo("validating against schema...")
        jsonschema.validate(instance=docs_instance_dict, schema=schema_dict)
        do_post_schema_validation(docs_instance_dict)
        click.echo("valid!")
    except jsonschema.exceptions.ValidationError as ve:
        click.echo(f"invalid: {ve}")


def do_post_schema_validation(proj_config_dict):
    """
    Does post-schema validation of proj_config_dict as documented in Targets.md.

    :param proj_config_dict:
    :raises RuntimeException: if proj_config_dict is invalid
    """
    pass  # todo


if __name__ == '__main__':
    app()
