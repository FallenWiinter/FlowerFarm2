print("Lancement du bot...")
import discord
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
     print("Bot pret")
     await bot.change_presence(status=discord.Status.idle,
                               activity=discord.Game("Coder mais galere un peux"))
@bot.command()
@commands.has_any_role("Administrateurs", "Adjoint.e")
async def open(ctx):
    await ctx.message.delete()
    msg = "<@&774569230267187212> **La zone est ouverte** ! Allez tous en **A291775** !\n\n*[Afin d'enlever les notifications allez dans le salon <#774567598972469249>]*"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)


@bot.command()
@commands.has_any_role("Administrateurs", "Adjoint.e")
async def close(ctx):
    await ctx.message.delete()
    msg = "**La zone est fermée** ! :pensive: Mais vous serez les premiers avertis de la réouverture ! :wink:"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)


@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def open5(ctx):
    await ctx.message.delete()
    msg = "<@&774569230267187212> La zone **A291775** ouvre dans **5 minutes** ! Soyez prêts !\n\n*[Afin d'enlever les notifications allez dans le salon <#774567598972469249>]*"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)


@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def banque(ctx):
    await ctx.message.delete()
    msg = "<@&774569230267187212> Les comptes en banque dans le salon <#771387246501953557> ainsi que le !classement (<#774567598972469249>) ont été actualisés !"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def event(ctx):
    await ctx.message.delete()
    msg = "<@&774569230267187212> **Event** dans quelques secondes ! C'est urgent ! Tous en **A291775** !\n\n*[Afin d'enlever les notifications allez dans le salon <#774567598972469249>]*"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def event5(ctx):
    await ctx.message.delete()
    msg = "<@&774569230267187212> **Event** dans **5 minutes** ! Vite ! Tous en **A291775** !\n\n*[Afin d'enlever les notifications allez dans le salon <#774567598972469249>]*"
    channel = bot.get_channel(771387241390014524)
    await channel.send(msg)

@bot.command()
async def classement(ctx):
    await ctx.message.delete()
    pos1 = ":first_place: : **X1** avec Y   ¥"
    pos2 = ":second_place: : **X2** avec Y ¥"
    pos3 = ":third_place: :  **X3** avec Y ¥"
    date = "05/08/2020 à 00:15)*"
    await ctx.author.send("Le classement **monétaire** du Flower Farm est : \n\n"+pos1+"\n\n"+pos2+"\n\n"+pos3+"\n\n"+"*(Dernière actualisation le "+date)

@bot.event
async def on_member_join(nouveau_membre: discord.Member):
    channel = bot.get_channel(771387239577681992) # ID du channel
    pseudo = nouveau_membre.mention
    await channel.send(f"Bienvenue {pseudo} sur le serveur discord du SkyFarm de la zone A167676 🎉🤗 !")


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    mention = get(roles, name="Mentionné.e.s")
    pseudo = get(roles, name="Pseudo")
    joueur = get(roles, name="Joueur.se")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 771387233030242364 and emoji == "✅" and message == 774610316305891339:
        await membre.add_roles(mention)
        await membre.add_roles(pseudo)
        await membre.add_roles(joueur)

        await membre.send(
            "**Tu as maintenant acces au serveur ! ** "
            "\n\n**N'oublie pas** de changer de pseudo dans le salon <#771387247257321483>"
            "\nTu peux **consulter ton compte en banque** dans le salon <#771387246501953557>. "
            "\nTu peux également **consulter le classement** et utiliser les différents bots dans le salon <#774567598972469249>.  ")



@bot.command()
async def react(ctx):
    message = await ctx.fetch_message(774610316305891339)
    emoji = '✅'
    await message.add_reaction(emoji)

@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    mention = get(roles, name="Mentionné.e.s")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 774567598972469249  and emoji == "❌" and message == 774648584750497793:
        await membre.remove_roles(mention)

        await membre.send("Tu **ne recevra** maintenant **plus de notification**. Tu peux tout de même **les réactiver** en **enlevant la réaction** :x: au même message")

@bot.event
async def on_raw_reaction_remove(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    mention = get(roles, name="Mentionné.e.s")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 774567598972469249  and emoji == "❌" and message == 774648584750497793:
        await membre.add_roles(mention)

        await membre.send("Suite à **cette réactivation** tu **recoit** dés maintenants **les notifications** du serveur !")


jeton = "Nzc0NTY1NDA5NjM3NTMxNjk4.X6ZoQA.AssMkI58-Q72aGnFSdMvg9S4LmE" \

bot.run(jeton)
