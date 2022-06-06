# Change limits file

exec { 'change limits':
  command  => "sed -i 's/holberton//' /etc/security/limits.conf",
  provider => shell
}
