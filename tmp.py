from dotenv import load_dotenv
import discord,os
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")
intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)
@client.event
async def on_ready():
    await client.get_channel(1556028288865018047).send("Welcome to the server! Please read the rules below.")
    await client.get_channel(1556028288865018047).send("Lift: Lift keeps the community airborne. Members are expected to lift each other up. Harassment, unnecessary hostility, or deliberately dragging others down will result in a loss of altitude, such as a warning or mute. Help keep the server elevated.")
    await client.get_channel(1556028288865018047).send("Thrust: Thrust is the engine that drives conversation forward. Keep text and voice channels moving in a positive direction. No spamming, flooding chat with identical memes, or using slurs or hate speech. Swearing is fine, just don't overdo it.")
    await client.get_channel(1556028288865018047).send("Drag: Drag slows the server down. Trolling, harassment, and cyberbullying create friction that ruins the vibe. Minimize the friction and keep the community streamlined.")
    await client.get_channel(1556028288865018047).send("Lift: Lift keeps the community airborne. Members are expected to lift each other up. Harassment, unnecessary hostility, or deliberately dragging others down will result in a loss of altitude, such as a warning or mute. Help keep the server elevated.")
    await client.get_channel(1556028288865018047).send("Weight: Weight is the gravitational pull holding us to reality. Content must remain grounded in safety and legality. Absolutely no NSFW content, illegal material, or dangerous links. Violations may result in a mute and/or more serious administrative action.")
    await client.get_channel(1556028288865018047).send("Bernoulli's Principle: High flow velocity can correspond to lower static pressure. When a debate accelerates too quickly and the pressure starts rising, Clouds may temporarily lock a channel or enable slow mode to let things cool down. Keep your cool when the velocity picks up.")
    await client.get_channel(1556028288865018047).send("Action & Reaction: Every action has an equal and opposite reaction. If you choose to break a rule or disrespect a member, expect an appropriate administrative reaction, such as a warning, mute, or worse. You are responsible for the momentum of your own actions.")
    await client.get_channel(1556028288865018047).send("Supersonic Flight: Going too fast breaks things. Do not bypass server security, circumvent automod filters, or attempt to raid the server. Breaking the barrier gets you ejected.")
    await client.get_channel(1556028288865018047).send("Boundary Layer: The boundary layer is the fluid zone closest to a surface and should not be unnecessarily disrupted. Respect people's personal boundaries. No unsolicited DMs, doxxing, or leaking private information. Keep the personal boundary layer intact.")
client.run(TOKEN)