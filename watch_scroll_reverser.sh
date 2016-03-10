#!/bin/bash

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
$DIR/sleep_watcher.py 'killall "Scroll Reverser"; sleep 2; open "/Applications/Scroll Reverser.app"'
