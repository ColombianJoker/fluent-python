# %% 1
class Vowels:
    def __getitem__(self, i):
        return 'AEIOU'[i]

v = Vowels()

# %% 2
print(f"{v[0]=}")

# %% 3
print(f"{v[1]=}")

for c in v:
    print(c)
