import pilasengine
pilas = pilasengine.iniciar()
#pilas.fondos.Selva()
cantidad_vidas = 3
# puntaje = pilas.actores.Puntaje(color='blanco')
puntajes=[]
nombre=''

def reiniciar():

    global puntaje

    # Obtiene todos los actores de la pantalla.
    # actores = pilas.actores.listar_actores()
    #
    # # Elimina todos los actores excepto el fondo y el puntaje
    # for actor in actores:
    #    if actor not in [puntaje, pilas.escena.fondo]:
    #        actor.eliminar()

    # Cambio de escena
    pilas.escenas.Normal()
    pilas.fondos.Selva()

    #puntaje = pilas.actores.Puntaje(color='blanco')
    puntaje.x = -300
    puntaje.y = 220

    print str(puntaje.obtener())
    vidas ()

    # Genera una pregunta nueva
    crear_una_nueva_pregunta()

def vidas():

    global numvidas
    global cantidad_vidas

    #VIDA
    vida = pilas.actores.Texto("Vidas:")
    vida.x = -250
    vida.y = -170

    numvidas = pilas.actores.Puntaje()
    numvidas.definir(cantidad_vidas)
    numvidas.x = -200
    numvidas.y = -170

def crear_una_nueva_pregunta():

    global cantidad_vidas

    #PREGUNTA
    pilas.fondos.Selva()
    preg1 = pilas.azar(0,20)
    preg2 = pilas.azar(0,20)
    pregunta = pilas.actores.Texto("Cuanto es: " + str(preg1) + " + " + str(preg2),
                y=180,magnitud=25)

    #DEFINO LAS CAJAS
    caja1 = pilas.actores.Actor(x = -200, y = 70)
    caja1.imagen = "caja.png"
    caja1.escala = 2
    caja1.esverdadera = False

    caja2 = pilas.actores.Actor(x = 0, y = 70)
    caja2.imagen = "caja.png"
    caja2.escala = 2
    caja2.esverdadera = False

    caja3 = pilas.actores.Actor(x = 200, y = 70)
    caja3.imagen = "caja.png"
    caja3.escala = 2
    caja3.esverdadera = False

    #DEFINO RESPUESTAS
    rta_1 = pilas.actores.Texto("",x=-200, y=70)
    rta_2 = pilas.actores.Texto("",x = 0, y = 70)
    rta_3 = pilas.actores.Texto("",x = 200, y = 70)

    #CAJA VERDADERA
    cajas_posibles = [caja1,caja2,caja3]
    textos_posibles = [rta_1,rta_2,rta_3]
    indiceok = pilas.azar(0,2)
    respuesta_verdadera = cajas_posibles[indiceok]
    respuesta_verdadera.esverdadera = True
    texto_de_respuestaok = textos_posibles[indiceok]
    texto_de_respuestaok.texto = str(preg1+preg2)

    #CAJAS FALSAS
    if caja1.esverdadera:
        rta_2.texto = str(pilas.azar(0,100))
        rta_3.texto = str(pilas.azar(0,100))
    elif caja2.esverdadera:
            rta_1.texto = str(pilas.azar(0,100))
            rta_3.texto = str(pilas.azar(0,100))
    elif caja3.esverdadera:
            rta_1.texto = str(pilas.azar(0,100))
            rta_2.texto = str(pilas.azar(0,100))

    #EL MONO
    mono = pilas.actores.Mono(x=200,y=-150)
    mono.aprender(pilas.habilidades.Arrastrable)

    #COLISIONES
    cajas = [caja1,caja2,caja3]
    pilas.colisiones.agregar(mono,cajas,respuesta)

def respuesta(mono, caja):
    global cantidad_vidas
    global puntaje

    if caja.esverdadera:
        mono.decir("MUY BIEN")

        # Genera una estrella para mostrar que contesto bien
        estrella = pilas.actores.Estrella()
        estrella.x = caja.x
        estrella.y = caja.y
        estrella.escala = 0.2
        estrella.escala = [2, 1] * 2

        # Aumenta el puntaje
        puntaje.aumentar()

        # Reinicia el juego pasados los 2 segundos.
        pilas.tareas.una_vez(2, reiniciar)
    else:
        mono.decir("CUALQUIERA")
        cantidad_vidas -= 1
        numvidas.eliminar()
        vidas()
        pilas.camara.vibrar()
        caja.eliminar()
        if cantidad_vidas==0:
            morir()

def iniciar_juego():
    global nombre
    # global puntaje
    # pilas.escenas.Normal()
    # pilas.fondos.Selva()

    nombre=raw_input("Ingrese su nombre: ")
    reiniciar()

