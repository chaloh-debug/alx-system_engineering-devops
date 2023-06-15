# fix too many requests in nginx server

exec {'fix-default-limit':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx",
  provider => shell
}

exec {'restart':
  provider => shell,
  command => 'sudo service nginx restart'
}
