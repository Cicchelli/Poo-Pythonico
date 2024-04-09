from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro(
        titulo="Hary Potter e a Pedra Filosofal",
        autor="J.K. Rowling",
        paginas=300,
    )
    assert livro.titulo == "Hary Potter e a Pedra Filosofal"
    assert livro.autor == "J.K. Rowling"
    assert livro.paginas == 300
