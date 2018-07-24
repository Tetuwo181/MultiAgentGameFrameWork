# -*- coding: utf-8 -*-
from typing import Callable
from typing import Optional
from typing import Generic

from typing import Tuple
from typing import List
from typing import Union

ACT_DECIDER = Tuple
BEHAVIOR_RESULT = Union[int, float] # 行動した結果を表す型


class Player(object):
    """
    ゲームを行うプレイヤー
    過去の行動結果も記録
    """
    def __init__(self,
                 strategy,
                 name: str = "anonymous"):
        """
        初期化パラメータ
        :param strategy: 具体的な戦略 。引数は戦略を決定する際に必要なパラメータ。返し値は行動
        :param name: プレイヤー名
        """
        self.__strategy = strategy
        self.__name = name #type: str
        self.__record = None #type: List[BEHAVIOR_RESULT]

    @property
    def strategy(self):
        """
        戦略を表すプロパティ
        """
        return self.__strategy

    @property
    def name(self) -> str:
        """
        名前を返すプロパティ
        """
        return self.__name

    @property
    def record(self) -> Optional[List[BEHAVIOR_RESULT]]:
        """
        行動履歴を返すプロパティ
        """
        return self.__record

    @property
    def pre_behavior(self)->Optional[BEHAVIOR_RESULT]:
        """
        最後に取った行動を返す
        """
        if self.record is None:
            return None
        return self.record[-1]

    def act(self, **kwargs)->BEHAVIOR_RESULT:
        """
        戦略に応じて結果を出す
        結果を出した後、行動を記録する
        @param kwargs: 戦略を決めるパラメータ strategyの引数と同じようにする
        @return: 結果
        """
        try:
            result = self.strategy(kwargs)
            return result
        finally:
            if self.__record is None:
                self.__record = [result]
            else:
                self.__record.append(result)



