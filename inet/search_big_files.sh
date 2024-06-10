#!/bin/bash

check_disk_space() {
    df -h > find.txt
}

check_large_files() {
    find / -type f -size +100M -exec ls -lh {} + 2>/dev/null >> find.txt
    find / -type d -size +1G -exec du -h {} + 2>/dev/null >> find.txt
}

if [ "$(id -u)" != "0" ]; then
    exit 1
fi

check_disk_space
check_large_files

exit 0
