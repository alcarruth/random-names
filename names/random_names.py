#!/usr/bin/python -i
# -*- coding: utf-8 -*-

import random
from name_lists import female_names, male_names, surnames

def random_generator(xs):
    while True:
        random.shuffle(xs)
        for x in xs:
            yield x

def random_name(first_list, last_list):
    first_name = random_generator(first_list)
    last_name = random_generator(last_list)
    while True:
        yield "%s %s" % (first_name.next(), last_name.next())


random_name = random_name(female_names + male_names, surnames)

if __name__ == '__main__':

    import readline
    import rlcompleter
    readline.parse_and_bind("tab: complete")


