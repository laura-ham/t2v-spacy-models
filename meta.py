class Meta:
    def __init__(self, model):
        self.meta_info = model.meta

    def get(self):
        return {
            'name': self.meta_info["name"],
            'language': self.meta_info["lang"]
        }
