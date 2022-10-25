def computer_random_choice():

    import random

    print("컴퓨터가 랜덤으로 가위, 바위, 보 중 하나를 선택합니다..")
    computer = random.randrange(1,4)
    """print(computer)"""           # 1, 2, 3 중 어떤 숫자가 뽑혔는지 확인
    
    if (computer == 1) :
        computer = "가위"

    elif (computer == 2) :
        computer = "바위"

    elif (computer == 3) :
        computer = "보"
    
    return computer

print("컴퓨터는",computer_random_choice(),"를 냈습니다.")
