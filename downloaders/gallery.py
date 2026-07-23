import os
import subprocess
import tempfile


async def download_from_gallery(url: str):
    temp_dir = tempfile.mkdtemp()

    result = subprocess.run(
        [
            "gallery-dl",
            "-D",
            temp_dir,
            url,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    files = []

    for root, dirs, filenames in os.walk(temp_dir):
        for file in filenames:
            files.append(os.path.join(root, file))

    if not files:
        raise Exception("No file downloaded.")

    return files[0]
