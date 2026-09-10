def verificar_grupo(usuario, grupo):
    if not usuario.is_authenticated:
        return False

    return usuario.groups.filter(name=grupo).exists()
