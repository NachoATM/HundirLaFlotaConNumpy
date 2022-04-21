# Hundir La Flota Con Numpy

![Agua-tocado-o-hundido-974x1024](https://user-images.githubusercontent.com/98879159/164447526-1a4eec98-9688-4bf8-bd3f-b3eae8a22417.jpg)

## ¿Qué es?

He creado mi propio juego de **Hundir la flota** en Python.
Para el desarrollo del mismo, he necesitado la librería *numpy*, módulos, bucles, funciones, clases y colecciones de Python.

## ¿Cómo funciona el juego?

1. Hay dos jugadores: tú y la máquina
2. Un **tablero de 10 x 10** posiciones donde irán los barcos
3. Lo primero que se hace es colocar los barcos. Para este juego **los barcos se colocan de manera aleatoria. 
4. Los barcos son:
    - 4 barcos de 1 posición de eslora
    - 3 barcos de 2 posiciones de eslora
    - 2 barcos de 3 posiciones de eslora
    - 1 barco de 4 posiciones de eslora
5. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.
6. Funciona por turnos y empiezas tú.
7. En cada turno disparas a una coordenada (X, Y) del tablero adversario. **Si aciertas, te vuelve a tocar**. En caso contrario, le toca a la máquina.
8. En los turnos de la máquina, si acerta también le vuelve a tocar. ¿Dónde dispara la maquina? A un punto aleatorio en tu tablero.
9. Si se hunden todos los barcos de un jugador, el juego acaba y gana el otro.
