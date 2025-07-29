size = int(input("Please specify the board size: "))

box_mu = "╭――-╮"
box_mr = "|   |"
box_md = "╰―-―╯"

for i in range(size):
    print(box_mu*size)
    print(box_mr*size)
    print(box_md*size)
