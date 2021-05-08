#moderation commands

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(administrator = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.send(member.name + " has been kicked from the server, because:"+reason)
    await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(administrator = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided"):
    await ctx.send(member.name + " has been banned from the server, because:"+reason)
    await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(administrator=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name + " unbanned")
            return
    await ctx.send(member+" was not found")

#moderation command end
