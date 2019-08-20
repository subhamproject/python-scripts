import filecmp
import os
import shutil

def test_diff_files():
    """Create two files with different contents and compare results."""

    folder1 = 'results1'
    folder2 = 'results2'
    os.mkdir(folder1)
    os.mkdir(folder2)

    file1 = os.path.join(folder1, 'hello_world.txt')
    with open(file1, 'w') as file:
        file.write('foo')

    file2 = os.path.join(folder2, 'hello_world.txt')
    with open(file2, 'w') as file:
        file.write('bar')

    comparison = filecmp.dircmp(folder1, folder2)

    try:
        assert comparison.diff_files == ['hello_world.txt']
        assert comparison.same_files == []
    except AssertionError:
        raise
    finally:
        shutil.rmtree(folder1)
        shutil.rmtree(folder2)

# Run the test 100 times to get percent accuracy
failures = 0
for _ in range(100):
    try:
        test_diff_files()
    except AssertionError:
        failures += 1

print("%i 'same files' out of 100 expected 'diff files'" % failures)
