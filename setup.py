import os

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()


def prerelease_local_scheme(version):
    """
    Return local scheme version unless building on master in CircleCI.

    This function returns the local scheme version number
    (e.g. 0.0.0.dev<N>+g<HASH>) unless building on CircleCI for a
    pre-release in which case it ignores the hash and produces a
    PEP440 compliant pre-release version number (e.g. 0.0.0.dev<N>).
    """
    from setuptools_scm.version import get_local_node_and_date

    if os.getenv('CIRCLE_BRANCH') in ('master', ):
        return ''
    else:
        return get_local_node_and_date(version)


setup(
    name='large-image-bin-utils',
    use_scm_version={'local_scheme': prerelease_local_scheme, 'fallback_version': '0.0.0'},
    setup_requires=['setuptools-scm'],
    description='Python access to binary executables for large_image',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    license='Apache Software License 2.0',
    long_description=readme,
    long_description_content_type='text/x-rst',
    keywords='large-image',
    url='https://github.com/girder/largr_image',
    packages=['large_image_bin_utils'],
    package_data={'large_image_bin_utils': ['bin/*']},
    python_requires='>=3.6',
    zip_safe=True,
    include_package_data=True,
    entry_points={'console_scripts': [
        '%s=large_image_bin_utils.bin:program' % name
        for name in os.listdir('large_image_bin_utils/bin')
        if not name.endswith('.py')]},
)
