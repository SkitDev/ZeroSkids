from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="zeroskids",
    version="1.5",
    author="SkitDev",
    description="Truly skid-proof Python obfuscator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SkitDev/ZeroSkids",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[],
)
