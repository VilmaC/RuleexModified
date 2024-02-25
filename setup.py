import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RuleexModified',
    version='0.1.0',
    description='Rule extraction methods from neural networks- Update from fantamat93@gmail.com to use with newer versions of Tensorflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/VilmaC/RuleexModified.git',
    author='Vilma',
    author_email='vilma.virtu@gmail.com',
    license='MIT',
    packages=['RuleexModified',
              'RuleexModified.anndt',
              'RuleexModified.deepred',
              'RuleexModified.hypinv',
              'RuleexModified.tree'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ]
)
