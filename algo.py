from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

from hopper.debug import log, dump
from hopper.config.config import Config as cfg
from hopper.util.opt import Opt
from hopper.util.context import ctx, get_ctx_list, get_ctx

from basic.process import process_basic


ARGS = None

class app_cfg(cfg):
    def init_usr_args(self):
        self.args_parser.add_argument('--mode', type=str, help='Execution type, default basic')
        self.args_parser.add_argument('--run', type=str, help='Algorithm to run')
        self.args_parser.add_argument('--comp', action='store_const', const=True, help='Enable compare')

    def default_usr_config(self):
        self.default_set_config('args', 'mode', "basic")
        self.default_set_config('args', 'run', "opt")
        self.default_set_config('args', 'comp', False)

        self.default_set_config('args', 'inst_dir', "r0")
        self.default_set_config('debug', 'level', log.DL.DEBUG)
        #self.default_set_config('debug', 'channel', (log.DC.ALL & ~log.DC.DEV))

def algo_run(opt):
    state = Opt(root=None)
    cl = get_ctx_list(opt=opt, state=state)

    with ctx(cl, None, level=0):
        if opt.mode == 'basic':
            process_basic(cl)

if __name__ == "__main__":
    con = app_cfg(name="Exp Scan")
    ARGS = con.opt.args

    if ARGS.m == 'c':
        sys.exit()

    algo_opt = Opt(mode = ARGS.mode,
                   run = ARGS.run,
                   comp = ARGS.comp)
    algo_run(algo_opt)

