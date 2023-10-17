from random import choice as ch


def main() -> str:
    n: int = 20000
    for i in range(n):
        print("\033[H\033[J")
        print(round((i/n)*100, 1),'%', 'I'*int((i/n)*100) + '_'*int(100 - int((i/n)*100)))
    print("\033[H\033[J")
    input_list: list[int] or str= input_data()
    if type(input_list) == str:
        return '\033[31m\033[1m {} \033[37m\033[0m'.format("WRONG INPUT")
    result: bool or str = game_process(input_list[0], input_list[1])
    vs: str = f'you - {input_list[0]} vs computer  - {input_list[1]}'
    if result is True:
        print(vs)
        return "\n-------------\033[32m\033[1m  {} \033[37m\033[0m-------------".format("WIN")
    elif result is False:
        print(vs)
        return "\n-------------\033[31m\033[1m  {} \033[37m\033[0m-------------".format("LOST")
    else:
        print(vs)
        return "\n-------------\033[33m\033[1m  {} \033[37m\033[0m-------------".format(result)


def input_data() -> list:
    user_choice: int = \
        int(input(
            "Сделайте выбор — (камень[0], бумага[1], ножницы[2]): "
        ))
    if user_choice == 0 or user_choice == 2 or user_choice == 3:
        pass
    else:
        return "WRONG INPUT"
    computer_choice: int = ch([0, 1, 2])
    return [user_choice, computer_choice]


def game_process(u: int, c: int) -> bool or str:
    if u == c:
        return "NOBODY"
    if is_win(u, c):
        return True
    return False


def is_win(u: int, c: int) -> bool:
    if (u == 0 and c == 2) or \
        (u == 2 and c == 1) or \
        (u == 1 and c == 0):
        return True
    return False

print(main())
