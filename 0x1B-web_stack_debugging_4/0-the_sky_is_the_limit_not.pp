#a puppet script that increases limit
exec { 'increase ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
