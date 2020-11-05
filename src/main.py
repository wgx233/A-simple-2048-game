from tkinter import *
from tkinter.font import Font
from Game import *

key_map = {'Up': UP, 'Down': DOWN, 'Left': LEFT, 'Right': RIGHT}
color_map = {2: ('#776e65', '#eee4da'), 4: ('#776e65', '#ede0c8'), 8: ('#f9f6f2', '#f2b179'), 16: ('#f9f6f2', '#f2b179'),
            32: ('#f9f6f2', '#f67c5f'), 64: ('#f9f6f2', '#f65e3b'), 128: ('#f9f6f2', '#edcf72'), 256: ('#f9f6f2', '#edcc61'),
            512: ('#f9f6f2', '#edc850'), 1024: ('#f9f6f2', '#edc53f'), 2048: ('#f9f6f2', '#edc22e'), 'base': '#ccc0b3'}
color_map.update(dict.fromkeys(
    [2**x for x in range(12, 18)], ('#f9f6f2', '#3c3a32')))


def KeyInput(event, game, tk_root, labels):
    key = '{}'.format(event.keysym)
    if key in key_map and game and labels and tk_root and game.notOver():
        if game.Move(key_map[key]):
            grid, score = game.getGrid(), game.getScore()
            max_tile = game.getMax()
            if max_tile == 2048:
                tk_root.title('你真是太牛逼了!!!  继续加油!!!')
            else:
                tk_root.title('快! 你下一个目标是 {}!   当前分数: {}'.format(max_tile * 2, score))
            for i in range(0, ROW):
                for j in range(0, COL):
                    val = grid[i][j]
                    text = '{}'.format('' if val == 0 else val)
                    if val == 0:    font_color = color_map['base']
                    elif val < 10:  font_color = color_map[32][1]
                    else:   font_color = color_map[val][0]
                    labels[COL*i+j].config(text=text, fg=font_color, bg=color_map['base'] if val == 0 else color_map[val][1])
        else:
            grid, score = game.getGrid(), game.getScore()
            max_tile = game.getMax()
            new_root = Tk()
            new_root.geometry('200x100+250+300')
            new_root.title('没了啊, 老板')
            l = Label(new_root, text = '游戏结束\n继续加油啊!!!', bg = color_map['base'], font = ('楷体', 18), width = 30, height = 30)
            l.pack()
            tk_root.title('Game Over! 你获得的最大数: {}, 分数: {}'.format(max_tile, score))


if __name__ == '__main__':
    game, root, window_size = Game(), Tk(), 400
    root.title('快! 你的目标是 2048!   当前分数: 0')
    root.geometry('{0}x{0}+150+150'.format(window_size))
    root.config(background='#bbada0')

    grid, labels = game.getGrid(), []
    for i in range(0, ROW):
        for j in range(0, COL):
            frame = Frame(root, width = window_size // COL - 2, height = window_size // ROW - 2)
            font = Font(family = 'Helvetica', weight = 'bold', size = window_size // 15)
            frame.pack_propagate(0)
            frame.place(x = j * window_size // ROW + 1, y = i * window_size // COL + 1)
            val = grid[i][j]
            (text, color) = ('', color_map['base']) if val == 0 else (val, color_map[val][0])
            label = Label(frame, text = text, font = font, fg = color, bg = color_map['base'] if val == 0 else color_map[val][1])
            label.pack(fill = BOTH, expand = True)
            labels.append(label)

    root.bind_all('<Key>', lambda event: KeyInput(event, game, root, labels))
    root.mainloop()
