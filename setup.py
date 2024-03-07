from setuptools import setup, find_packages as _fp

# Using a context manager for safely opening and reading requirements.txt
with open('requirements.txt', 'r') as file:
    install_requires = [line.strip() for line in file if line.strip()]

setup(
    name='openai-contentcreator',
    version='0.1.0',
    description='A Package that helps you create content using OpenAI.',
    author='Eric Baker',
    author_email='e-baker@noreply.users.github.com',
    packages=_fp(),  # Here we use the alias _fp instead of find_packages
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
)
