laberinto= [
    [0,1,1,0],
    [0,0,0,0],
    [0,1,1,0],
    [0,0,0,0],
]

def buscar_caminos(laberinto,coordenada,salida,camino,respuesta):

    cola = [(coordenada,[])]
    while(len(cola)!=0):
        camino = cola.pop(0)
        x,y = camino[0][0],camino[0][1]
        if (x>=0 and x<len(laberinto)) and (y>=0 and y<len(laberinto[0])) and (not(camino[0] in camino[1]) and laberinto[x][y] != 1):
            camino[1].append(camino[0])
            if(camino[0] == salida):
                respuesta.append(camino[1])
            else:
                for nx,ny in[(1,0),(-1,0),(0,1),(0,-1)]:
                    newcamino= ((x + nx, y + ny),camino[1].copy()) 
                    cola.append(newcamino)

#Poner los datos aquí
#------------------------
coordenada = (0,0)
salida = (3,3)
#------------------------

camino = []
respuesta = []

buscar_caminos(laberinto, coordenada, salida, camino, respuesta)
for index,i in enumerate(respuesta):
    print(f"Camino #{index+1}:\n{i}\n")