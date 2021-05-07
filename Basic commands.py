#First you need to make a balance command

@client.command()
async def bal(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"💸| {ctx.author.name}'s balance ¥",color = discord.Color.red())
    em.add_field(name = "Wallet balance",value = wallet_amt)
    em.add_field(name = "Bank balance",value = bank_amt)
    await ctx.send(embed = em)


#To add cooldown do the following

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown): #check if on cooldown
        msg = '**⏰ | Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)

#Now the economy commands
--To get the economy commands working your first need to create a mainbank.json file in your bot folder--
--Main bank will store all the data of a users bal--

#Beg command

@client.command()
@commands.cooldown(1,60,commands.BucketType.user)  #this is for the cooldowns
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(201)

    await ctx.send(f"🔫 |Someone gave you {earnings} ¥ !!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
        
#work command

@client.command()
@commands.cooldown(1,60,commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(100,501)

    await ctx.send(f"🎒 | You worked hard and got {earnings} ¥ !!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
        
#fight and crime command for extra earnings

@client.command()
@commands.cooldown(1,600,commands.BucketType.user)
async def fight(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(200,701)

    await ctx.send(f"⚔️ | You fought hard and got {earnings} ¥ !!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.command()
@commands.cooldown(1,600,commands.BucketType.user)
async def crime(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(200,701)

    await ctx.send(f"😒 | Bruh you stole a beggar and got {earnings} ¥ !!")

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)
        
#Slots command [you can change the == as per your win requirements]

@client.command()
async def slots(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You dont have enough cash!")
        return
    if amount<0:
        await ctx.send("Amount must be positive!")
        return

    final = []
    for i in range(3):
        a = random.choice(["👑","🍒","💰"])

        final.append(a)
    
    await ctx.send(str(final))

    if final[0] == final[1] and final[0] == final[2] and final[2] == final[1] or final[0] == final[2]:
        await update_bank(ctx.author,3*amount)
        await ctx.send("You won!")

    else:
        await update_bank(ctx.author,-0*amount)
        await ctx.send("You lost!")
    
        
    await update_bank(ctx.author,-1*amount)
