import discord
import os 
from discord.ext import commands
from dotenv import load_dotenv
from utils import extraer_video_id 
from aleatorio import videos_botellas, videos_latas, videos_carton, videos_vidrio, consejo_random, datos_curiosos

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv(dotenv_path="token.env")
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

'''confirmación de que el bot ha iniciado sesión exitosamente'''

@bot.event
async def on_ready():
    print(f'✅ Bot iniciado como {bot.user}')

'''bot da la bienvenida a nuevos miembros del canal'''

@bot.event
async def on_member_join(member):
    print(f"🔔 Se ha unido: {member.name}")
    canal = discord.utils.get(member.guild.text_channels, name='general')
    if canal:
        await canal.send(f"👋 ¡Bienvenido/a {member.mention} al servidor!")

'''presentación del bot y sus funciones'''
@bot.event
async def on_ready():
    canal = bot.get_channel(CHANNEL_ID)
    embed=discord.Embed(
        title="Presentando al bot",
        description=" **¡Hola! Soy EcoBot 🌿**\n"
        "Estoy aquí para compartir datos curiosos, manualidades reciclables y consejos sobre el medio ambiente.\n"
        "Para saber sobre qué es la contaminación usa:`!contaminacion`,si deseas saber sobre los tipos de contaminación usa:`!tipos`, para saber sobre el cambio climático usa: `!cambio`,usa `!consejos` para recibir tips ecológicos, o `!carton,!vidrio,!latas,!botella` para ver una manualidad divertida que puedas hacer en casa. También puedes usar `!datos`, para saber algún dato curioso\n"
        "¡Explora y cuida el planeta conmigo! ♻️✨",
        color= discord.Color.yellow()
    ) 
    await canal.send(embed=embed)

'''Significado contaminación'''

@bot.command('contaminacion')
async def contaminacion(ctx):
    embed = discord.Embed(
        title="¿Qué es la contaminación?",
        description="La contaminación es la introducción de sustancias o elementos físicos en un medio ambiente que causan efectos perjudiciales para la salud, el equilibrio ecológico o la seguridad. Básicamente, es la alteración negativa de un entorno natural por la presencia de elementos dañinos. ",
        color= discord.Color.dark_green()
    )
    embed.set_image(url='https://i.postimg.cc/ZqTC4qC2/contaminaci-n.jpg')
    await ctx.send(embed=embed)

'''tipos de contaminación'''

@bot.command('tipos')
async def tipos_contaminacion (ctx):
    embed = discord.Embed(
        title="Tipos de contaminación",
        description="Contaminación del aire: Presencia de sustancias nocivas en la atmósfera, como gases tóxicos, partículas y otros contaminantes que afectan la calidad del aire que respiramos. \n"
        "Contaminación del agua: Introducción de sustancias o elementos que deterioran la calidad del agua, haciéndola inadecuada para su uso.\n" 
        "Contaminación del suelo: Presencia de sustancias químicas o residuos que afectan la composición y calidad del suelo, perjudicando la vida que depende de él.\n" 
        "Contaminación acústica:Exceso de ruido que puede ser perjudicial para la salud humana y el bienestar de los animales.\n" 
        "Contaminación lumínica:Exceso de luz artificial que afecta los ciclos naturales y la visibilidad del cielo nocturno.\n" 
        "Contaminación térmica:Aumento de la temperatura de un medio, como el agua, debido a la liberación de calor. \n"
        "Contaminación radiactiva:Presencia de materiales radiactivos en el ambiente, que pueden ser peligrosos para la salud.\n",
        color= discord.Color.dark_blue()

    )  
    embed.set_image(url='https://i.postimg.cc/vZ8tSGG8/types.jpg') 
    await ctx.send(embed=embed)

'''cambio climático significado'''

@bot.command('cambio')
async def cambio_climatico(ctx):
    embed = discord.Embed(
        title="¿Qué es el cambio climático?",
        description="El cambio climático es la alteración del clima y las temperaturas de la Tierra que afecta a los ecosistemas y origina cambios que directa o indirectamente son producidos por la actividad humana",
        color= discord.Color.dark_teal()
    )
    embed.set_image(url='https://i.postimg.cc/t4cMHsSC/change.jpg') 
    await ctx.send(embed=embed)

'''datos aleatorios'''

@bot.command('datos')
async def datos_random(ctx):
    datos = datos_curiosos()
    embed = discord.Embed(
        title="🌿 Dato curioso del día",
        description=datos,
        color= discord.Color.pink()
    )
    await ctx.send(embed=embed)

'''consejos aleatorios'''

@bot.command('consejos')
async def consejos(ctx):
    consejo = consejo_random()
    embed = discord.Embed(
        title="🌿 Consejo ecológico del día",
        description=consejo["texto"],
        color=discord.Color.teal()
    )
    embed.set_image(url=consejo["imagen"])
    await ctx.send(embed=embed)

'''Ideas con botellas '''

@bot.command('botella')
async def idea_botella(ctx):
    video = videos_botellas()
    video_id = extraer_video_id(video['url'])
    # uso del embed para hacer más llamativo el mensaje
    embed = discord.Embed(
        title=video['title'],
        url=video['url'],
        description="¡Aquí tienes una idea para reciclar botellas plásticas!",
        color=discord.Color.blue()
    )
    # Miniatura del video (YouTube)
    embed.set_thumbnail(url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
    await ctx.send(embed=embed)

'''Ideas con latas'''

@bot.command('latas')
async def idea_lata(ctx):
    video = videos_latas()
    video_id = extraer_video_id(video['url'])
    # uso del embed para hacer más llamativo el mensaje
    embed = discord.Embed(
        title=video['title'],
        url=video['url'],
        description="¡Aquí tienes una idea para reciclar latas! ",
        color=discord.Color.purple()
    )
    # Miniatura del video (YouTube)
    
    embed.set_thumbnail(url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
    await ctx.send(embed=embed)
 
'''Ideas con cartón '''

@bot.command('carton')
async def idea_carton (ctx):
    video = videos_carton()
    video_id = extraer_video_id(video['url'])
    # uso del embed para hacer más llamativo el mensaje
    embed = discord.Embed(
        title=video['title'],
        url=video['url'],
        description="¡Aquí tienes una idea para reciclar cartón! ",
        color=discord.Color.green()
    )
    # Miniatura del video (YouTube)
    
    embed.set_thumbnail(url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
    await ctx.send(embed=embed)

'''Ideas con vidrio'''

@bot.command('vidrio')
async def idea_vidrio (ctx):
    video = videos_vidrio()
    video_id = extraer_video_id(video['url'])
    # uso del embed para hacer más llamativo el mensaje
    embed = discord.Embed(
        title=video['title'],
        url=video['url'],
        description="¡Aquí tienes una idea para reciclar vidrio! ",
        color=discord.Color.orange()
    )
    # Miniatura del video (YouTube)
    embed.set_thumbnail(url=f"https://img.youtube.com/vi/{video_id}/0.jpg")
    await ctx.send(embed=embed)

# Cositas del token
    
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)

