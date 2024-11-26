import joblib
import numpy as np
import os

class ExercisePrediction:
    # Mapeamento para o tipo de exercício
    workout_mapping = {'Cardio': 0, 'Strength': 1, 'Yoga': 2, 'HIIT': 3}
    gender_mapping = {'male': 0, 'female': 1}

    def __init__(self, exercise_data):
        """
        Inicializa a classe com os dados fornecidos pelo usuário.
        :param exercise_data: Dicionário contendo os dados:
            - 'duration': duração do exercício em minutos
            - 'workout_type': tipo de exercício
            - 'gender': gênero do usuário
        """
        self.exercise_data = exercise_data

    def prepare(self):
        """
        Prepara os dados de entrada para o modelo.
        """
        # Inicializar vetor com tamanho esperado (ajustar conforme necessário)
        result = np.zeros(4)  # Ajuste conforme o número de features no seu modelo

        # Preencher com dados mapeados
        result[0] = float(self.exercise_data['duration'])  # Duração do exercício
        result[1] = self.workout_mapping.get(self.exercise_data['workout_type'], -1)  # Tipo de exercício
        result[2] = self.gender_mapping.get(self.exercise_data['gender'].lower(), -1)  # Gênero

        # Validar se todos os mapeamentos foram encontrados
        if -1 in result:
            raise ValueError("Entrada inválida nos dados fornecidos.")
        
        return result

    def predict(self, prepared_data):
        """
        Realiza a previsão com base nos dados preparados.
        """
        # Escolher o modelo com base no gênero
        if self.exercise_data['gender'].lower() == 'male':
            #model_male = joblib.load('./modelo/modelo_male.pkl')
            model = joblib.load('/modelo/model_male.pkl')
            prediction = model.predict([prepared_data])
            return prediction[0]
        elif self.exercise_data['gender'].lower() == 'female':
            model = joblib.load('./modelo/model_female.pkl')

            prediction = model.predict([prepared_data])
            return prediction[0]
        else:
            raise ValueError("Gênero inválido. Escolha 'male' ou 'female'.")

        # Fazer previsão
        #prediction = model.predict([prepared_data])
        #return prediction[0]
