print("Lancement du bot...")
import discord

from discord.ext import commands
from discord.utils import get
from discord import NotFound


bot = commands.Bot(command_prefix='!')

#Changer le Statut
@bot.event
async def on_ready():
     print("Bot pret")
     await bot.change_presence(status=discord.Status.idle,
                               activity=discord.Game("la zone A167676"))

@bot.command()
async def items(ctx,arg):
    arg = arg.split()
    arg[0] = arg[0].lower()
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540 :
        if arg[0] == "pokeballs":
            await ctx.send(' {0} Voici la liste des **Pokeballs**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Pokeballs Page 1.png'))
        elif arg[0] == "baies":
            await ctx.send(' {0} Voici la liste des **Baies**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Baies Page 1.png'))
        elif arg[0] == "autres":
             await ctx.send(' {0} Voici la liste de tous **les objets non catégorisables**'.format(ctx.author.mention))
             await ctx.send(file=discord.File('Items Autres Page 1.png'))
             await ctx.send(file=discord.File('Items Autres Page 2.png'))
        elif arg[0] == "equipement":
            await ctx.send(' {0} Voici la liste des **Équipements**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Equipement Page 1.png'))
        elif arg[0] == "fossiles":
            await ctx.send(' {0} Voici la liste des **Fossiles**, des **Pierres** et des **Roches**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Fossiles Page 1.png'))
        elif arg[0] == "gemmes":
            await ctx.send(' {0} Voici la liste des Gemmes, des **Orbes**, des **Poudres** et des **Encens**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Gemmes Page 1.png'))
        elif arg[0] == "loots":
            await ctx.send(' {0} Voici la liste des **Loots**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Loots Page 1.png'))
        elif arg[0] == "plaques":
            await ctx.send(' {0} Voici la liste des **Plaques**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Plaques Page 1.png'))
        elif arg[0] == "tickets":
            await ctx.send(' {0} Voici la liste des **Tickets de Pokémons**'.format(ctx.author.mention))
            await ctx.send(file=discord.File('Items Tickets Page 1.png'))
            await ctx.send(file=discord.File('Items Tickets Page 2.png'))
        else:
            await ctx.send("Merci de renseigner une de ces catégories : Baies, Pokéballs, Tickets, Gemmes, Loots, Equipement, Plaques ou Autres")
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon" )

@items.error
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
           await ctx.send("Merci de renseigner une de ces catégories : Baies, Pokéballs, Tickets, Gemmes, Loots, Equipement, Plaques ou Autres")

