
name = "PyOpenGL"

description = "Standard OpenGL bindings for Python"

version = "3.1.5"

requires = []

variants = [
    ["python-2.7"],
    ["python-3.6"],
    ["python-3.7"],
]


private_build_requires = ["rezutil-1", "pipz"]
build_command = "python -m rezutil build {root} --use-pipz"


def commands():
    env = globals()["env"]

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
