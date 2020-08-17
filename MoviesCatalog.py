import sys
import csv
from time import process_time 
movies=[]
def newCatalog (file, lst, sep=";"):
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def addMovie (movie:tuple):
    movies.append(movie)
def topVoted (movies:list):
    top=0
    topnombre=""
    counter=(len(movies)-1)
    while counter>=0:
        e=dict(movies[counter])
        c=int(e["vote_count"])
        if c>=top:
            topnombre=e["original_title"]
            top=c
        counter-=1
    counter=(len(movies)-1)
    while counter>=0:
        i=dict(movies[counter])
        i=int(i["vote_count"])
        if i==top:
            movies.pop(counter)
        counter-=1
    return [topnombre,top]
def topAverageVoted (movies:list):
    top=0
    topnombre=""
    counter=(len(movies)-1)
    while counter>=0:
        e=dict(movies[counter])
        c=int(e["vote_average"])
        if c>=top:
            topnombre=e["original_title"]
            top=c
        counter-=1
    counter=(len(movies)-1)
    while counter>=0:
        i=dict(movies[counter])
        i=int(i["vote_average"])
        if i==top:
            movies.pop(counter)
        counter-=1
    return [topnombre,top]
def worstVoted (movies:list):
    top=1000000
    topnombre=""
    counter=(len(movies)-1)
    while counter>=0:
        e=dict(movies[counter])
        c=int(e["vote_count"])
        if c<=top:
            topnombre=e["original_title"]
            top=c
        counter-=1
    counter=(len(movies)-1)
    while counter>=0:
        i=dict(movies[counter])
        i=int(i["vote_count"])
        if i==top:
            movies.pop(counter)
        counter-=1

    return [topnombre,top]
def worstAverageVoted (movies:list):
    top=1000000
    topnombre=""
    counter=(len(movies)-1)
    while counter>=0:
        e=dict(movies[counter])
        c=int(e["vote_average"])
        if c<=top:
            topnombre=e["original_title"]
            top=c
        counter-=1
    counter=(len(movies)-1)
    while counter>=0:
        i=dict(movies[counter])
        i=int(e["vote_average"])
        if i==top:
            movies.pop(counter)
        counter-=1
    return [topnombre,top]
def ranking_movies(movies:list, numero:int, tipo:str, orden:str):
    rankingmejor=[]
    rankingpeor=[]
    numero=int(numero)
    if "COUNT"==tipo:
        counter=int(numero)
        while (counter-1)!=(-1):
            mejor=topVoted(movies)
            rankingmejor.append(mejor)
            counter-=1
        counter=numero
        while (counter-1)!=-1:
            peor=worstVoted(movies)
            rankingpeor.append(peor)
            counter-=1
    if "AVERAGE"==tipo:
        counter=numero
        print(counter)
        while (counter-1)!=-1:
            mejor=topAverageVoted(movies)
            rankingmejor.append(mejor)
            counter-=1
        counter=numero
        while (counter-1)!=-1:
            peor=worstAverageVoted(movies)
            rankingpeor.append(peor)
            counter-=1
    if "ASCENDENTE"==orden:   
        rankingmejor.reverse()
    if "DESCENDENTE"==orden:
        rankingpeor.reverse()    
    return rankingmejor, rankingpeor
def rankingbygenre(movies:list, numero:int, tipo:str, orden:str, genero:str):
    genre=[]
    for i in movies:
        e=dict(i)
        if genero in i["genres"] :
            genre.append(i)
    rankingmejor=[]
    rankingpeor=[]
    if "COUNT"==tipo:
        counter=numero
        while (counter-1)!=-1:
            mejor=topVoted(genre)
            rankingmejor.append(mejor)
            counter-=1
        counter=numero
        while (counter-1)!=-1:
            peor=worstVoted(genre)
            rankingpeor.append(peor)
            counter-=1
    if "AVERAGE"==tipo:
        counter=numero
        while (counter-1)!=-1:
            mejor=topAverageVoted(genre)
            rankingmejor.append(mejor)
            counter-=1
        counter=numero
        while (counter-1)!=-1:
            peor=worstAverageVoted(genre)
            rankingpeor.append(peor)
            counter-=1
    if "ASCENDENTE"==orden:   
        rankingmejor.reverse()
    if "DESCENDENTE"==orden:
        rankingpeor.reverse()
    return rankingmejor, rankingpeor

