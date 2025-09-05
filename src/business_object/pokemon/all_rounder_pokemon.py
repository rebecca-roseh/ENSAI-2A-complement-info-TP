from business_object.pokemon.abstract_pokemon import Pokemon


class AllRounderPokemon(Pokemon):

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multplier related to the attacker type.

        Returns :
            float: the multiplier
        """
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
