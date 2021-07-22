# py-code-snippets
Assorted snippets in python


## Setting up your environment
This will only be done once. This environment is configured for python3 and it creates a virtual environment `venv` for execution.  If you don't have python3 installed yet, follow the instructions at https://www.python.org/downloads/

```
python3 -m venv venv
```

## Starting up your development environment
If you're unfamiliar with virtualenv, you have to `activate` a virtual environment to use instead of the host machine's python binaries.  This allows you to have requirements nailed down without affecting your global python.

```
source venv/bin/activate
```