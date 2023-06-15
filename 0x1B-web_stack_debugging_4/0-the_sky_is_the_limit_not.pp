# fix too many requests in nginx server
# traffic amount fix

exec {fix-default-limit:
  command => 'sed -i "s/15/4096 /etc/default/nginx"',
  path => 'usr/local/bin:/bin/',
}

exec {restart:
    provider => shell,
    command => 'sudo service nginx restart',
}
