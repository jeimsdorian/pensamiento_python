def busca_pais(paises, pais):
    &quot;&quot;&quot;
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    &quot;&quot;&quot;
    
    try:
        return paises[pais]
    except KeyError:
        return None
