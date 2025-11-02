def userEntidade(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "nome": db_item["nome"],
        "email": db_item["email"],
        "senha": db_item["senha"],
    }

def listaUserEntidade (db_items) -> list:
    return [userEntidade(item) for item in db_items]