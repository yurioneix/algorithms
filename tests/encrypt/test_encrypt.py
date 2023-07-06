import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    "Ao passar um tipo invalido como parametro, retorna um erro"
    with pytest.raises(TypeError):
        encrypt_message("german", "cano")

    "Ao passar uma key que nao existe na string, retorna a string invertida"
    assert encrypt_message("fluminense", 12) == "esnenimulf"

    "Retorna a string invertida na parte um e dois concatenados por _"
    assert encrypt_message("fluminense", 5) == "imulf_esnen"
