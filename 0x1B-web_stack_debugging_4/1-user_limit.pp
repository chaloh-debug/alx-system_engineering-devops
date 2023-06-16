# increase limit of open files by user

#increase soft limit
exec {'soft limit':
  provider => shell,
  command => "sudo sed -i '/holberton soft/s/4/1000/' /etc/security/limits.conf",
}

# increase hard limit
exec {'hard limit':
  provider => shell,
  command => "sudo sed -i '/holberton hard/s/5/10000/' /etc/security/limits.conf",
}
