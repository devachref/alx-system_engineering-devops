#!/usr/bin/pup
# Installs flask
package { 'flask':
  ensure   => '2.5.0',
  provider => 'pip3',
}
