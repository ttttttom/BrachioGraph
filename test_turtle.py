import pytest

from turtle_draw import BaseTurtle, BrachioGraphTurtle
from brachiograph import BrachioGraph
from base import AbstractWriter


def test_baseturtle():
    bt = BaseTurtle()
    bt.draw_grid()

def test_abstractwriter_with_turtle():
    aw = AbstractWriter(virtual=True, turtle=True)
    aw.box()




bgt = BrachioGraphTurtle(
    inner_arm=9,
    shoulder_centre_angle=-45,
    shoulder_sweep=120,
    outer_arm=7.5,
    elbow_centre_angle=95,
    elbow_sweep=120,
)

bg = BrachioGraph(virtual=True, turtle=True)



def test_grid():
    bgt.draw_grid()


def test_outline():
    bgt.draw_outline()
