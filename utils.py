#!/usr/bin/env python

import sys
import pandas as pd

class FileReader(object):
    def __init__(self):
        self.srcs = []
        self.src = None
        self.names = []
        self.name = None

    def load_csv_file(self, path: str, name: str):
        print("Loading file: %s" % (name), file=sys.stderr)
        return pd.read_csv(path)
    
    def load_csv_file_batch(self, paths: list, names: list):
        data = {}
        for path, name in zip(paths, names):
            data[name] = self.load_csv_file(path, name)
        return data

    def load_file(self, _input, is_batch=False):
        if is_batch:
            self.srcs = _input
            self.names = []
            for src in self.srcs:
                self.src = src
                self.name = self.src.split('/')[-1].split('.')[0]
                self.names.append(self.name)
            return self.load_csv_file_batch(self.srcs, self.names)
        else:
            self.src = _input
            self.name = self.name = self.src.split('/')[-1].split('.')[0]
            return  self.load_csv_file(self.src, self.name)


if __name__ == '__main__':
    reader = FileReader()
    data = reader.load_file('./data/train.csv')
    data = reader.load_file(['./data/train.csv', './data/merchants.csv'], is_batch=True)
