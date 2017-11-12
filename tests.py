from algorithms import Number

# inputs
base = 8
input_a = 2355520000
action = '/'
input_b = 2400

# create trve ints in the given base
a = int(str(input_a), base)
b = int(str(input_b), base)

# create Number objects
a_number = Number(str(a), base)
b_number = Number(str(b), base)

# get decimal representations
a_dec = a_number.convert_to_base(10)
b_dec = b_number.convert_to_base(10)

c_dec = eval('a {} b'.format(action))
c_number = Number(str(c_dec), 10)
c = c_number.convert_to_base(base)

# Get complements
a_complement = Number(str(input_a), base).get_complement()
b_complement = Number(str(input_b), base).get_complement()
c_complement = Number(c, base).get_complement()

print('Base:    {a} {action} {b} in base {base} = {c}'.format(a=input_a, b=input_b, action=action, base=base, c=c))
print('Decimal: {a_dec} {action} {b_dec} = {c_dec}'.format(a_dec=a_dec, b_dec=b_dec, action=action, c_dec=c_dec))
print('Complements:\n    a: {a} = {a_complement}\n    b: {b} = {b_complement}\n    c: {c} = {c_complement}'.format(
    a=input_a, a_complement=a_complement, b=input_b, b_complement=b_complement, c=c, c_complement=c_complement
))