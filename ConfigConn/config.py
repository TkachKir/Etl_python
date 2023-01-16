from configparser import ConfigParser


def configPg(filename='database.ini', section='postgresql'):
    """Парсер конфигурации подключения postgresql"""
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def configMysqp(filename='database.ini', section='mysql'):
    """Парсер конфигурации подключения mysql"""
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]

    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db



