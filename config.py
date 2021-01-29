import configparser
import os
import sys


class Server:
    RunMode: str
    HttpPort: int

    def __init__(self, run_mode: str, http_port: int):
        self.RunMode = run_mode
        self.HttpPort = http_port


class Database:
    User: str
    Password: str
    Host: str
    Name: str
    Port: int

    def __init__(self, host: str, port: int, user: str, password: str, database: str) -> None:
        self.Host = host
        self.User = user
        self.Password = password
        self.Name = database
        self.Port = port


cfg = configparser.ConfigParser()
cfg.read(sys.path[0] + '/conf/app.ini')


def get_dict(section: str) -> dict:
    result = {}
    for item in cfg.items(section):
        result[item[0]] = item[1]
    return result


def get_server_info() -> Server:
    info = get_dict("server")
    return Server(info.get('runmode'), info.get('httpport'))


def get_database_info(env: str) -> Database:
    info = get_dict("database_" + env)
    return Database(info.get('host'), info.get('port'), info.get('user'), info.get('password'), info.get('name'))


if __name__ == '__main__':
    print(cfg.items("server"))
    print(get_dict("server"))
    print(get_server_info().HttpPort)
    print(get_database_info("dev").Host)
    print(get_database_info("dev").Port)
