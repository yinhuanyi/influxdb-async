# coding: utf-8
"""
@Author: Robby
@Module name: async_api.py
@Create date: 2020-06-11
@Function: 
"""

from threading import Thread

from influxdb import InfluxDBClient

class InfluxdbMultiFieldsAsync(Thread):

    def __init__(self, host, port, database, measurement, tags, fields_list, username=None, password=None):
        self.host = host
        self.port = port
        self.database = database
        self.measurement = measurement
        self.tags = tags
        self.fields_list = fields_list
        self.username = username
        self.password = password
        super(InfluxdbMultiFieldsAsync, self).__init__()

    def __enter__(self):
        if self.username and self.password:
            self.influxdb_connect = InfluxDBClient(host=self.host, port=self.port, username=self.username, password=self.password, database=self.database, timeout=6)
        else:
            self.influxdb_connect = InfluxDBClient(host=self.host, port=self.port, database=self.database, timeout=6)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.influxdb_connect.close()

    def __json_data(self, fields):
        """
        :return:
        json_body = [
            {
                "measurement": "cpu_load_short",
                "tags": {
                    "host": "server01",
                    "region": "us-west"
                },
                "time": "2009-11-10T23:00:00Z",
                "fields": {
                    "value": 0.64
                }
            }
        ]
        """

        inter_dict = dict()
        json_body = list()
        inter_dict.update(measurement=self.measurement)
        inter_dict.update(fields=fields)
        inter_dict.update(tags=self.tags)
        json_body.append(inter_dict)

        return json_body

    def run(self):
        try:
            # 有多少行fields就写多少次
            for i in range(len(self.fields_list)):
                json_data = self.__json_data(self.fields_list[i])
                self.influxdb_connect.write_points(json_data)
        except Exception as e:
            raise Exception(e)








