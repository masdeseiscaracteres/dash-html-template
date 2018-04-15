from setuptools import setup

setup(
    name='dash_html_template',
    version=0.1,
    author='Óscar González',
    author_email='masdeseiscaracteres@gmail.com',
    packages=['dash_html_template'],
    license='MIT',
    description='Dash component tree generator from HTML template',
    install_requires=['dash_html_components', 'lxml']
)