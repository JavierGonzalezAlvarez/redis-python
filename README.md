##  redis

# installation
$ sudo add-apt-repository ppa:redislabs/redis
$ sudo apt-get update
$ sudo apt-get install redis

# version of redis
$ redis-server
$ redis-cli --version

# before starting
- short keys
- separation for the keys
- string < 512 mb
- list => queues
- hashes = objects
- sets and sorted sets => unordered collections of binary safe things
- key / value => to store data

# commands
- list of commands
    $ redis-cli -h 
- connect to a remote server
    $ redis-cli -h 
- connect to a specific port
    $ redis-cli -p 6380
- some info
    $ redis-cli info
- name of the db
    $ config get dbfilename
- configuration
    sudo nano /etc/redis/redis.conf

# comands in redis-cli
> config get dir  => give back 2 rows, parameter name and value of the parameter
> config set
> config get dbfilename => give back name of the DB
> config get * => all parameters
> config set {name parameter} {value parameter} => in run-time
> config set loglevel => values in parameter loglevel
ie: config set loglevel verbose => set verbose

## python and redis

# install python3 to handle redis
$ sudo apt install python3-pip
$ pip3 install redis
$ pip3 install hiredis

# install python2 to handle redis
$ sudo apt install python
$ pip install redis
$ pip install python==2.7.4
$ pip install hiredis

# redis python  documentation
https://redis-py.readthedocs.io/en/stable/genindex.html

# install entorno virtual
sudo apt install python3-virtualenv

# Crear el proyecto en django y en un entorno virtual para python3
virtualenv ev -p python3

# Crear el proyecto en django y en un entorno virtual para python2
virtualenv ev -p python
source ev/bin/activate

# desactivar entorno virtual
deativate

# if error:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'redis' has no attribute 'Redis'
solution: not name redis.py another file

# start redis to work with python
$ redis-server

# connection to 127.0.0.1 6379
$ redis-cli

# exit from redis
$ exit







