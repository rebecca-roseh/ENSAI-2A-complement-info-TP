from business_object.pokemon.abstract_pokemon import Pokemon


class AttackerPokemon(Pokemon):

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multplier related to the attacker type.

        Returns :
            float: the multiplier
        """
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier
