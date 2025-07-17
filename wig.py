#!/usr/bin/env python3

from wig.wig import Wig, parse_args

# if called from the command line
if __name__ == '__main__':
    args = parse_args()

    wig = Wig(args)
    wig.run()
