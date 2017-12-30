from flask import Flask, render_template,request,jsonify
from classes.Estudante import *
from classes.ProvaObjetiva import *
from classes.ProvaRedacao import *

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

import sys

reload(sys)
sys.setdefaultencoding('utf8')

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/algoritmos')
def alg():
    charts = get_chart_list()
    return render_template('algoritmos.html',charts = charts)

@app.route('/estados')
def est():
    return render_template('estados.html')

@app.route('/pesquisar')
def pesquisa():
    a = request.args.get('a')
    print 'entrou flask',a
    out = None
    if out:
        out = search_school_list(out)
    else:
        out = [-1,'Not Found... =|']
    return jsonify(result=out)

@app.route('/sort_alunos')
def sort():
    a = request.args.get('a')
    print 'entro jquery alunos',a
    out = sort_alunos(a)
    return jsonify(result=out)

@app.route('/pesquisar_cidade')
def pesquisa_cidade():
    a = request.args.get('a')
    print 'entrou flask',a
    out = None
    if out:
        out = search_city_list(out)
    else:
        out = [-1,'Not Found... =|']
    return jsonify(result=out)

@app.route('/busca')
def busca():
    return render_template('busca.html')

@app.route('/cidades')
def busca_cidade():
    return render_template('busca_cidade.html')

@app.route('/uf')
def uf():
    a = request.args.get('a')
    out = soma(a,b)
    return render_template('uf.html')

@app.route('/cidade/<mun>')
def cidade(mun):
    out = busca_mun(mun)
    municipio = out[0]
    lista_alunos = out[1]
    lista_escolas = out[2]
    l = []
    for escola in lista_escolas:
        e = busca_escola(escola)
        l.append(e)
    return render_template('cidade.html',municipio=municipio,lista_alunos=lista_escolas,lista_escolas=l)

@app.route('/escola/<cod>')
def escola(cod):
    escola = busca_escola(cod)
    out = busca_alunos_por_escola(cod)
    alunos = sorted(out[0], key=lambda x: x.media, reverse=True)
    graph = gera_grafico(out[1],out[2])
    municipio = busca_municipio(escola.municipio)
    return render_template('escola.html',escola=escola,alunos=alunos,municipio=municipio,graph=graph)

@app.route('/firebase')
def bases():
    return render_template('firebase.html')

@app.route('/map/<est>')
def map(est):
    info = define_map(est)
    if info[1] == 'ChIJq7dMA7UaRYkRTcp63_PsALY':
        parametros = []
    else:
        parametros = consulta_db(est)
    return render_template('map.html',est=est,info=info,pam=parametros)

@app.route('/aluno',methods=['GET', 'POST'])
def aluno():
    num_inscricao = request.form['num']
    if num_inscricao:
        num_inscricao = int(num_inscricao) + 140000000000;
        aluno = Estudante.findByCod(num_inscricao);
        provaobjetiva = ProvaObjetiva.findByCod(num_inscricao);
        provaredacao = ProvaRedacao.findByCod(num_inscricao);
        return render_template('new_aluno.html',aluno=aluno, provaobjetiva=provaobjetiva, provaredacao=provaredacao);
    else:
        return render_template('new_aluno.html');
@app.route('/admin')
def admin():
    header=None
    return render_template('adm.html', header=header);

@app.route('/admin', methods=['POST'])
def admin_post():
    csvFile = request.files['csvfile'];
    csvSeparator = request.form['csvseparator'];
    if csvFile:
        header = csvFile.readline();
        header = header.split(csvSeparator);
    return render_template('adm.html', header=header);

if __name__ == '__main__':
    app.run()