@bot.command()
async def pokedex(ctx,arg):
    arg = arg.split()
    arg[0] = arg[0].lower()
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        if arg[0] == "acier":
            await ctx.send(' {0} Voici tous les Pokémons de type **Acier** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Acier Page 1.png'))
            await ctx.send(file=discord.File('Type Acier Page 2.png'))
        elif arg[0] == "combat":
            await ctx.send(' {0} Voici tous les Pokémons de type **Combat** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Combat Page 1.png'))
            await ctx.send(file=discord.File('Type Combat Page 2.png'))
        elif arg[0] == "dragon":
            await ctx.send(' {0} Voici tous les Pokémons de type **Dragon** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Dragon Page 1.png'))
        elif arg[0] == "eau":
            await ctx.send(' {0} Voici tous les Pokémons de type **Eau** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Eau Page 1.png'))
            await ctx.send(file=discord.File('Type Eau Page 2.png'))
            await ctx.send(file=discord.File('Type Eau Page 3.png'))
        elif arg[0] == "electrik":
            await ctx.send(' {0} Voici tous les Pokémons de type **Electrik** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Electrik Page 1.png'))
            await ctx.send(file=discord.File('Type Electrik Page 2.png'))
        elif arg[0] == "fée":
            await ctx.send(' {0} Voici tous les Pokémons de type **Fée** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Fée Page 1.png'))
        elif arg[0] == "feu":
            await ctx.send(' {0} Voici tous les Pokémons de type **Feu** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Feu Page 1.png'))
            await ctx.send(file=discord.File('Type Feu Page 2.png'))
        elif arg[0] == "glace":
            await ctx.send(' {0} Voici tous les Pokémons de type **Glace** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Glace Page 1.png'))
        elif arg[0] == "insecte":
            await ctx.send(' {0} Voici tous les Pokémons de type **Insecte** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Insecte Page 1.png'))
            await ctx.send(file=discord.File('Type Insecte Page 2.png'))
        elif arg[0] == "normal":
            await ctx.send(' {0} Voici tous les Pokémons de type **Normal** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Normal Page 1.png'))
            await ctx.send(file=discord.File('Type Normal Page 2.png'))
            await ctx.send(file=discord.File('Type Normal Page 3.png'))
        elif arg[0] == "plante":
            await ctx.send(' {0} Voici tous les Pokémons de type **Plante** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Plante Page 1.png'))
            await ctx.send(file=discord.File('Type Plante Page 2.png'))
        elif arg[0] == "poison":
            await ctx.send(' {0} Voici tous les Pokémons de type **Poison** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Poison Page 1.png'))
            await ctx.send(file=discord.File('Type Poison Page 2.png'))
        elif arg[0] == "psy":
            await ctx.send(' {0} Voici tous les Pokémons de type **Psy** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Psy Page 1.png'))
            await ctx.send(file=discord.File('Type Psy Page 2.png'))
        elif arg[0] == "roche":
            await ctx.send(' {0} Voici tous les Pokémons de type **Roche** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Roche Page 1.png'))
            await ctx.send(file=discord.File('Type Roche Page 2.png'))
        elif arg[0] == "sol":
            await ctx.send(' {0} Voici tous les Pokémons de type **Sol** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Sol Page 1.png'))
            await ctx.send(file=discord.File('Type Sol Page 2.png'))
        elif arg[0] == "spectre":
            await ctx.send(' {0} Voici tous les Pokémons de type **Spectre** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Spectre Page 1.png'))
        elif arg[0] == "tenebres":
            await ctx.send(' {0} Voici tous les Pokémons de type **Ténèbres** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Ténèbres Page 1.png'))
        elif arg[0] == "vol":
            await ctx.send(' {0} Voici tous les Pokémons de type **Vol** '.format(ctx.author.mention))
            await ctx.send(file=discord.File('Type Vol Page 1.png'))
            await ctx.send(file=discord.File('Type Vol Page 2.png'))
            await ctx.send(file=discord.File('Type Vol Page 3.png'))
        else:
            await ctx.send("Merci de renseigner un des Types suivant : Normal, Plante, Feu, Eau, Glace, Combat, Vol, Poison, Sol, Roche, Insecte, Spectre, Acier, Electrik, Psy, Dragon, Tenebres ou Fée")
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon" )

@pokedex.error
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Merci de renseigner un des Types suivant : Normal, Plante, Feu, Eau, Glace, Combat, Vol, Poison, Sol, Roche, Insecte, Spectre, Acier, Electrik, Psy, Dragon, Tenebres ou Fée")




