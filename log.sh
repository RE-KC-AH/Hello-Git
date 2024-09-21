#!/usr/bin/bash

echo -e  "\"$(pwd)/log.log\" {\n    daily\n    rotate 7\n    compress\n    missingok\n    notifempty\n}" > /etc/logrotate.d/logreq
