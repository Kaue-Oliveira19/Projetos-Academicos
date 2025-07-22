from flask import Flask, request, jsonify, render_template
from carbon_calculator import calcular_carbono_alimentar

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza o arquivo HTML da página principal
    return render_template('Index.html')

@app.route('/contato')
def contato():
    # Renderiza o arquivo HTML da página contato
    return render_template('Contato.html')

@app.route('/mapa')
def mapa_site():
    # Renderiza o arquivo HTML da página do Mapa do Site
    return render_template('MapaSite.html')

@app.route('/calcular', methods=['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        # Coleta os parâmetros para o formulário
        carne_bovina = float(request.form.get('carne_bovina', 0))
        frango = float(request.form.get('frango', 0))
        peixe = float(request.form.get('peixe', 0))
        carne_suina = float(request.form.get('carne_suina', 0))
        cafe = float(request.form.get('cafe', 0))
        ovos = float(request.form.get('ovos', 0))
        leite = float(request.form.get('leite', 0))
        agua = float(request.form.get('agua', 0))
        arroz = float(request.form.get('arroz', 0))

        # Calcula a pegada de carbono com base nos alimentos
        resultado = calcular_carbono_alimentar(carne_bovina, frango, peixe, carne_suina, cafe, ovos, leite, agua, arroz)

        # Retorna o resultado na página de cálculo
        return render_template('Index.html', total_carbono=resultado['total_carbono'], creditos_carbono=resultado['creditos_carbono'])

    # Caso seja GET, exibir a página sem resultado
    return render_template('Index.html')

if __name__ == '__main__':
    app.run(debug=True)
