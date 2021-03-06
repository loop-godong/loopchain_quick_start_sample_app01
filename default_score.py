#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import json
from loopchain.blockchain import ScoreBase


class UserScore(ScoreBase):
    """ 기본 체인코드
        기본 체인코드는 아무런 역활을 하지 않는다
    """
    def invoke(self, transaction, block):
        pass

    def query(self, params):
        logging.debug("in UserScore Query...")
        json_params = json.loads(params)
        json_params['test'] = "my test"
        return json.dumps(json_params)

    def info(self):
        # TODO Score info (package.json) 을 로드하여 json object 를 리턴하여야 한다.
        return None
