import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Calculadora-con-AB",
    version="0.0.2",
    author="Alex Montaño Rojas",
    author_email="alex.lx.man.alstaraciend@gmail.com",
    description="calculadora usando arboles binarios",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BPBO/Project1",
    packages= ['Calculadora_pkg'],
    entry_pints= {'gui_scripts': ['Calculadora_pkg = Calculadora_pkg.__main__:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)