import tweepy
import random
import time
api = tweepy.Client(
    consumer_key='tXDwMRvDTLhypnuUx5nQ21eDK',
    consumer_secret='emgYaOyAUQ4cCIXmh3umCrHYRRN8JoOZc0I95KYZcG3J3uMFlz',
    access_token='1806444460806393857-rtrf5sVULkcnnQOPEeIRID3EzauBN7',
    access_token_secret='ijkjmICaAsKuYGWTmnYsAaEwjvPgfrVTgAgx0gnIJtMv8',

)

with open("seguidores-broxada.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    num = random.randint(0, 115)
    n = 0
    for linha in linhas: 
        n+=1
        if n==num:
            break
        nome = linha.strip()

print(nome)
tweet_text = f'@{"magalzaoshow"}, Hora do Lanche!'
tweet = api.create_tweet(text=tweet_text)
print(tweet)
"""try:
    tweet_text = f'@{}, Hora do Lanche!'
    tweet = api.create_tweet(tweet_text)
    print(tweet)
except:
    pass
"""