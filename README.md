# JF_SA_phaser

## Contents
index.html was assembled by Sayo inspired by this YouTube tutorial
https://www.youtube.com/watch?v=4dHlbXigtss

test_game.py was added by Jean to run the game

python test_game.py
copies the necessary files to a fresh, uniquely named folder, starts a web server, opens a browser running the game.
(the game should work)

## About phaser versions
The game appears to require an old version of phaser.

python test_game.py old
uses the phaser.min.js from the phaser_old folder, v2.7.10
(the game should work)

python test_game.py new
uses the phaser.min.js from the phaser_new folder, v3.1.2
copied from https://github.com/photonstorm/phaser/blob/v3.1.2/dist/phaser.min.js
(the game does not work)
