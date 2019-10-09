# -*- coding:utf-8 -*-
# @Time   : 2019-10-09 18:01
# @Author : liuqian
import os

import cairosvg


def main(input, output):
    cwd = os.getcwd() + input
    output = os.getcwd() + output
    cairosvg.svg2png(url=cwd, write_to=output)


if __name__ == '__main__':
    input = "/flink/flink.svg"
    output = "/flink/flink.png"
    main(input,output)
