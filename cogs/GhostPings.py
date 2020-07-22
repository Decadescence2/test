class GhostPings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('GhostPing file Loaded')

    @commands.command()
    async def GhostTest(self, ctx, *, question):
        spamnumber = 0
        while spamnumber < int(question):
                await ctx.send('**LURKING!?** ' + MyID, delete_after=2);
                asyncio.sleep(1)
                spamnumber += 1
                print ({spamnumber})
                await ctx.message.delete()

def setup(client):
    client.add_cog(GhostPings(client))
