__author__ = "Mario Figueiro Zemor"
__email__ = "mario.figueiro@ufgrs.br"
from classes.Database import *
import logging

logger = logging.getLogger(__name__);

class Estudante():
    cursor = Database.getCursor();

    def __init__(self,tupla):
        self.inscricao = tupla[0];
        self.idade = tupla[1];
        self.sexo = Estudante.getSexo(tupla[2]);
        self.cod_nacionalidade = Estudante.getNacionalidade(tupla[3]);
        self.cod_municipio_resid = tupla[4];
        self.cod_municipio_nasc = tupla[5];
        self.cod_uf_resid = tupla[6];
        self.cod_uf_nasc = tupla[7];
        self.estado_civil = Estudante.getEstadoCivil(tupla[8]);
        self.etnia = Estudante.getEtnia(tupla[9]);
        self.cod_conclusao_EM = Estudante.getConclusaoEM(tupla[10]);
        self.ano_conclusao_EM = tupla[11];
        self.tipo_escola_EM = tupla[12];
        self.tipo_ens_escola_EM = tupla[13];
        self.cod_escola = tupla[14];

    def toString(self):
        return "Estudante[{},{},{}]".format(self.inscricao,self.idade,self.sexo);

    @staticmethod
    def getQuery(query):
        queries = { 'INSERT' : """INSERT INTO estudante VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    'FIND_BY_ID': """SELECT * FROM estudante WHERE codinscricao = {} """};
        return queries[query];

    @staticmethod
    def getEtnia(etnia):
        etnias = { '0': 'Nao Declarado',
                   '1': 'Branca',
                   '2': 'Preta',
                   '3': 'Parda',
                   '4': 'Amarela',
                   '5': 'Indigina'};

        return etnias[etnia];

    @staticmethod
    def getNacionalidade(nacionalidade):
        nacionalidades = {'1': 'Brasileiro(a)', '2': 'Brasileiro(a) Naturalizado(a)', '3': 'Estrangeiro(a)', '4': 'Brasileiro(a) Nato(a), nascido(a) no exterior'};
        return nacionalidades[nacionalidade];

    @staticmethod
    def getEstadoCivil(estado_civil):
        estados = {'0': 'Solteiro(a)', '1': 'Casado(a)/Mora com um(a) companheiro(a)', '2': 'Divorciado(a)/Desquitado(a)/Separado(a)', '3': 'Viuvo(a)'};
        return estados[estado_civil];

    @staticmethod
    def getSexo(sexo):
        sexos = { 'F': 'Feminino', 'M': 'Masculino'};
        return sexos[sexo];

    @staticmethod
    def getConclusaoEM(cod):
        situacao = {1: 'Ja conclui o Ensino Medio', 2: 'Estou cursando e concluirei o Ensino Medio este Ano', 3: 'Estou cursando e concluirei o Ensino Medio apos este ano', 4: 'Nao conclui e nao estou cursando o Ensino Medio'};
        return situacao[cod]

    @staticmethod
    def insert(values,cursor):
        try:
            logger.debug("Inserting values: {} into Student.".format(values));
            query = Estudante.getQuery('INSERT');
            cursor.execute(query,values);
        except Exception as e:
            logger.error("Exception during insert values into Student: {}".format(e));
            raise

    @staticmethod
    def findByCod(cod):
        try:
            logger.debug("Find Studante by cod.");
            query = Estudante.getQuery('FIND_BY_ID');
            query = query.format(cod);
            Estudante.cursor.execute(query);
            result = Estudante.cursor.fetchone();
            if result:
                result = Estudante(result);
            return result;
        except Exception as e:
            logger.error("class: (Estudante) Method: (findByCod) : Exception ({}).".format(e));
            raise

    @staticmethod
    def getValues(columns,dd):
        try:
            logger.debug("Estudante: Getting values from file columns.");
            inscricao = int(columns[dd['NU_INSCRICAO']]);
            idade = int(columns[dd['IDADE']]);
            sexo = columns[dd['TP_SEXO']];
            cod_nacionalidade = int(columns[dd['NACIONALIDADE']]);
            cod_municipio_resid = int(columns[dd['COD_MUNICIPIO_RESIDENCIA']]);
            cod_municipio_nasc = -1 if columns[dd['COD_MUNICIPIO_NASCIMENTO']] == '' else int(columns[dd['COD_MUNICIPIO_NASCIMENTO']]);
            cod_uf_resid = -1 if columns[dd['COD_UF_RESIDENCIA']] == '' else int(columns[dd['COD_UF_RESIDENCIA']]);
            cod_uf_nasc = -1 if columns[dd['COD_UF_NASCIMENTO']] == '' else int(columns[dd['COD_UF_NASCIMENTO']]);
            estado_civil = int(columns[dd['TP_ESTADO_CIVIL']]);
            etnia = int(columns[dd['TP_COR_RACA']]);
            cod_conclusao_EM = int(columns[dd['ST_CONCLUSAO']]);
            no_conclusao_EM = -1 if columns[dd['ANO_CONCLUIU']] == '' else int(columns[dd['ANO_CONCLUIU']]);
            tipo_escola_EM = -1 if columns[dd['TP_ESCOLA']] == '' else int(columns[dd['TP_ESCOLA']]);
            tipo_ens_escola_EM = -1 if columns[dd['IN_TP_ENSINO']] == '' else int(columns[dd['IN_TP_ENSINO']]);
            cod_escola = -1 if columns[dd['COD_ESCOLA']] == '' else int(columns[dd['COD_ESCOLA']]);
            values = (inscricao,idade,sexo,cod_nacionalidade,cod_municipio_resid,cod_municipio_nasc,cod_uf_resid,cod_uf_nasc,estado_civil,etnia, cod_conclusao_EM, no_conclusao_EM, tipo_escola_EM, tipo_ens_escola_EM, cod_escola);
            ret = values;
        except Exception as e:
            logger.error("Estudante: Exception during get values from columns: {}".format(e));
            ret = None;
        return ret;
