import autotraders
import click

from website.app import create_app

print(" * Running autotraders version check")
accepted_autotraders_major_version = 2
accepted_autotraders_minor_versions = [0, 1, 2, 3]
warning_autotraders_minor_versions = [0, 1, 3]

autotraders_major_version = int(autotraders.__version__.split(".")[0])
autotraders_minor_version = int(autotraders.__version__.split(".")[1])

if autotraders_major_version > accepted_autotraders_major_version:
    raise ValueError(
        "Please downgrade autotraders to v"
        + str(accepted_autotraders_major_version)
        + "."
        + str(max(accepted_autotraders_minor_versions))
        + ".x"
    )

if (
        autotraders_minor_version not in accepted_autotraders_minor_versions
        and autotraders_minor_version < min(accepted_autotraders_minor_versions)
):
    raise ValueError(
        "Please upgrade autotraders to v"
        + str(accepted_autotraders_major_version)
        + "."
        + str(max(accepted_autotraders_minor_versions))
        + ".x"
    )
elif (
        autotraders_minor_version not in accepted_autotraders_minor_versions
        and autotraders_minor_version < max(accepted_autotraders_minor_versions)
):
    raise ValueError(
        "Please downgrade autotraders to v"
        + str(accepted_autotraders_major_version)
        + "."
        + str(max(accepted_autotraders_minor_versions))
        + ".x"
    )
elif autotraders_minor_version not in accepted_autotraders_minor_versions:
    raise ValueError(
        "Please install autotraders v"
        + str(accepted_autotraders_major_version)
        + "."
        + str(max(accepted_autotraders_minor_versions))
        + ".x"
    )
elif autotraders_minor_version in warning_autotraders_minor_versions:
    print(f" * Warning: Autotraders v{autotraders.__version__} is not officially supported, procceed at your own risk.")
print(" * Acceptable version found: Autotraders v" + autotraders.__version__)


@click.command()
@click.option("--debug", is_flag=True)
@click.option("--port", default=5000)
@click.option("--threaded", is_flag=True)
def cmd(debug, port, threaded):
    create_app().run(debug=debug, port=port, threaded=threaded)


if __name__ == "__main__":
    cmd()
