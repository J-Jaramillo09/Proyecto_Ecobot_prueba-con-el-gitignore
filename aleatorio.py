import random

#Función para los datos curiosos

def datos_curiosos():
    lista_datos = [
        " El vidrio puede tardar más de 4,000 años en descomponerse, pero es 100% reciclable infinitamente.",
        " Una pila puede tardar 1,000 años en degradarse y contaminar hasta 600,000 litros de agua.",
        " Una botella de plástico tarda hasta 450 años en degradarse; bolsas, entre 150 y 1,000 años.",
        " Una lata de aluminio tarda 200 años en descomponerse, pero reciclada vuelve a usarse en 2 meses.",
        " Un chicle tarda unos 5 años en degradarse.",
        " Reciclar una lata de aluminio ahorra energía para encender una bombilla 3 horas.",
        " Reciclar una tonelada de papel salva 17 árboles y reduce 74% la contaminación del aire.",
        " Cada año se vierten 6,000 millones de kg de basura al mar; mueren más de 1 millón de animales.",
        " La Gran Mancha de Basura del Pacífico es 7 veces más grande que España."
    ]

    return random.choice(lista_datos)
    
# Función para los consejos

def consejo_random():
    lista_consejos = [
    {
        "texto": "Separa residuos: Azul (papel), Amarillo (plástico), Verde (vidrio), Marrón (orgánicos).",
        "imagen": "https://i.postimg.cc/vHVKqVVb/Codigo-Colores-Contenedores.webp"  # Ejemplo ilustrativo
    },
    {
        "texto": "Aplica las 3R: Reduce, Reutiliza y Recicla.",
        "imagen": "https://i.postimg.cc/dthhzqsq/tres-r.jpg"
    },
    {
        "texto": "Residuos especiales: pilas, aceite y medicinas → llévalos a puntos limpios.",
        "imagen": "https://i.postimg.cc/cLZr6f7J/puntos-limpios.jpg"
    },
    {
        "texto": "Compra consciente: productos duraderos, a granel y locales.",
        "imagen": "https://i.postimg.cc/C1WK08LS/compra.jpg"
    },
    {
        "texto": "Ten un plan: espacio para reciclar e involucra a tu familia.",
        "imagen":"https://i.postimg.cc/MpdKTNKs/reciclaje-familiar.jpg"
    }
]

    return random.choice(lista_consejos)

# función para las botellas

def videos_botellas ():
    videos = [
        {
            "title": "2 Super Ideas con UNA SOLA BOTELLA PLÁSTICA",
            "url": "https://www.youtube.com/watch?v=X4AJ1--oyhA"
        },
        {
            "title": "GANA DINERO!!! 3 MANUALIDADES CON BOTELLAS",
            "url": "https://www.youtube.com/watch?v=3EtyOm775Jo"
        },
        {
            "title": "¡I CUT PLASTIC BOTTLE INTO 3 PARTS AND THIS ...",
            "url": "https://www.youtube.com/watch?v=l7wRJEhY33M"
        },
        {   
            "title":"PORTA BOLSAS útil y decorativo reciclando una botella de plástico - Diy Organizadores con reciclaje.",
             "url":"https://youtu.be/d2j8P6djLlA?si=B-V1Som97QhBZG2R"
        }
    ]
    return random.choice(videos)

#Función para las latas

def videos_latas ():
    videos = [
        {
            "title": "4 IDEAS PARA REUTILIZAR LATAS",
            "url": "https://youtu.be/kIs0fl8qJJc?si=5ASpNtFKpj5m-P13"
        },
        {
            "title": "ÚTIL Idea con LATAS De ATUN reciclada",
            "url": "https://youtu.be/bQTp6nv-fwU?si=zMTIpzI9Q_WvCdHv"
        },
        {
            "title": "10 Ideas con Anillas de Latas ",
            "url": "https://youtu.be/o8xknNRJlbg?si=5-FOcpnrO5XnaKT5"
        },
        {   
            "title":"LÁMPARA RECICLADA con ANILLAS de LATAS",
             "url":"https://youtu.be/GqHwo1eE3H4?si=GX5GPODouCcMVEgp"
        }
    ]
    return random.choice(videos)

# FUnción para cartón

def videos_carton ():
    videos = [
        {
            "title": "COMO HACER un TELEFERICO con MATERIALES CASEROS",
            "url": "https://youtu.be/sxiAAcUaBwk?si=9KDEh5ZTUmpZ1Pmv"
        },
        {
            "title": "hacer una lampara de escritorio usando carton reciclado",
            "url": "https://youtu.be/oQ1xT-3baLA?si=M1PbX85lU4NaFAey"
        },
        {
            "title": "COMO FAZER UM VENTILADOR INFINITO COM PAPELÃO ",
            "url": "https://youtu.be/_GOi3LHZB-U?si=rdusKoIxJHzIs9v6"
        },
        {   
            "title":"Como Hacer una Mano Robotica en tu Casa con Carton",
             "url":"https://youtu.be/ybFy-zyLYco?si=iY3A0dBJhC50PrDL"
        }
    ]
    return random.choice(videos)

# FUnción para vidrio

def videos_vidrio ():
    videos = [
        {
            "title": "IDEAS DE DECORACION DE BOTELLAS /COMO RECICLAR BOTELLAS DE VIDRIO",
            "url": "https://youtu.be/uEz6c_YbtJM?si=ky6OZj-60UB4IRLA"
        },
        {
            "title": "Botella de arte con uvas y barril ",
            "url": "https://youtu.be/3JmDNJBu3AQ?si=wzcrs87Gw_sdJL8I"
        },
        {
            "title": "Awesome Bottle House",
            "url": "https://youtu.be/osXz0tuILwQ?si=M98yO9Xc-VcjYxVf"
        },
        {   
            "title":"Diy Moroccan lamp,jam jar lamp how to,how to make lantern with jar",
             "url":"https://youtu.be/SlzesWLkmic?si=8QoNuwhKDgVjrfMv"
        }
    ]
    return random.choice(videos)

