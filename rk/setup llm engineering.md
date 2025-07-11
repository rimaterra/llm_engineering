# LLM Engineering Class Setup Mac or Linux

June 18, 2025

## Grab the class files

Clone the class repository into a _temporary_ folder. We will copy the
contents of this folder into our working folder after we get setup for
our environment.

    git clone https://github.com/ed-donner/llm_engineering.git

## Prepare our working environment

    uv init llm_engineering --python 3.12
    cd llm_engineering

## Add `[tool.uv]` section to bottom of `pyproject.toml` to be compatible with macOS

```sh
[tool.uv]
# Require that the package is available for macOS ARM and x86 (Intel).
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'arm64'",
    "sys_platform == 'darwin' and platform_machine == 'x86_64'",
    "sys_platform == 'linux' and platform_machine == 'x86_64'",
]
```

## Set up virtual environment for Python 3.12

    uv sync --upgrade

## Activate environment

I add the following aliases to my shell

```sh
# Python venv
alias ae='deactivate &> /dev/null; source .venv/bin/activate'
alias de='deactivate'
```

Now I can type the following to activate the environment.

    ae

Check to make sure you are now running Python 3.11

    python3 --version

## Copy the class files to the working folder

Go ahead and overwrite the README. We're not copying the .git folder
from the class. I don't know if that is needed, but we can checkout the
class files again if needed.

## Add the required files to our **activated** environment

    uv add docarray
    uv add python-dotenv
    uv add -r requirements.txt

## Test the environment

     jupyter lab

You can type the following to deactivate the environment if you added the alias

    de

## Convert Existing Environment

I forked the class repo. Then I added a branch for the i9 and m1.

When you set up on a new machine, you need to checkout the appropriate branch and work within the branch.

	git checkout $NAME    (example: i9 for the MBP i9)
	uv venv --python 3.12
	ae

### Create .env

	OPENAI_API_KEY=sk-proj-xxxx
	ANTHROPIC_API_KEY=xxxx
	GOOGLE_API_KEY=xxxx
	DEEPSEEK_API_KEY=xxxx

### Create `pyproject.toml`

**Important:** Uncomment your architecture.

```toml
[project]
name = "llm-engineering"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
[tool.uv]
# Require that the package is available for macOS ARM and x86 (Intel).
required-environments = [
#    "sys_platform == 'darwin' and platform_machine == 'arm64'",
#    "sys_platform == 'darwin' and platform_machine == 'x86_64'",
#    "sys_platform == 'linux' and platform_machine == 'x86_64'",
]
```

### Add the required files to our **activated** environment

    uv add docarray
    uv add python-dotenv
    uv add -r requirements.txt
