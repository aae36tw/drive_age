#開車年齡
drive = input('你有開過車嗎(有/沒有)?')
if drive != '有' and drive != '沒有':
    print('請再次確認答案，請填答有或沒有')
    raise SystemExit 
age = input('你今年幾歲?')
age = int(age)

if drive == '有':
    if age >= 18:    
        print('沒有問題')
    else:
        print('未成年駕駛')
elif drive == '沒有': 
    if age >= 18:
        print('改考駕照了')
    else:
        print('加油') 
  