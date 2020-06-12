###  influxdb-async 模块使用方法



> **`(一)：安装`**

- 从 PYPI 安装

```
pip install influxdb-async
```

- 从 Github 安装

```
pip isntall git+https://github.com/yinhuanyi/influxdb-async.git
```

> **`(二)：使用方法`**

```
from influxdb_async import InfluxdbMultiFieldsAsync


host = '100.122.0.2'
port = 8086
database = 'db1'
measurement = 'measurement1'
tags = {"host": "server1", "env": "env1"}
fields_list = [{"value": 1}, 
               {"value": 2}, 
               {"value": 3}]
username = 'username'
password = 'password'

# 如果influxdb没有用户名和密码
with InfluxdbMultiFieldsAsync(host, port, database, measurement, tags, fields_list) as influxdb:
    influxdb.start()
    
    
# 如果influxdb有用户名和密码
with InfluxdbMultiFieldsAsync(host, port, database, measurement, tags, fields_list, username=username, password=password) as influxdb:
    influxdb.start()
```

> **`(三)：influxdb显示效果`**

```
> use db1;
Using database db1
> select * from measurement1;
name: measurement1
time                env  host    value
----                ---  ----    -----
1591946958016786087 env1 server1 1
1591946958229993773 env1 server1 2
1591946958438736358 env1 server1 3
```
