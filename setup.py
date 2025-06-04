import setuptools

# Read README.md for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Metadata
__version__ = "0.0.0"
REPO_NAME = "End-To-End-Wine-Quality-Prediction"
AUTHOR_USER_NAME = "Tipto-Ghosh"
SRC_REPO = "wine_quality_prediction"
AUTHOR_EMAIL = "tiptoghosh@gmail.com"

setuptools.setup(
    name = SRC_REPO, 
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,  
    description = "An end-to-end ML pipeline and Flask app for predicting wine quality",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src"),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.8",
)
