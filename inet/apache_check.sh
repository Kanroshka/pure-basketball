#!/bin/bash

if [ ! -f "/var/log/apache2/access.log" ]; then
    exit 1
fi

grep -E ' 404 | 403 | 500 ' /var/log/apache2/access.log > /tmp/apache_errors.log

count=$(wc -l < /tmp/apache_errors.log)
echo "$count"

awk '{print $1}' /tmp/apache_errors.log | sort | uniq -c | sort -nr > /tmp/apache_top_ips.log
cat /tmp/apache_top_ips.log

awk '{print $7}' /tmp/apache_errors.log | sort | uniq -c | sort -nr > /tmp/apache_top_urls.log
cat /tmp/apache_top_urls.log

rm /tmp/apache_errors.log
rm /tmp/apache_top_ips.log
rm /tmp/apache_top_urls.log

exit 0
