from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='rpi_ws281x_cool_animations',
      version='0.0',
      description='Cool animations for led matrixes of the family rpi_ws281x on Raspbian',
      long_description=readme(),
      classifiers=[
            'Development Status :: 0 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Text Processing :: Linguistic',
      ],
      keywords='raspberry raspbian matrix rpi_ws281x animations',
      url='http://github.com/RiccardoCereghino/rpi_ws281x_cool_animations',
      author='Riccardo Cereghino',
      author_email='riccardo.cereghino@gmail.com',
      license='MIT',
      packages=['rpi_ws281x_cool_animations'],
      install_requires=[
      ],
      dependency_links=['https://github.com/jgarff/rpi_ws281x'],
      zip_safe=False)