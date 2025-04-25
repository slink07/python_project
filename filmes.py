'''4. Desafio do Módulo
Crie um mini sistema de recomendação de filmes baseado em preferências simples do usuário.
Requisitos:
O usuário informa se gosta de ação, comédia ou drama.
O sistema recomenda filmes com base nessas preferências.'''
'''
Melhore o sistema permitindo que o usuário avalie os filmes recomendados e, com base nessas avaliações, refine as recomendações futuras.'''



pergunta = input('Qual o seu gênero favorito (ação, comédia, drama)? ')




recomendações = {
    "ação": ["Mad Max", "John Wick", "Vingadores"],
    "comédia": ["Superbad", "As Branquelas", "Se Beber, Não Case"],
    "drama": ["À Espera de um Milagre", "Clube da Luta", "Forrest Gump"]
}
# avaliação da recomendação


def avaliação():
    nota = int(input('Qual nota voce dá para as recomendações? (1-5)  '))
    if nota == 5:
        print('Que legal que voçê gostou das recomendações!')
    elif nota <= 4:
        print('Iremos melhorar nossas recomendações para voçê!')


if pergunta in recomendações:
    print(f"filmes recomendados de {pergunta}: {", ".join(recomendações[pergunta])}")
    

else:
    print('recomendação nao encontrado, tente outro')
    pergunta = input('Qual o seu gênero favorito (ação, comédia, drama)? ')
    

    


avaliação()



