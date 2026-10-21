# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.
import subprocess


def test_rock(rock_container):
    """Test rock."""
    # assert the rock contains the expected files
    subprocess.run(
        [
            "docker",
            "exec",
            rock_container[1],
            "ls",
            "-la",
            "/third_party/mariadb-connector-c",
        ],
        check=True,
    )

    subprocess.run(
        ["docker", "exec", rock_container[1], "ls", "-la", "/bin/metadata_store_server"],
        check=True,
    )
