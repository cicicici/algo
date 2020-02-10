from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

from hopper.debug import log, dump
from hopper.config.config import Config as cfg
from hopper.util.opt import Opt
from hopper.util.context import ctx, get_ctx_list, get_ctx


def process_basic(cl):
    gc = get_ctx(cl)

    log.debug(log.DC.STD, "== Basic, run [{}], comp [{}]".format(gc.opt.run, gc.opt.comp))

