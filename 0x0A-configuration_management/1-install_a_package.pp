#!/usr/bin/pup
# Installs flask
package { 'flask':
  ensure   => '2.4.4',
  provider => 'pip3',
}
