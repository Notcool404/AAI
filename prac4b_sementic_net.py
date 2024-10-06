class SemanticNetwork:
    def __init__(self):
        self.network = {}

    def add_concept(self, concept):
        if concept not in self.network:
            self.network[concept] = {'is_a': [], 'has_a': []}

    def add_relation(self, relation, concept1, concept2):
        self.add_concept(concept1)
        self.add_concept(concept2)
        self.network[concept1][relation].append(concept2)

    def get_relations(self, concept):
        return self.network.get(concept, {})
    
    def display_network(self):
        for concept, relations in self.network.items():
            print(f"Concept: {concept}")

            for relation, related_concepts in relations.items():
                for related_concept in related_concepts:
                    print(f" {relation} -> {related_concept}")

if __name__ == "__main__":
    sn = SemanticNetwork()
    
    # Adding concepts and relations
    sn.add_concept("Animal")
    sn.add_concept("Bird")
    sn.add_concept("Mammal")
    sn.add_concept("Penguin")
    sn.add_concept("Canary")
    sn.add_relation("is_a", "Bird", "Animal")
    sn.add_relation("is_a", "Mammal", "Animal")
    sn.add_relation("is_a", "Penguin", "Bird")
    sn.add_relation("is_a", "Canary", "Bird")
    sn.add_relation("has_a", "Bird", "Wings")
    sn.add_relation("has_a", "Canary", "Yellow_Feathers")
    # Displaying the network
    sn.display_network()