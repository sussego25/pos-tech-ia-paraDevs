from models.dengue_parametros import DengueFeatures


class PrevisaoDengueService:
    def __init__(self, model, features:DengueFeatures ):
        self.model = model
        self.features = features

    def predict(self):
        prediction = self.model.predict([list(self.features.__dict__.values())])
        has_dengue = bool(prediction[0])
        return self.__format_prediction(has_dengue)

    def __format_prediction(self, has_dengue:bool):
        description = "Paciente provavelmente não tem dengue"
        if has_dengue:
            description = "Paciente provavelmente tem dengue !!!"
        return {
                "tem_dengue": has_dengue,
                "descricao": description
            }