#!/usr/bin/env python

import sys
import pandas as pd

class FileReader(object):
    def __init__(self):
        self.src = []
        self.name = []

    def load_csv_file(self, paths, names):
        data = {}
        for path, name in zip(paths, names):
            print("Loading file: %s" % (name))
            data[name] = pd.read_csv(path)
        return data

    def load_file(self, _input):
        if isinstance(_input, list):
            self.src = _input
        elif isinstance(_input, str):
            self.src = [_input]
        else:
            print("Unsuppotred path format. ")
            return -1
        for src in self.src:
            name = src.split('/')[-1].split('.')[0]
            self.name.append(name)
        return(self.load_csv_file(self.src, self.name))
