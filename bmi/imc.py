class Imc():
    def __init__(self,  weight:float, height: float):
        self.weight = weight
        self.height = height
    
    def calculate_bmi(self):
        self.classification = {
            (0,18.5) : 'baixo peso',
            (18.5,24.9) : 'normal',
            (24.9,29.9) : 'sobrepeso',
            (29.9,34.9) : 'obesidade grau 1',
            (35,39.9) : 'obsidade grau 2',
            (39.9, 100) : 'obsidade extrema',
        }
        self.height = self.height / 100
        bmi:float = self.weight / (self.height ** 2)
        
        for bmi_class in self.classification.keys():
            if bmi > bmi_class[0] and bmi < bmi_class[1]:
                result = {
                    'bmi': bmi,
                    'classification' :self.classification[bmi_class]
                }
                return result