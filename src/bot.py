import discord
import responses
import random

async def send_m(message, user_message, is_private):
    try: 
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else  await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = ''
    
    
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #print(f'{username} said: "{user_message}" ({channel})')
        
        # message = 'cringe!!!'
        # channel = await member.create_dm()
        # await channel.send(message)
        #preeb address
        #mine

        l = ["Akash", "Ari", "Moz","Chat", "Pat",  "Preeb", "Geeg"]
        og = ["Akash", "Ari", "Moz","Chat", "Pat",  "Preeb", "Geeg"]
        uid = [278999817575727104, 213750170389708801, 152215478348021761, 240977124024909825, 181245170715590657, 352170758019088384, 178990313929441281]

        uid_fake = [308370253266812928, 308370253266812928, 308370253266812928, 308370253266812928, 308370253266812928, 308370253266812928, 308370253266812928]

        # santa = "Akash"
        # santa = randomize(santa, "Akash", l)
        # user = client.get_user(308370253266812928)
        # message = "Rules: no wishlists, no dildos, no drugs, no alcohol, no sex toys, no telling people who you got, no asking for rerolls\n\n Your secret santa assginment is: " 
        # message+=santa
        # embed = discord.Embed(title="🅱 Secret Santa Assignment 🎅(Don't tell anyone who you get 🤫)", description=message)
        # await user.send(embed=embed)

        for i in range(0, len(uid)):
            santa = og[i]
            fin = ""
            fin+=santa
            fin+=" "
            santa = randomize(santa, santa, l)
            fin+=santa
            #print(fin)
            user = client.get_user(uid[i])
            message = "Rules: no wishlists, no dildos, no drugs, no alcohol, no sex toys, no telling people who you got, no asking for rerolls\n\n Gift exchange will happen on the 30th. If your secret santa isn't able to make it, their address has been specified in this message(except for moz)\n\n Your secret santa assginment is: " 
            message+=santa
            embed = discord.Embed(title="🅱 Secret Santa Assignment 🎅(Don't tell anyone who you get 🤫)", description=message)
            await user.send(embed=embed)

        # #ari
        # user = client.get_user(213750170389708801)
        # await user.send('cringe!!!')
        
        # #moz
        # user = client.get_user(152215478348021761)
        # await user.send('cringe!!!')
        
        # #chat
        # user = client.get_user(240977124024909825)
        # await user.send('cringe!!!')


        # #pat
        # user = client.get_user(181245170715590657)
        # await user.send('cringe!!!')

        # #preeb
        # user = client.get_user(352170758019088384)
        # await user.send('cringe!!!')

        # #geeg
        # user = client.get_user(178990313929441281)
        # await user.send('cringe!!!')
    client.run(TOKEN)

def randomize(santa, name, l):
    while(santa == name):
        rand = random.randint(0, len(l)-1)
        santa = l[rand]
    l.remove(santa)
    if(santa == "Preeb"):
        santa += "(his address is 1140 W Blaine St, Riverside, CA 92507)"
    return santa