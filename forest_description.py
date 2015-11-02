class ForestDescription:
    def __init__(self, descriptions):
        self.descriptions = [desc1, desc2, desc3, desc4, desc5, desc6, desc7, desc8, desc9, desc10]

        desc1 = """You are in the forest"""
        desc2 = """You are in the forest"""
        desc3 = """You are in the forest"""
        desc4 = """You are in the forest"""
        desc5 = """You are in the forest"""
        desc6 = """You are in the forest"""
        desc7 = """You are in the forest"""
        desc8 = """You are in the forest"""
        desc9 = """You are in the forest"""
        desc10 = """You are in the forest"""

    def description(self):
        desc = random.choice(self.descriptions)

        print desc
