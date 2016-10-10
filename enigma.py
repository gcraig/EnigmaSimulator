#
# Enigma 1 1930 Simulator 
# georgeacraig@gmail.com
#
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Reflectors

reflector_a = "EJMZALYXVBWFCRQUONTSPIKHGD"
reflector_b = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector_c = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
# thin_reflector_b = "ENKQAUYWJICOPBLMDXZVFTHRGS"
# thin_reflector_c = "RDOBJNTKVEHMLFCWZAXGYIPSUQ"

# Table Rotors Enigma 1 1930

rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
          
# Table Notches

rotor_1_tn = "QQ" # If rotor steps from Q to R, the next rotor is advanced
rotor_2_tn = "EE" # If rotor steps from E to F, the next rotor is advanced
rotor_3_tn = "VV" # If rotor steps from V to W, the next rotor is advanced