from data import *


def main():
    get_page("https://www.3dmgame.com/news/game/", "", "let")
    run_compile_page("data", "GameNews")
    run_server()


if __name__ == "__main__":
    main()
