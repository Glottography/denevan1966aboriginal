from setuptools import setup
import json


with open('metadata.json', encoding='utf-8') as fp:
    metadata = json.load(fp)


setup(
    name='cldfbench_denevan1966aboriginal',
    description=metadata['title'],
    license=metadata.get('license', ''),
    url=metadata.get('url', ''),
    py_modules=['cldfbench_denevan1966aboriginal'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'denevan1966aboriginal=cldfbench_denevan1966aboriginal:Dataset',
        ]
    },
    install_requires=[
        'pyglottography>=2.0',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
