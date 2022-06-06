# Change the number of workers for nginx server

exec { 'change workers':
  command  => "sed -i 's/processes 4/processes 7/' /etc/nginx/nginx.conf && sudo service nginx restart",
  provider => shell
}
