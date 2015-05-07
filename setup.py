from distutils.core import setup
import utensils

requires = []

packages = [
    'pagerank',
]

setup(
    name='pagerank',
    author='Eytan Daniyalzade',
    author_email='eytan85@gmail.com',
    url='http://daniyalzade.com',
    packages=packages,
    description='Utility to get pagerank of keywords on google',
    long_description=open('README.rst').read(),
    version=utensils.__version__,
    data_files=[
        ('', ['README.rst']),
        ],
    package_dir={
        'utensils': 'utensils'
        },
    install_requires=requires,
    include_package_data=True,
)

