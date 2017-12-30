__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"
from classes.Database import *
import logging

logger = logging.getLogger(__name__);

class ProvaRedacao():
    cursor = Database.getCursor();

    def __init__(self,tupla):
        self.codigo = tupla[0];
        self.codinscricao = tupla[1];
        self.status = ProvaRedacao.getStatus(tupla[2]);
        self.linguaestrangeira = tupla[3];
        self.notard = tupla[4];
        self.notacomp1 = tupla[5];
        self.notacomp2 = tupla[6];
        self.notacomp3 = tupla[7];
        self.notacomp4 = tupla[8];
        self.notacomp5 = tupla[9];

    def toString(self):
        return "ProvaRedacao[{},{},{}]".format(self.codigo, self.codinscricao, self.notard);

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO provaredacao VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    'FIND_BY_ID': """SELECT * FROM provaredacao WHERE codinscricao = {} """};
        return queries[query];

    @staticmethod
    def insert(values, cursor):
        try:
            logger.debug("ProvaRedacao: Inserting values: {}".format(values));
            query = ProvaRedacao.getQuery('INSERT');
            cursor.execute(query,values);
        except Exception as e:
            logger.error("ProvaRedacao: Exception during insert values: {}".format(e));
            raise

    @staticmethod
    def findByCod(cod):
        try:
            logger.debug("Find ProvaRedacao by cod.");
            query = ProvaRedacao.getQuery('FIND_BY_ID');
            query = query.format(cod);
            ProvaRedacao.cursor.execute(query);
            result = ProvaRedacao.cursor.fetchone();
            if result:
                result = ProvaRedacao(result);
            return result;
        except Exception as e:
            logger.error("class: (ProvaRedacao) Method: (findByCod) : Exception ({}).".format(e));
            raise

    @staticmethod
    def getValues(columns,dd,cod):
        try:
            logger.debug("ProvaRedacao: Getting values from file columns.");
            codigo = cod;
            codinscricao = int(columns[dd['NU_INSCRICAO']]);
            status = int(columns[dd['IN_STATUS_REDACAO']]);
            linguaestrangeira = int(columns[dd['TP_LINGUA']]);
            notard = 0.0 if columns[dd['NU_NOTA_REDACAO']] == '' else float(columns[dd['NU_NOTA_REDACAO']]);
            notacomp1 = 0.0 if columns[dd['NU_NOTA_COMP1']] == '' else float(columns[dd['NU_NOTA_COMP1']]);
            notacomp2 = 0.0 if columns[dd['NU_NOTA_COMP2']] == '' else float(columns[dd['NU_NOTA_COMP2']]);
            notacomp3 = 0.0 if columns[dd['NU_NOTA_COMP3']] == '' else float(columns[dd['NU_NOTA_COMP3']]);
            notacomp4 = 0.0 if columns[dd['NU_NOTA_COMP4']] == '' else float(columns[dd['NU_NOTA_COMP4']]);
            notacomp5 = 0.0 if columns[dd['NU_NOTA_COMP5']] == '' else float(columns[dd['NU_NOTA_COMP5']]);
            values = (codigo,codinscricao, status, linguaestrangeira, notard, notacomp1, notacomp2, notacomp3, notacomp4, notacomp5);
            ret = values;
        except Exception as e:
            logger.error("ProvaRedacao: Exception during get values from columns: {}".format(e));
            ret = None;
        return ret;

    @staticmethod
    def getStatus(cod):
        status = { 1: 'Em Branco', 2: 'Anulada',3:'Fuga ao Tema',4:'Nao atende ao tipo textual',5:'Texto Insuficiente',6:'Ausente',7:'Presente e texto conforme os requisitos',8:'Anulada - Fere Direitos Humanos',9:'Copia de texto motivador',10:'Parte do texto desconectada com o tema proposto'};
        return status[cod];
