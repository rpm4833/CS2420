work = [0, 0, 0]

def move(n, f, t, o):
    if n == 1:
        print("Move 1 disk from tower", f, "to tower", t)
        work[1] += 1
    else:
        work[2] += 1
        move(n-1, f, o, t)
        move(1, f, t, o)
        move(n-1, o, t, f)
    work[0] += 1

def main():
    n = 40
    move(n, 1, 2, 3)

if __name__ == "__main__":
    main()
    print(work)
    print(work[0] == (work[1] + work[2]))