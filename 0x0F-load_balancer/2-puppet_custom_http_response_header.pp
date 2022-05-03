# Manifiest that configures with puppet

exec { 'update':
  command => 'sudo apt-get -y update',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'install_nginx':
  require => Exec['update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'exec_sed':
  require => Exec['install_nginx'],
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin'],
  returns => [0,1]
}

exec { 'exec_nginx':
  require => Exec['exec_sed'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin'],
  returns => [0,1]
}
