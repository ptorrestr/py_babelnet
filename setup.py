from setuptools import setup
import subprocess
import os

root_path = os.path.dirname(os.path.realpath(__file__))
readme_file_path = os.path.join(root_path, 'README.md')
version_file_path = os.path.join(root_path, 'VERSION')
name_package = 'py_babelnet'
src_path = name_package

def readme():
    with open(readme_file_path) as f:
        return f.read()

def version():
    # default version
    version = "0.0.1"
    # Get version from git if any
    out = subprocess.Popen(['git', 'describe', '--tags'],
            stdout = subprocess.PIPE, universal_newlines = True)
    out.wait()
    # If version is available
    if out.returncode == 0:
        m_version = out.stdout.read().strip()
        m_version = m_version.split("-")
        if len(m_version) > 0:
            version = m_version[0]
            # Save to file for future readings
            with open(version_file_path, 'w') as f:
                f.write(version)
    else:
        # When git is not available, we check the file
        # This is the case when the code is distributed
        # without git references
        with open(version_file_path) as f:
            version = f.read()
    print(version)
    return version

setup(
        name = name_package,
        version = version(),
        description = "Python package for babelnet API",
        long_description = readme(),
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python :: 3.6',
            ],
        url = "",
        author = 'Pablo Torres',
        author_email = 'pablo.torres.t@gmail.com',
        license = 'MIT',
        packages = [name_package],
        setup_requires = ['pytest-runner'],
        install_requires = ['requests'],
        tests_require = ['pytest'],
        test_suite = 'tests',
    )
