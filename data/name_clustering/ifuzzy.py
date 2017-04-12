import fuzzy
import enum


class types(enum.IntEnum):
    Soundex = 1
    DMetaphone = 2
    nysiis = 3


_types_to_function = {
    types.Soundex: fuzzy.Soundex,
    types.DMetaphone: fuzzy.DMetaphone(10),
    types.nysiis: fuzzy.nysiis,
}


def phonetic_hash(name, hash_type):
    """name (str)"""
    phonetic_hash = _types_to_function[hash_type](name)
    if not isinstance(phonetic_hash, list):
        phonetic_hash = [phonetic_hash]
    return phonetic_hash
