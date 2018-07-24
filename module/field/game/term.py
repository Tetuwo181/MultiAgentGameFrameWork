# -*- coding: utf-8 -*-

from module.agent import player as PL
from typing import Callable
from typing import Tuple
from typing import Union
from abc import ABCMeta
from abc import abstractmethod

"""
1ターンに1プレイヤーのみが行動するタイプのゲーム

"""


class Game(metaclass=ABCMeta):
    """
    ベースとなるゲーム
    実際にはこれを継承したものを使用する
    """
    def __init__(self):
        pass

    @abstractmethod
    def is_foul(self, **kwargs)->bool:
        """
        反則かどうかを判定する
        引数などは継承先で記述
        """
        pass

    @abstractmethod
    def is_win(self, **kwargs)->bool:
        """
        勝利条件を判定する
        """
        return self.__rule_win

    @abstractmethod
    def one_term(self,
                 player: PL.Player,
                 **kwargs)->PL.BEHAVIOR_RESULT:
        """
        1ターンあたりの行動
        :param player: 行動対象のプレイヤー
        :param kwargs: 行動を決定する際のパラメータ
        :return: ゲームを続けるのであればTrueを、そうでなければ勝者を返す
        """
        pass

    def act_one_player(self,
                       player: PL.Player,
                       **kwargs)->PL.BEHAVIOR_RESULT:
        """
        一人ひとりがそれぞれ行動するゲームの際にここの中身を実装する
        one_termの行動次第ではここを実装しなくてもよい
        :param player: 行動するプレイヤー
        :param kwargs: 行動を決定するパラメータ。引数名はplayer.strategyの引数と同じでなければならない
        :return: 行動した結果
        """
        return player.act(kwargs)
