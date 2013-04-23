# requires Requests
import json
import requests
from board import Board
from time import sleep
from pprint import pprint

FIREBASE_URL    = 'https://quantumj.firebaseIO.com/'
MAIN_BOARD_NAME = 'main_board'
SECS_TO_SLEEP   = 5

while True:
    bd = Board()
    board_state = bd.get_board()

    print 'Using the following board:'
    pprint(board_state)

    payload = json.dumps({MAIN_BOARD_NAME: board_state})
    print 'Sending the following payload: %s' % payload

    response = requests.put(FIREBASE_URL + '.json', data=payload)

    print 'Done.'
    print 'Request body: %s' % response.text

    sleep(SECS_TO_SLEEP)