@bot.command()
async def pokemon(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send("Voici le menu des commandes !\nEnvoie \"**![Chiffre correspondant]**\" **sur le serveur Skyfarm **pour avoir accès à la catégorie sélectionnée ! *(ex \"!1\" pour avoir accès au menu \"Team\")*\n**Seul le menu et les descriptions des commandes sont en français, tous les critères des commandes doivent être renseignés en anglais (Sauf pour les commandes commençant par \"__!__\").**\n")
        await ctx.send(file=discord.File('menu pokemon.png'))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon" )


@bot.command(name="1")
async def _1(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send(' ||{0}|| \n                                                                                   **Voici les bases pour bien commencer ton aventure :**\n\nBienvenue dans le Merveilleux monde des Pokémons !\n\nGrâce à se bot tu pourras : combattre des Pokémons, les faire évoluer et les collectionner; combattre des dresseurs/joueurs et même des Maitres d\'arêne ! Et encore pleins de belles choses t\'attendent !\n\nLe tutoriel pour commencer ton aventure sera après cette courte introduction.\n\nTout d\'abord, les combats de pokemons se passent sur le serveur et les combats entre les joueurs se passent en privé.\n\nMerci de jouer seul sur un seul et même salon. Si aucun n\'est disponible vous pouvez en demander un dans le salon <#653183948196806667>.\n\n**TRÈS IMPORTANT : Afin de capturer un Pokémon vous devez dire dans le chat lors d\'un combat sauvage le nom de la pokeball *(ex : pokeball, loveball, greatball etc)*** \n\nSi vous avez une question Mentionnez FallenWiinter et il fera le nécessaire pour vous aiguiller.\n\n**Maintenant place au tutoriel :**\n**Vous devez obligatoirement finir le tutoriel avant de vous déconnecter (cela prend 1 à 2 min)**\n\n**1.** Faites ** .menu**\n**2.** Mentionnez <@326161147411562507>\n**3.** Choisissez votre starter entre les 4 Pokémons proposés **(tapez un nombre entre 1 et 4 pour le choisir)**\n**4.** Sélectionnez votre genre en Écrivant "male" ou "female"\n**5.** Réussissez votre Premier combat ! *(Choisissez quelle attaque faire en écrivant un nombre entre 1 et 2)* *(Vous apprendrez plus tard les 2 autres attaques)\n**6.** Faites** .team** pour voir vos combattants ! \n**7.** Faites** .box **pour voir votre stockage\n**8.** Faites **.mypkinfo <Nom de votre starter>** pour voir les stats de votre Pokémon !\n**9.** Faites** .wallet **pour voir votre compte en banque !\n**10.** Partez à l\'aventure ! (**__.__menu** pour avoir les commandes toutes en anglais; **__!__menu** pour l\'avoir en français !)     '.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon" )

@bot.command(name="2")
async def _2(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send(' ||{0}||                                                                                    **Voici les commandes concernant les équipes de Pokémons :**\n\n**.team**\n*Affiche les Pokémons disponibles en combat*\n\n**.learn <Pokémon> <move> ** \n *Apprends un mouvement à un Pokémon*\n*(Vous découvrez des nouveaux mouvements en jouant)* \n\n**.mvdelete <Pokémon> <move>**\nFait oublier le mouvement à votre Pokémon\n\n**.pkname <Pokémon> <surnom>**  \n*Donne un surnom à votre Pokémon*\n\n**.swap <Position de départ> <Position d\'arrivé>**\nChange votre Pokémon d\'emplacement\n\n**.release <Pokémon> **\n*Libère votre Pokémon'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="3")
async def _3(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||\n                                                                                   **Voici les commandes concernant les combats et les échanges :**\n\n**Chaque victoire en combat vous rapporte des PKC mais chaque defaite vous en fait perdre**\n**Pour capturer un Pokémon vous devez lors d\'un combat sauvage ecrire le nom de la Pokéball que vous voulez utiliser *(!items pokeballs pour avoir la liste)***\n\n**.route** [numéro]\nDémarre un combat avec le Pokémon sauvage désigné par le numéro renseigné\n\n**.route info <Nombre>**  \nMontre les Pokémons sauvages aux alentours correspondants au numéro renseigné\n\n**.battle @dresseur** \nDémarre un combat avec le dresseur/joueur désigné\n*(Les combats se déroulent en MP)*\n\n**.battlegym **\nDémarre un combat avec un maitre Pokémon \n*(PS : ils sont forts et vous détruisent)*\n\n**.trade @dresseur <Pokémon> <Number> <Pokémon> <Number> **\nÉchange votre Pokémon désigné contre le Pokémon désigné d\'un autre dresseur\n\n**.gift @dresseur <Nombre>**\nPermet de faire un don de PKC à un autre dresseur  '.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="4")
async def _4(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||\n                                                                                   **Voici les commandes concernant vos sacs et les items  :**\n**.bag** \nAffiche votre sac\n\n**.buybag**\nPermet d\'acheter 10 emplacement pour votre sac *(Prix : 300 PKC)*\n\n**.give <Pokémon> <item en anglais> **\nPermet de donner un item à votre Pokémon\n\n**.take <Pokémon> <item en anglais **\nPermet de prendre un item à votre Pokémon\n\n**__.__items**\nAffiche la liste des items en anglais\n\n**__!__items <Catégorie>**\nVous montre la liste des items traduite en français (La liste des catégories : Baies, Pokéballs, Tickets, Gemmes, Loots, Equipement, Plaques ou Autres'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")


@bot.command(name="5")
async def _5(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||                                                                                   **Voici les commandes concernant votre stockage :**\n\n**Votre stockage est l\'endroit ou vous stockez vos Pokémons qui ne combattent pas.**\n\n**.box** \nAffiche votre stockage *(à gauche votre stockage à droite votre team)*\n\n**.buybox** \nAchète un nouveau Stockage *(PRIX : 300 PKC)*\n\n**.swap <Position du pokémon de depart> <Position du Pokémon d\'arrivé> \n**Change de place votre Pokémon  (Les positions sont en lignes+colonnes exemple ".swap a1 b2")\n\n**.boxswap <numéro du stockage> <Nom du Pokémon>**\nStock votre Pokémon dans le Stockage désigné\n\n**.boxswap <numéro du stockage> <emplacement du Pokémon dans le stockage>**\nRécupère le Pokémon du stockage\n\n**boxrelease <numéro du stockage> <emplacement du Pokémon dans le stockage**\nLibère le Pokémon désigné\n\n**.boxmove <numéro du stockage de départ> <numéro du stockage d\'arrivée> <emplacement du Pokémon  de départ> <emplacement du Pokémon d\'arrivée>**\nChange le Pokémon de box\n\n**.boxsearch <Pokémon>**\nRecherche le Pokémon voulu dans tous les stockages'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="6")
async def _6(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||                                                                                   **Voici les commandes concernant le Pokedex :**\n\n**Le Pokedex vous permet d\'en apprendre plus sur les Pokémons !**\n\n**.mypkinfo <Pokémon> **\nVous donne les informations sur __votre__ Pokémon\n\n**__.__pokedex <Type en anglais> **\nVous donne la liste de tous les Pokémons selon le type (en anglais)\n\n**__!__pokedex <Type en français>**\nVous donne la liste de tous les Pokémons traduite en français (La liste des Types : Normal, Plante, Feu, Eau, Glace, Combat, Vol, Poison, Sol, Roche, Insecte, Spectre, Acier, Electrik, Psy, Dragon, Tenebres ou Fée)\n\n**__.__pokedex <Pokémon> **\nVous donne les informations __générales__ selon le Pokémon renseigné\n\n**.pokedex caught** \nVous donne la liste des Pokémons que vous avez capturés\n\n**__.__natures**\nVous donne les atouts de toutes les natures en anglais\n\n**__!__natures**\nVous donne la liste de toutes les natures des Pokémons traduite en français'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="7")
async def _7(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||                                                                                   **Voici les commandes concernant le Centre Pokémon :**\n\n**Le centre Pokémon vous sert à obtenir des œufs et les faire éclore. Vous ne pouvez envoyer les Pokémons dans le centre qu\'en paire.**\n\n**.daycare**\nPour voir le centre Pokémon\n\n**.raise <Pokémon> <Pokémon>**\nDépose les 2 Pokémons dans le Centre Pokémon * (2 Pokémons sont obligatoires)*\n\n**.get eggs**\nPermet de prendre les œufs qui sont dans le Centre Pokémon\n\n**.get <Pokémon>**\nPermet de prendre le Pokémon désigné'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="8")
async def _8(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||                                                                                   **Voici les commandes concernant la Boutique et l\'Économie :**\n\n**Le PKC (ou Pokémon Coin) est la monnaie principale, le PKD (ou Pokémon Diamond) est la monnaie secondaire. Les PKD sont seulement obtenables par le .vote ou le .donate.**\n\n**.wallet**\nPermet de voir votre Compte en Banque (PKC et PKD)\n\n**.buy <item> <quantité> **\nVous permet d\'acheter des items* (__.__items <item en anglais> pour avoir son prix et __!__items pour avoir la traduction des items en français)*\n\n**.sell <item> <quantité>**\nVous permet de vendre des items\n\n**.vote**\nVous permet de voter pour le bot afin de gagner de l\'XP des PKC et des PKD '.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")

@bot.command(name="9")
async def _9(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('||{0}||                                                                                   **Voici les commandes concernant les Options :**\n\n**.notif**\nActive ou désactive les notifications en jeu\n\n**.fly**\nAfin de changer de région\n\n**.privacy**\nAfin de mettre vos stats en privé et que les gens ne puissent pas les voir'.format(ctx.author.mention))
    else:
        await ctx.send("Afin de faire cela merci d'aller dans un Salon pour Pokémon")



@bot.command()
async def natures(ctx):
    await ctx.message.delete()
    if ctx.message.channel.id == 737795629668892762 or ctx.message.channel.id == 737795677236756571 or ctx.message.channel.id == 737795709138370622 or ctx.message.channel.id == 740245125556338708 or ctx.message.channel.id == 740245516381716540:
        await ctx.send('{0} Voici la liste des natures des pokemons'.format(ctx.author.mention))
        await ctx.send(file=discord.File('Natures.png'))


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    roles = bot.get_guild(payload.guild_id).roles
    pokemon1 = get(roles, name="Pokémon 1")
    pokemon2 = get(roles, name="Pokémon 2")
    pokemon3 = get(roles, name="Pokémon 3")
    pokemon4 = get(roles, name="Pokémon 4")
    pokemon5 = get(roles, name="Pokémon 5")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    if canal == 740220330987094189 and emoji == "✅" and message == 740864662731751466:
        for role in membre.roles:
            if 737795008807305327 == role.id:
                await membre.send("Tu as deja accès au salon **Pokemon 1**")
                return
            elif 737795131754676267 == role.id:
                await membre.send("Tu as deja accès au salon **Pokemon 2**")
                return
            elif 737795163409219624 == role.id:
                await membre.send("Tu as deja accès au salon **Pokemon 3**")
                return
            elif 740241648835100783 == role.id:
                await membre.send("Tu as deja accès au salon **Pokemon 4**")
                return
            elif 740241808142893088 == role.id:
                await membre.send("Tu as deja accès au salon **Pokemon 5**")
                return
        if len(pokemon1.members) < 1:
            await membre.add_roles(pokemon1)
            await membre.send("Tu as accès au salon **Pokémon 1** ! **N'oublie pas** d'**enlever la notification** quand tu arrête de jouer ! :wink:")
        elif len(pokemon2.members) < 1:
            await membre.add_roles(pokemon2)
            await membre.send(
                "Tu as accès au salon **Pokémon 2** ! **N'oublie pas** d'**enlever la notification** quand tu arrête de jouer ! :wink:")
        elif len(pokemon3.members) < 1:
            await membre.add_roles(pokemon3)
            await membre.send(
                "Tu as accès au salon **Pokémon 3** ! **N'oublie pas** d'**enlever la notification** quand tu arrête de jouer ! :wink:")
        elif len(pokemon4.members) < 1:
            await membre.add_roles(pokemon4)
            await membre.send(
                "Tu as accès au salon **Pokémon 4** ! **N'oublie pas** d'**enlever la notification** quand tu arrête de jouer ! :wink:")
        elif len(pokemon5.members) < 1:
            await membre.add_roles(pokemon5)
            await membre.send(
                "Tu as accès au salon **Pokémon 5** ! **N'oublie pas** d'**enlever la notification** quand tu arrête de jouer ! :wink:")
        else:
            await membre.send("Il n'y a **plus** de salon Pokémon disponible ! Fais une **demande** dans le salon <#653183948196806667> afin d'avoir un **nouveau salon** ! :wink: ")


@bot.event
async def on_raw_reaction_remove(payload):

     emoji = payload.emoji.name
     canal = payload.channel_id
     message = payload.message_id

     roles = bot.get_guild(payload.guild_id).roles
     pokemon1 = get(roles, name="Pokémon 1")
     pokemon2 = get(roles, name="Pokémon 2")
     pokemon3 = get(roles, name="Pokémon 3")
     pokemon4 = get(roles, name="Pokémon 4")
     pokemon5 = get(roles, name="Pokémon 5")
     membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)


     #Detecter les bons salon, emoji, message
     if canal == 740220330987094189 and emoji == "✅" and message == 740864662731751466:
         await membre.remove_roles(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5)
         await membre.send("Tu as fermé le salon Pokémon, **Merci** d'y avoir pensé ! :wink:")
@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def open(ctx):
    await ctx.message.delete()
    msg = "<@&616598123803967518> La zone est ouverte ! Allez tous en A167676 !\n\n*[Afin d'enlever les notifications allez dans le salon <#616604530351538204>]*"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)


@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def open5(ctx):
    await ctx.message.delete()
    msg = "<@&616598123803967518> La zone A167676 ouvre dans 5 minutes ! Soyez prêts !\n\n*[Afin d'enlever les notifications allez dans le salon <#616604530351538204>]*"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def banque(ctx):
    await ctx.message.delete()
    msg = "<@&616598123803967518> Les comptes en banque dans le salon <#735121147061862410> ainsi que le !classement (<#774567598972469249>)  ont été actualisés !"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def close(ctx):
    await ctx.message.delete()
    msg = "Fermeture de la zone ! :pensive: Mais vous serez les premiers au courant lors de la réouverture ! :wink:"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def event(ctx):
    await ctx.message.delete()
    msg = "<@&616598123803967518> Event dans quelques secondes ! C'est urgent ! Tous en A167676 !\n\n*[Afin d'enlever les notifications allez dans le salon <#616604530351538204>]*"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)

@bot.command()
@commands.has_any_role("Administrateurs", "Adjoints")
async def event5(ctx):
    await ctx.message.delete()
    msg = "<@&616598123803967518> Event dans 5 minutes ! Vite ! Tous en A167676 !\n\n*[Afin d'enlever les notifications allez dans le salon <#616604530351538204>]*"
    channel = bot.get_channel(612643872463519755)
    await channel.send(msg)

@bot.command()
async def classement(ctx):
    await ctx.message.delete()
    pos1 = ":first_place: : **PaleRider_** avec 42 418 900   ¥"
    pos2 = ":second_place: : **tryjn666** avec 26 436 400 ¥"
    pos3 = ":third_place: :  **Here_L** avec 3 866 200 ¥"
    date = "05/08/2020 à 00:15)*"
    await ctx.author.send("Le classement **monétaire** du SkyFarm est : \n\n"+pos1+"\n\n"+pos2+"\n\n"+pos3+"\n\n"+"*(Dernière actualisation le "+date)

@bot.command()
async def game(ctx,nouveau_membre: discord.Member):
    pseudo = nouveau_membre.mention
    channel = bot.get_channel(740220330987094189)
    membre = ctx.message.author
    mini1 = get(ctx.guild.roles, name="Jeux 1")
    mini2 = get(ctx.guild.roles, name="Jeux 2")
    mini3 = get(ctx.guild.roles, name="Jeux 3")
    mini4 = get(ctx.guild.roles, name="Jeux 4")
    mini5 = get(ctx.guild.roles, name="Jeux 5")
    auteur = ctx.author.mention
    if ctx.author.id == nouveau_membre.id:
        await ctx.send("Tu ne peux pas jouer avec toi même !")
        return
    for role in membre.roles:
        if 737794706674811003 == role.id:
           await membre.send("Tu as deja acces au salon **Mini Jeux 1**")
           return
        elif 737794878255136888 == role.id:
           await membre.send("Tu as deja acces au salon **Mini Jeux 2**")
           return
        elif 737794940238561300 == role.id:
            await membre.send("Tu as deja acces au salon **Mini Jeux 3**")
            return
        elif 740612095904710767 == role.id:
            await membre.send("Tu as deja acces au salon **Mini Jeux 4**")
            return
        elif 740612132269326447 == role.id:
            await membre.send("Tu as deja acces au salon **Mini Jeux 5**")
            return
    if nouveau_membre.id == 356065937318871041:

        if len(mini1.members) < 1:
            await membre.add_roles(mini1)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 1 **")
            return
        elif len(mini2.members) < 1:
            await membre.add_roles(mini2)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 2 **")
            return
        elif len(mini3.members) < 1:
            await membre.add_roles(mini3)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 3 **")
            return
        elif len(mini4.members) < 1:
            await membre.add_roles(mini4)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 4 **")
            return
        elif len(mini5.members) < 1:
            await membre.add_roles(mini5)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 5 **")
            return
        else:
            await membre.send(
                "Il n'y a **plus** de salon Mini Jeux disponible ! Fais une **demande** dans le salon <#653183948196806667> afin d'avoir un **nouveau salon* ! :wink:")
    else:
        await ctx.send(f"{auteur} "+ "te demande en duel de mini-jeux !"+ f"{pseudo}"+ ",acceptes-tu d\'y participer ?")


@bot.event
async def on_raw_reaction_add(payload):

    roles = bot.get_guild(612621063687241740).roles
    mini1 = get(roles, name="Jeux 1")
    mini2 = get(roles, name="Jeux 2")
    mini3 = get(roles, name="Jeux 3")
    mini4 = get(roles, name="Jeux 4")
    mini5 = get(roles, name="Jeux 5")
    emoji = payload.emoji.name
    canal = payload.channel_id
    message_id = payload.message_id
    membre = bot.get_guild(612621063687241740).get_member(payload.user_id)

    message = await bot.get_user(payload.user_id).fetch_message(message_id)
    iduser = message.mentions[1].id
    print(message)

    if emoji == "✅":

        for role in membre.roles:
            if 737794706674811003 == role.id:
                await membre.send("Tu as deja acces au salon **Mini Jeux 1**")
                return
            elif 737794878255136888 == role.id:
                await membre.send("Tu as deja acces au salon **Mini Jeux 2**")
                return
            elif 737794940238561300 == role.id:
                await membre.send("Tu as deja acces au salon **Mini Jeux 3**")
                return
            elif 740612095904710767 == role.id:
                await membre.send("Tu as deja acces au salon **Mini Jeux 4**")
                return
            elif 740612132269326447 == role.id:
                await membre.send("Tu as deja acces au salon **Mini Jeux 5**")
                return
        if len(mini1.members) < 1:
            print("debug")
            await membre.add_roles(mini1)
            await user1.add_role(mini1)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 1 **")
            return
        elif len(mini2.members) < 1:
            await membre.add_roles(mini2)
            await user1.add_role(mini2)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 2 **")
            return
        elif len(mini3.members) < 1:
            await membre.add_roles(mini3)
            await user1.add_role(mini3)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 3 **")
            return
        elif len(mini4.members) < 1:
            await membre.add_roles(mini4)
            await user1.add_role(mini4)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 4 **")
            return
        elif len(mini5.members) < 1:
            await membre.add_roles(mini5)
            await user1.add_role(mini5)
            await membre.send("Tu as maintenant accés au salon de Mini Jeux 5 **")
            return
        else:
            await membre.send(
                "Il n'y a **plus** de salon Mini Jeux disponible ! Fais une **demande** dans le salon <#653183948196806667> afin d'avoir un **nouveau salon* ! :wink:")

@bot.event
async def on_member_join(nouveau_membre: discord.Member):
    channel = bot.get_channel(612643857884250131) # ID du channel
    pseudo = nouveau_membre.mention
    await channel.send(f"Bienvenue {pseudo} sur le serveur discord du SkyFarm de la zone A167676 🎉🤗 !")


jeton = "NzM5NzczNjU5Mzc5NTMxNzc3.XyfV6A.bffpOrGk1mHJFeDL2wA6yj2kHzY"

bot.run(jeton)
