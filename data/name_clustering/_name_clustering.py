from collections import defaultdict

from . import ifuzzy


def cluster_names(names, hash_type=ifuzzy.types.DMetaphone):
    phonetic_hash_to_names = defaultdict(set)
    for name in names:
        phonetic_hashes = ifuzzy.phonetic_hash(name, hash_type)
        for phonetic_hash in phonetic_hashes:
            if phonetic_hash is not None:
                phonetic_hash_to_names[phonetic_hash].add(name)
            break

    unique_clusters = set(
        tuple(sorted(list(clustered_names)))
        for _, clustered_names in phonetic_hash_to_names.iteritems()
    )

    name_to_clusters = defaultdict(list)
    for clustered_names in unique_clusters:
        for name in clustered_names:
            name_to_clusters[name].extend(clustered_names)

    return name_to_clusters
