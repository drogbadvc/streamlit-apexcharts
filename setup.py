import setuptools
from os.path import dirname
from os.path import join


def readme() -> str:
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


setuptools.setup(
    name="streamlit_apexjs",
    version="0.0.3",
    author="Andell",
    author_email="drogadvc@gmail.com",
    description="streamlit_apexcharts React component for Streamlit",
    packages=setuptools.find_packages(),
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/drogbadvc/streamlit-apexcharts",
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
