#Mums name and age

print ('what is your Mothers name?')
mums_name = raw_input('her name is: ')
print ('how old is %s?') % mums_name
mum_age = input('her age is: ')

# Dads name and age

print ('what is your Fathers name?')
fathers_name = raw_input('his name is: ')
print ('how old is %s?') % fathers_name
fathers_age = input('his age is: ')

# sum and difference of ages

age_sum=fathers_age + mum_age
age_difference=fathers_age - mum_age

print ('the sum of their ages is %s years') % age_sum
print ('the difference in their ages is %d years') % age_difference

