from model.point import Point


def main(args = []):

    p1 = Point(3,5)
    p2 = Point(3,5)

    print(p1+p2)

    if(p1 == p2):
        print("São Iguais")
    else:
        print("são diferentes")

if __name__ == "__main__":
    main()
