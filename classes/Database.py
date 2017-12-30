__author__ = "Mario Figueiro Zemor";
__email__ = "mario.figueiro@ufgrs.br";

import psycopg2
import config.db as db
import logging

logger = logging.getLogger(__name__);

class Database():
    def __init__(self):
        pass

    @staticmethod
    def connect():
        ret = None;
        try:
            logger.debug("connecting to postgres db: {} {} {}".format(db.host,db.user,db.dbname));
            conn = psycopg2.connect(host=db.host,user=db.user,password=db.password,dbname=db.dbname);
            ret = conn;
            return ret;
        except Exception as e:
            logger.error("Exception during postgres connetion: {}".format(e));
            raise

    @staticmethod
    def getCursor():
        try:
            connection = Database.connect();
            cursor = connection.cursor();
            return cursor;
        except Exception as e:
            logger.error("class: (Database) method: (getCursor) - Exception during get cursor: {}".format(e));
            raise
