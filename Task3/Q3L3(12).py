
def email_silcer(email):
    username = email[:email.index('@')]
    domain_name = email[email.index('@')+1:]
    silce = (f'your username is "{username}" and domain_name is "{domain_name}"')
    return silce
print(email_silcer(input('Enter your Email: ')))
