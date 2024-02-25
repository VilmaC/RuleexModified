import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='RuleexModified',
    description='Rule extraction methods from neural networks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/VilmaC/RuleexModified.git',
    author='Vilma',
    author_email='vilma.virtu@gmail.com',
    license='MIT',
    packages=['ruleex',
              'ruleex.anndt',
              'ruleex.deepred',
              'ruleex.hypinv',
              'ruleex.tree'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ]
)
