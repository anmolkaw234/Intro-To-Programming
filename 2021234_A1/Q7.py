cost = float(input())
allowance = float(input())
sf = float(input())
irate = float(input())
savings_per_month = allowance*sf
swr = 0
t = 0
while swr <= cost:
  swr += savings_per_month
  swr += swr*(irate/100)
  t += 1
print(t)
print(swr - cost)
