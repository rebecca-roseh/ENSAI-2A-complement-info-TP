from business_object.pokemon.abstract_pokemon import Pokemon


class DefenderPokemon(Pokemon):
    def __innit__(self):
        super().__innit__()

    def get_pokemon_defender_coef(self) -> float:
        """
        Compute a damage multplier related to the attacker type.

        Returns :
            float: the multiplier
        """
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
