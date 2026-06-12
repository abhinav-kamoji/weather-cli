from setuptools import setup

setup(
    name="weather-cli",
    version="1.0",
    packages=find_packages(),  
    install_requires=[
        "typer",
        "requests",
        "yaspin",
        "python-dotenv",
        "inquirer",
    ],


      entry_points={
        "console_scripts": [
            "weather=weather_cli.main:app",
            "weather-config=weather_cli.config:setup"
        ],
    },
)
