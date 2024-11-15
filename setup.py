#-------------------------------------------------------
#
# Library Set-up File.
# author: Kananelo Chabeli
#-------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="uRAD-firmware",                         		# Replace with your project name
    version="1.0.0",                            		# Version of your package
    description="uRAD firmware library and script that reads the raw dara from the uRAD system",   # Short description
    author="Kananelo Chabeli",
    author_email="kchabeli688@gmail.com",
    url="https://github.com/your-repo",         		# GitHub repository or project URL
    packages=find_packages(),                   		# Automatically find and include the library
    py_modules=["uRAD"],                      			# Include the uRAD.py
    entry_points={
        'console_scripts': [
            'urad=uRAD:main',            				# Define `urad` as an executable
        ],
    },
    install_requires=['serial'],                        # List dependencies if any
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)