def req_3(nombre_director:str,movies:list,movies_casting:list)->tuple:
    id_movie=[]
        
    for i in range(len(movies_casting)):
        d=dict(movies_casting[i])
        if nombre_director in d["director_name"]:
            id_movie.append(d["id"])
            peliculas=[]
            suma=0
    for i in range(len(movies)):
        for j in range(len(id_movie)):
           if id_movie[j]==movies[i]["id"]:
                peliculas.append(movies[i]["title"])
                suma+=float(movies[i]["vote_average"])

    return (peliculas,id_movie,suma/(len(id_movie)))
    

def req_5(nombre_genero:str,movies:list)->tuple:
    peliculas=[]
    id_movie=[]
    suma=0
    for i in range(len(movies)):
        if nombre_genero in movies[i]["genres"]:
            peliculas.append(movies[i]["title"])
            id_movie.append(movies[i]["id"])
            suma+=float(movies[i]["vote_average"])
    return(peliculas,id_movie,suma/len(peliculas))
def actores(nombre_actor:str, archivo_casting:list,archivo_peliculas:list)->tuple:
    id_movie=[]
    directores={}
    for i in range(len(archivo_casting)):
        if nombre_actor in archivo_casting[i]["actor1_name"]:
            id_movie.append(archivo_casting[i]["id"])
            if archivo_casting[i]["director_name"] not in directores:
                    directores[archivo_casting[i]["director_name"]]=1
            if archivo_casting[i]["director_name"] in directores:
                    directores[archivo_casting[i]["director_name"]]+=1
    director=0
    nombre_director=""
    for i in directores.keys():
        if directores[i]>director:
            director=directores[i]
            nombre_director=i
        
    
    peliculas=[]
    suma=0
    for i in range(len(archivo_peliculas)):
        for j in range(len(id_movie)):
            if id_movie[j]==archivo_peliculas[i]["id"]:
                peliculas.append(archivo_peliculas[i]["title"])
                suma+=float(archivo_peliculas[i]["vote_average"])
    return (peliculas,id_movie,suma/len(id_movie),nombre_director)

def buenas_peliculas(movies:list, movies_casting:str, nombre_director:str)->tuple:
    id_movie=[]
    for i in range(len(movies_casting)):
        if nombre_director in movies_casting[i]["director_name"]:
            id_movie.append(movies_casting[i]["id"])
    n_peliculas=0
    suma=0
    for i in range(movies):
        for j in range(len(id_movie)):
            if id_movie[j]==movies[i]["id"] and float(movies[i]["vote_average"])>=6:
                n_peliculas+=1
                suma+=movies[i]["vote_average"]
    
    return (n_peliculas,suma/n_peliculas)
    
def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido, qué desea hacer?")
    print("1- Cargar datos ")
    print("2- Crear Ranking de películas")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género cinematográfico")
    print("6- Crear Ranking del género")
    print("7- Encontrar buenas peliculas")
    print("0- Salir")

def main():
    lista = []
    lista2= []
    while True:
        printMenu() 
        inputs =input('Seleccione una opción para continuar\n') 
        if int(inputs[0])==1:
            newCatalog("Data/MoviesCastingRaw-small.csv", lista) 
            newCatalog("Data/SmallMoviesDetailsCleaned.csv",lista2)
            print("Datos cargados, "+str(len(lista))+" elementos cargados ")
        elif int(inputs[0])==2: 
            numero=input("Ingrese el numero de peliculas para el ranking ")
            tipo=input("Ingrese el tipo de ranking(COUNT o AVERAGE) ")
            orden=input("Ingrese el orden que desea (ASCENDENTE O DESCENDENTE) ")
            print(ranking_movies(lista2,numero,tipo,orden))
        elif int(inputs[0])==3: 
            director=input("Ingrese el nombre del director que desea conocer ")
            print(req_3(director,lista2,lista))
        elif int(inputs[0])==5:
            genero=input("Ingrese el genero ")
            print(req_5(genero,lista2))
        elif int(inputs[0])==4:
            genero=input("Ingrese el nombre del actor ")
            print(actores(genero,lista,lista2))
        elif int(inputs[0])==0: 
            sys.exit(0)
main()
