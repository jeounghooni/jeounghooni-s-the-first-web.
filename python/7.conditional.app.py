input_id = input('아이디를 입력해주세요.')
input_pwd = input('비밀번호를 입력해주세요.')
if input_id == 'kasumigaoka' :
    if input_pwd == '1234' :
        print('반갑습니다.')
    else:
        print('비밀번호가 다릅니다.')
else:
    print('등록되지 않은 계정입니다. 아이를 확인해주십시요.')