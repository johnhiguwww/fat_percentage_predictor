from flask import Flask, request, render_template
from tools.exercise import ExercisePrediction
import os

# Cria a app
app = Flask(__name__)

# Página de entrada
@app.route("/")
def index():
    result = None
    return render_template("index.html", result=result)

# Página com resultado da previsão
@app.route("/estimate", methods=["POST"])
def estimate():
    try:
        # Capturar os dados do formulário
        duration = request.form.get('duration')
        workout_type = request.form.get('workout_type')
        gender = request.form.get('gender')
        
        # Validar entradas
        if not duration or not workout_type or not gender:
            return render_template("index.html", result="Por favor, preencha todos os campos.")
        
        # Criar instância da classe
        exercise_data = {'duration': duration, 'workout_type': workout_type, 'gender': gender}
        exercise = ExercisePrediction(exercise_data)
        
        # Preparar e prever
        prepared_data = exercise.prepare()
        result = exercise.predict(prepared_data)
        
        # Formatar resultado
        result = f"O percentual de gordura gasto estimado é: {result:.2f}%"
        return render_template('index.html', result=result)
    except Exception as e:
        return render_template("index.html", result=f"Erro ao processar: {e}")
# Rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
