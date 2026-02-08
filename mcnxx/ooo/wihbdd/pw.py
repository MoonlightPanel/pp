def password():
 while True:
    p = input('Nhập mật khẩu: ')
    if p == 'pyidler-idlerhadz':
        break
    elif p == '':
        print('Vui lòng nhập mật khẩu!')
    else:
        print('Sai mật khẩu! Vui lòng thử lại!')

password()
