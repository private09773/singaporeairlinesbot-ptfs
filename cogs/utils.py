from diseasy.math_solver import solve_equation, simplify_expr, expand_expr, factor_expr, evaluate, derivative, integral, MathError
from diseasy.ext.commands import command
from diseasy.ext.commands.cog import Cog
from diseasy.ext.slash import slash_command
from diseasy.ext.slash.core import Interaction, SlashCommand, SlashOption
from diseasy.variables import VARIABLES, register
from diseasy import Embed

class Utils(cog):
		def __init__(self, bot):
				super().__init__()
				self.bot = bot
	 
	 # Math Commands
	 @command(name="solve", description="Solve an equation.") 
	 async def solve(ctx, equation):
	 		try:
	 				result = solve_equation(equation, "x")
	 				await ctx.send(message=f"x = {result}")
	 		except MathError as e:
	 				await ctx.send(message=f"Cannot solve that: {e}")
	 
	 @slash_command(name="solve", description="Solve an equation.")
	 async def solve(interaction):
	 		equation = interaction.option_from("equation")
	 		try:
	 				result = solve_equation(equation, "x")
	 				await interaction.send(message=f"x = {result}")
	 		except MathError as e:
	 				await interaction.send(message=f"Cannot solve that: {e}")
	 
	 solve.slashoption(name="equation", type="3", required=True)
	 
	 @command(name="simplify", description="Simplify an equation.")
	 async def simpify(ctx, expression):
	 		try:
	 				result = simplify_expr(expression)
	 				await ctx.send(message=f"Simplified your math equation: {result}")
	 		except MathError as e:
	 				await ctx.send(message=f"I cannot simplify your equation: {e}")
	 
	 @slash_command(name="simplify", description="Simplify an equation.")
	 async def simplify(interaction):
	 		result = interaction.option_from("expression")
	 		try:
	 				result = simplify_expr(expression)
	 				await ctx.send(message=f"Simplified your math equation: {result}")
	 		except MathError as e:
	 				await ctx.send(message=f"I cannot simplify your equation: {e}")
	 
	 simplify.slashoption(name="expression", type="3", required=True)
	 
	 @command(name="calc", description="Evaluates a numeric expression")
  async def calc(ctx, expression):
    try:
        result = evaluate(expression)
        await ctx.send(message=f"= {result}")
    except MathError as e:
        await ctx.send(message=f"Couldn't calculate that: {e}")

  @command(name="derivative", description="Finds the derivative of an expression")
  async def derivative_cmd(ctx, expression):
    try:
        result = derivative(expression, "x")
        await ctx.send(message=f"d/dx = {result}")
    except MathError as e:
        await ctx.send(message=f"Couldn't differentiate that: {e}")

  @command(name="integral", description="Finds the integral of an expression")
  async def integral_cmd(ctx, expression):
    try:
        result = integral(expression, "x")
        await ctx.send(message=f"∫ dx = {result}")
    except MathError as e:
        await ctx.send(message=f"Couldn't integrate that: {e}")
  
  @slash_command(name="calc", description="Evaluates a numeric expression")
  async def calc(interaction):
    expression = interaction.option_from("expression")
    try:
        result = evaluate(expression)
        await interaction.send(message=f"= {result}")
    except MathError as e:
        await interaction.send(message=f"Couldn't calculate that: {e}")

  calc.slashoption(name="expression", type="3", required=True)


  @slash_command(name="derivative", description="Finds the derivative of an expression")
  async def derivative_cmd(interaction):
    expression = interaction.option_from("expression")
    try:
        result = derivative(expression, "x")
        await interaction.send(message=f"d/dx = {result}")
    except MathError as e:
        await interaction.send(message=f"Couldn't differentiate that: {e}")

  derivative_cmd.slashoption(name="expression", type="3", required=True)


  @slash_command(name="integral", description="Finds the integral of an expression")
  async def integral_cmd(interaction):
    expression = interaction.option_from("expression")
    try:
        result = integral(expression, "x")
        await interaction.send(message=f"∫ dx = {result}")
    except MathError as e:
        await interaction.send(message=f"Couldn't integrate that: {e}")

  integral_cmd.slashoption(name="expression", type="3", required=True)
  
  # Ping 
  @command(name="ping", description="Pong!")
  async def ping(self, ctx):
  		await ctx.send(message="Pong!")
  		
  @slash_command(name="ping", description="Pong!")
  async def ping(self, interaction):
  		await interaction.send(message="Pong!")
  
  # Info Commands
  @command(name="userinfo", description="Yours/someones userinfo.")
  async def userinfo(ctx):
  		# Embed Lines
  		line1 = "**Username**: <user.name>"
  		line2 = "**User ID**: `<user.id>`"
  		line3 = "**User Mention**: <user.mention>"
  		line4 = "**User's Top Role**: <user.top_role>"
  		line5 = "**User's Join Date**: `<user.joined_at>`"
  		# Embed
  		embed = Embed(
  				title="<user.name>'s info"
  				description=line1 + "" + line2 + "" + line3 + "" + line4 + "" + line5
  				color=0x00FF08
  		)
  await ctx.send(message="", embed=embed)
  
  @slash_command(name="userinfo", description="Shows info about a user")
  async def userinfo_slash(interaction):
    member = interaction.option_from("member") or interaction.user

    embed = Embed(
        title="<user.name>'s Info",
        color=0x5865F2
    )
    embed.add_field(name="Username", value="<user.name>", inline=True)
    embed.add_field(name="User ID", value="<user.id>", inline=True)
    embed.add_field(name="Mention", value="<user.mention>", inline=True)
    embed.add_field(name="Top Role", value="<user.top_role>", inline=True)
    embed.add_field(name="Joined At", value="<user.joined_at>", inline=True)
    embed.add_field(name="Is Bot", value="<user.is_bot>", inline=True)

    await interaction.send(embed=embed)

    userinfo_slash.slashoption(name="member", type="6", required=False)
  
# Initalize/Load All bot commands.
bot.add_slash_command(solve)
bot.add_slash_command(simplify)
bot.add_slash_command(calc)
bot.add_slash_command(derivative_cmd)
bot.add_slash_command(integral_cmd)
bot.add_slash_command(userinfo_slash)
bot.add_slash_command(ping)

bot.add_command(userinfo)
bot.add_command(solve_prefix)
bot.add_command(simplify_prefix)
bot.add_command(calc_prefix)