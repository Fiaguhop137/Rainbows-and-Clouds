from dotenv import load_dotenv
import discord,os,math
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")
intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)
@client.event
async def on_ready():
    await client.get_channel(1556028288865018047).send("Welcome to the server! Please read the rules below.")
    await client.get_channel(1556028288865018047).send("Frequency: Every signal occupies its own frequency. Keep conversation appropriate to the channel and don't deliberately disrupt other conversations. Spam, flooding, and repeated messages create interference.")
    await client.get_channel(1556028288865018047).send("Interference: Waves can interfere with one another. Don't deliberately interfere with other members through trolling, harassment, hostility, or starting unnecessary conflicts. Let people communicate without turning every discussion into static.")
    await client.get_channel(1556028288865018047).send("Absorption: Materials can absorb electromagnetic energy. The server can absorb problematic behavior too, in the form of warnings, mutes, kicks, or bans. Repeated violations will eventually get absorbed from the server entirely.")
    await client.get_channel(1556028288865018047).send("Wavelength: Every wave has boundaries defined by its wavelength. Respect other people's boundaries. No unsolicited DMs, doxxing, leaking private information, or other invasions of privacy.")
    await client.get_channel(1556028288865018047).send("Energy: Electromagnetic radiation carries energy. Use that energy constructively. Keep discussion reasonably positive and don't deliberately make the server hostile or miserable for everyone else.")
    await client.get_channel(1556028288865018047).send("Spectrum: The electromagnetic spectrum covers an enormous range of frequencies. People can have very different interests, opinions, personalities, and identities. You don't have to agree with everyone, but you do have to treat people with basic respect.")
    await client.get_channel(1556028288865018047).send("Propagation: Electromagnetic waves propagate through their environment. Don't deliberately spread harmful content, misinformation intended to cause harm, malicious links, or anything that could compromise the server or its members.")
    await client.get_channel(1556028288865018047).send("Reflection: Waves can reflect from surfaces. Think before you send something, because once you've put something into a public channel, other people can see, quote, or respond to it. Don't use that as an excuse to post private information or harmful content.")
    await client.get_channel(1556028288865018047).send("Resonance: When a system is driven at the right frequency, its response can become dangerously large. Do not attempt to exploit, raid, crash, spam, or otherwise deliberately overwhelm the server. Don't bypass security systems or automod filters. If you try to make the server resonate, you'll probably discover that the moderation team also has a frequency.")
#client.run(TOKEN)
commands=[]
points=300
for i in range(points+1):
    x=i/(points/5)
    y=math.sin(x**2)
    sx=x*20
    sy=90-10*y
    commands.append(f"{'M' if i==0 else 'L'} {sx:.2f} {sy:.2f}")
print('<path d="' + " ".join(commands) + '" fill="none" stroke="white" stroke-width="2"/>')