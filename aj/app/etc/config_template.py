# config.py
#
# config file for aj.py
#
# rename to config.py to use
#


# default values
class Config(object):
    DEBUG = False
    ENVI = 'base'

    # those are used to protect the web-service with Basic-Auth, passed by Apache
    BASIC_AUTH_USER = 'user'
    BASIC_AUTH_PASSWORD = 'password'

    LOGFILE = '/var/log/aj/aj.log'

    # if True, PUT and POST requests will need to contain a uuid parameter
    MANDATE_UUID = True

    # those are used by the DeviceSshAPI call
    SSH_USER = 'ssh-user'
    SSH_PASSWORD = 'ssh-password'

    # how we do log. This would be a rotation of 10 files of 1 Mb in size
    LOG_MAX_SIZE = 1000000
    LOG_BACKUP_COUNT = 10

    # how long we should wait for a device config-save operation
    DEVICE_SAVE_TIMEOUT = 20

    # global SNMP timeout and retry
    SNMP_TIMEOUT = 2
    SNMP_RETRIES = 2


# values for prod
class ProductionConfig(Config):
    ENVI = 'production'


# values for int
class IntegrationConfig(Config):
    DEBUG = True
    ENVI = 'integration'


# values for devel
class DevelopmentConfig(Config):
    DEBUG = True
    ENVI = 'development'

