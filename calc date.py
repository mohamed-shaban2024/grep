
#OLD 

age= int(input("what\'s  your age ?").strip())
months= age * 12
weeks=months * 4
days=months * 30
hours=days * 24
minutes=hours * 60
seconds=minutes * 60

print(f"{months} months.")
print(f"{weeks:,} weeks.")
print(f"{days:,} days.")
print(f"{hours:,} hours.")
print(f"{minutes:,} minutes.")
print(f"{seconds:,}seconds.")