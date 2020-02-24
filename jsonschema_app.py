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


def do_post_schema_validation(project_dict):
    """
    Does post-schema validation of project_dict as documented in Targets.md.

    :param project_dict:
    :raises RuntimeException: if proj_config_dict is invalid
    """
    project = None  # todo

    locations = validate_and_create_locations(project, project_dict)
    click.echo(f"- created {len(locations)} Locations: {locations}")

    targets = validate_and_create_targets(project, project_dict)
    click.echo(f"- created {len(targets)} Targets: {targets}")

    timezeros = validate_and_create_timezeros(project, project_dict)
    click.echo(f"- created {len(timezeros)} TimeZeros: {timezeros}")


def validate_and_create_locations(project, project_dict):
    # no validation necessary
    return []  # todo


def validate_and_create_targets(project, project_dict):
    targets = []
    type_name_to_type_int = None  # todo
    for target_dict in project_dict['targets']:
        type_name = _validate_target_dict(target_dict, type_name_to_type_int)  # raises RuntimeError if invalid
    return targets


def _validate_target_dict(target_dict, type_name_to_type_int):
    type_name = target_dict['type']

    # check for step_ahead_increment required if is_step_ahead
    if target_dict['is_step_ahead'] and ('step_ahead_increment' not in target_dict):
        raise RuntimeError(f"step_ahead_increment not found but is required when is_step_ahead is passed. "
                           f"target_dict={target_dict}")

    # todo

    return type_name


def validate_and_create_timezeros(project, project_dict):
    return []  # todo


if __name__ == '__main__':
    app()
