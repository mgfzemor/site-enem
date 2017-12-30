__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"
from classes.Database import *
import logging

logger = logging.getLogger(__name__);

class ProvaObjetiva():
    cursor = Database.getCursor();

    def __init__(self,tupla):
        self.codigo = tupla[0];
        self.codinscricao = tupla[1];
        self.presencacn = tupla[2];
        self.presencach = tupla[3];
        self.presencalc = tupla[4];
        self.presencamt = tupla[5];
        self.corprovacn = tupla[6];
        self.corprovach = tupla[7];
        self.corprovalc = tupla[8];
        self.corprovamt = tupla[9];
        self.notacn = tupla[10];
        self.notach = tupla[11];
        self.notalc = tupla[12];
        self.notamt = tupla[13];
        self.notamedia = tupla[14];
        self.respostascn = tupla[15];
        self.respostasch = tupla[16];
        self.respostaslc = tupla[17];
        self.respostasmt = tupla[18];

    def toString(self):
        return "ProvaObjetiva[{},{},{}]".format(self.codigo, self.codinscricao, self.notamedia);

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO provaobjetiva VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    'FIND_BY_ID': """SELECT * FROM provaobjetiva WHERE codinscricao = {} """};
        return queries[query];

    @staticmethod
    def insert(values, cursor):
        try:
            logger.debug("ProvaObjetiva: Inserting values: {}".format(values));
            query = ProvaObjetiva.getQuery('INSERT');
            cursor.execute(query,values);
        except Exception as e:
            logger.error("ProvaObjetiva: Exception during insert values: {}".format(e));
            raise

    @staticmethod
    def findByCod(cod):
        try:
            logger.debug("Find ProvaObjetiva by cod.");
            query = ProvaObjetiva.getQuery('FIND_BY_ID');
            query = query.format(cod);
            ProvaObjetiva.cursor.execute(query);
            result = ProvaObjetiva.cursor.fetchone();
            if result:
                result = ProvaObjetiva(result);
            return result;
        except Exception as e:
            logger.error("class: (ProvaObjetiva) Method: (findByCod) : Exception ({}).".format(e));
            raise

    @staticmethod
    def getValues(columns,dd,cod):
        try:
            logger.debug("ProvaObjetiva: Getting values from file columns.");
            codigo = cod;
            codinscricao = int(columns[dd['NU_INSCRICAO']]);
            presencacn = int(columns[dd['IN_PRESENCA_CN']]);
            presencach = int(columns[dd['IN_PRESENCA_CH']]);
            presencalc = int(columns[dd['IN_PRESENCA_LC']]);
            presencamt = int(columns[dd['IN_PRESENCA_MT']]);
            corprovacn = -1 if columns[dd['ID_PROVA_CN']] == '' else int(columns[dd['ID_PROVA_CN']]);
            corprovach = -1 if columns[dd['ID_PROVA_CH']] == '' else int(columns[dd['ID_PROVA_CH']]);
            corprovalc = -1 if columns[dd['ID_PROVA_LC']] == '' else int(columns[dd['ID_PROVA_LC']]);
            corprovamt = -1 if columns[dd['ID_PROVA_MT']] == '' else int(columns[dd['ID_PROVA_MT']]);
            notacn = 0.0 if columns[dd['NOTA_CN']] == '' else float(columns[dd['NOTA_CN']]);
            notach = 0.0 if columns[dd['NOTA_CH']] == '' else float(columns[dd['NOTA_CH']]);
            notalc = 0.0 if columns[dd['NOTA_LC']] == '' else float(columns[dd['NOTA_LC']]);
            notamt = 0.0 if columns[dd['NOTA_MT']] == '' else float(columns[dd['NOTA_MT']]);
            notamedia = (notacn + notach + notalc + notamt)/4;
            respostascn = -1 if columns[dd['TX_RESPOSTAS_CN']] == '' else columns[dd['TX_RESPOSTAS_CN']];
            respostasch = -1 if columns[dd['TX_RESPOSTAS_CH']] == '' else columns[dd['TX_RESPOSTAS_CH']];
            respostaslc = -1 if columns[dd['TX_RESPOSTAS_LC']] == '' else columns[dd['TX_RESPOSTAS_LC']];
            respostasmt = -1 if columns[dd['TX_RESPOSTAS_MT']] == '' else columns[dd['TX_RESPOSTAS_MT']];
            values = (codigo,codinscricao, presencacn, presencach, presencalc, presencamt, corprovacn, corprovach, corprovalc, corprovamt, notacn, notach, notalc, notamt, notamedia, respostascn, respostasch, respostaslc, respostasmt);
            ret = values;
        except Exception as e:
            logger.error("ProvaObjetiva: Exception during get values from columns: {}".format(e));
            ret = None;
        return ret;
