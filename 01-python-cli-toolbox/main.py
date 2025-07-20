# import sys
import argparse
from toolbox_class import  Toolbox

def main():
    toolbox = Toolbox()

    parser = argparse.ArgumentParser(description="🧰 工具箱命令行工具")
    parser.add_argument("command", help="要执行的命令，如：weather / ip / cat")
    parser.add_argument("param", nargs="?", help="可选参数，如城市名")

    args = parser.parse_args()

    # if len(sys.argv) < 2:
    #     print("❗用法：python toolbox.py [命令] [参数]")
    #     print("支持命令：weather <城市> | ip | cat")
    #     return
    #
    # command = sys.argv[1]

    if args.command == "weather":
        if not args.param:
            print("❗请提供城市名称。例如：python toolbox.py weather 北京")
        else:
            toolbox.get_weather(args.param)

    elif args.command == "ip":
        toolbox.get_ip()

    elif args.command == "cat":
        toolbox.get_cat_fact()

    else:
        print(f"❌ 未知命令：{args.command}")
        print("✔ 支持命令：weather <城市> | ip | cat")

if __name__ == "__main__":
    main()