from setuptools import setup

setup(
    name="rip-beacon",
    version="1.0",
    description="Simple RIPv2 beacon",
    author="Tom Petr",
    author_email="trpetr@gmail.com",
    packages=["rip_beacon"],
    entry_points={"console_scripts": ["rip-beacon:rip_beacon:main"]},
)
