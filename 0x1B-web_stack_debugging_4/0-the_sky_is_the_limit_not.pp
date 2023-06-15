# fix too many requests in nginx server

exec {'ulimit':
  provider => shell,
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx",
}

exec {'restart':
  provider => shell,
  command => 'sudo service nginx restart',
}