def ayuda():
    global cantidad_vidas
    global puntaje
  # Obtiene todos los actores de la pantalla
    actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
    for actor in actores:
        if actor not in [puntaje, pilas.escena.fondo]:
            actor.eliminar()

    pilas.escenas.Normal()
    pilas.fondos.Selva()

    texto_ayuda=pilas.actores.Texto('Arrastra el mono hasta \nla respuesta que creas correcta',x=-100,y=-100)
    volverayuda = pilas.actores.Menu(
        [
            ('Empezar el juego', reiniciar)
        ])
    volverayuda.x = -200
    volverayuda.y = -200

    preg1 = pilas.azar(0,20)
    preg2 = pilas.azar(0,20)
    pregunta = pilas.actores.Texto("Cuanto es: " + str(preg1) + " + " + str(preg2),
                y=180,magnitud=25)

    #DEFINO LAS CAJAS
    caja1 = pilas.actores.Actor(x = -200, y = 70)
    caja1.imagen = "caja.png"
    caja1.escala = 2
    caja1.esverdadera = False

    caja2 = pilas.actores.Actor(x = 0, y = 70)
    caja2.imagen = "caja.png"
    caja2.escala = 2
    caja2.esverdadera = False

    caja3 = pilas.actores.Actor(x = 200, y = 70)
    caja3.imagen = "caja.png"
    caja3.escala = 2
    caja3.esverdadera = False

    #DEFINO RESPUESTAS
    rta_1 = pilas.actores.Texto("",x=-200, y=70)
    rta_2 = pilas.actores.Texto("",x = 0, y = 70)
    rta_3 = pilas.actores.Texto("",x = 200, y = 70)

    #CAJA VERDADERA
    cajas_posibles = [caja1,caja2,caja3]
    textos_posibles = [rta_1,rta_2,rta_3]
    indiceok = pilas.azar(0,2)
    respuesta_verdadera = cajas_posibles[indiceok]
    respuesta_verdadera.esverdadera = True
    texto_de_respuestaok = textos_posibles[indiceok]
    texto_de_respuestaok.texto = str(preg1+preg2)

    #CAJAS FALSAS
    if caja1.esverdadera:
        rta_2.texto = str(pilas.azar(0,100))
        rta_3.texto = str(pilas.azar(0,100))
    elif caja2.esverdadera:
            rta_1.texto = str(pilas.azar(0,100))
            rta_3.texto = str(pilas.azar(0,100))
    elif caja3.esverdadera:
            rta_1.texto = str(pilas.azar(0,100))
            rta_2.texto = str(pilas.azar(0,100))

    #ACA EL MONO
    mono = pilas.actores.Mono(x=200,y=-150)
    mono.aprender(pilas.habilidades.Arrastrable)

    #COLISIONES
    cajas = [caja1,caja2,caja3]
    pilas.colisiones.agregar(mono,cajas,respuesta1)


def respuesta1(mono, caja):
    if caja.esverdadera:
        mono.decir("MUY BIEN")

        # Genera una estrella para mostrar que contesto bien
        estrella = pilas.actores.Estrella()
        estrella.x = caja.x
        estrella.y = caja.y
        estrella.escala = 0.2
        estrella.escala = [2, 1] * 2

    else:
        mono.decir("CUALQUIERA")
        pilas.camara.vibrar()
        caja.eliminar()

def salir_del_juego():
    pilas.terminar()

def morir():
    global nombre
    global cantidad_vidas
    global puntaje

    cantidad_vidas = 3
    jugador=[nombre,puntaje.obtener()]
    puntajes.append(jugador)
    i=0
    puntaje.definir(i)
       # Obtiene todos los actores de la pantalla.
    actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
    for actor in actores:
        if actor not in [puntaje, pilas.escena.fondo]:
            actor.eliminar()
    pilas.fondos.Selva()

    menusecundario()

def mostrar_puntajes():

     # Obtiene todos los actores de la pantalla.
    actores = pilas.actores.listar_actores()

    # Elimina todos los actores excepto el fondo y el puntaje
    for actor in actores:
        if actor not in [pilas.escena.fondo]:
            actor.eliminar()
    pilas.escenas.Normal()
    pilas.fondos.Selva()

    volverayuda = pilas.actores.Menu([('Volver al menu', menuprincipal)])
    volverayuda.x = -200
    volverayuda.y = -200

    valor_y = 100
    pilas.actores.Texto("Puntajes",x=0,y=200)
    for jugador in puntajes:
        pilas.actores.Texto(jugador[0],x=-100,y=valor_y)
        pilas.actores.Texto(str(jugador[1]),x=100,y=valor_y)
        valor_y = valor_y - 30

def menuprincipal():
    # global puntaje

    pilas.escenas.Normal()
    pilas.fondos.Selva()
    # Obtiene todos los actores de la pantalla.
    # actores = pilas.actores.listar_actores()
    #
    # # Elimina todos los actores excepto el fondo y el puntaje
    # for actor in actores:
    #     if actor not in [puntaje, pilas.escena.fondo]:
    #         actor.eliminar()
    # pilas.fondos.Selva()
    # print nombre
    # print puntajes

    # puntaje = pilas.actores.Puntaje(color='blanco')
    # puntaje.x = -300
    # puntaje.y = 220

    menu1 =pilas.actores.Menu([('Iniciar juego', iniciar_juego), ('Puntajes', mostrar_puntajes), ('Ayuda', ayuda), ('Salir', salir_del_juego),])
    menu1.x = 0
    menu1.escala = 1.0
    menu1.rotacion = 0

    mono = pilas.actores.Mono()
    mono.x = 0
    mono.y = 100
    mono.escala = 1.0
    mono.rotacion = 0

def menusecundario():

    volverajugar = pilas.actores.Menu([('Game Over \n Volver a jugar', menuprincipal)])
    volverajugar.escala=2
    volverajugar.x = 0
    volverajugar.y = 0

menuprincipal()
pilas.ejecutar()
