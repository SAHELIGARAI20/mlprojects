
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Saheli Garai',
    author_email='saheligarai261@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
