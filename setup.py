import setuptools

setuptools.setup(
    name="take_photo",
    version="1.0.0",
    author="Michał Nieznański",
    author_email="nieznanm@gmail.com",
    description="Take a photo with a webcam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["opencv-python"]
)
