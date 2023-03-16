import os
import subprocess

SCRIPT = 'benchmark.py'
IMAGES = [
    {'name': 'Python 3.9', 'image': 'python:3.9-slim'},
    {'name': 'Python 3.10', 'image': 'python:3.10-slim'},
    {'name': 'Python 3.11', 'image': 'python:3.11-slim'},
    {'name': 'PyPy 3.9', 'image': 'pypy:3.9-slim'},
]

# Get the path to the parent directory
parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
lib_source = os.path.join(parent_dir, 'option_pricing')
file_source = os.path.join(parent_dir, 'benchmarking')

def benchmark(image):
    output = subprocess.run(
        [
            'docker',
            'run',
            '-it',
            '--rm',
            '--mount',
            f'type=bind,source={lib_source},target=/option_pricing', # my library directory
            '--mount',
            f'type=bind,source={file_source},target=/benchmarking', # benchmark main file
            '-w',
            '/benchmarking',
            f'{image}',
            'python',
            f'{SCRIPT}',
        ],
        capture_output=True,
        text=True,
    )

    return float(output.stdout.strip())


if __name__=="__main__":
    for image in IMAGES:
        t = benchmark(image=image['image'])
        print(f"{image['name']} took {t} seconds per run.")