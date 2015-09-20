__author__ = 'dfields'

import trello

API_KEY = 'cc0f13b21cedc64a5a64878eda654ce8'
### The AUTH key needs to be reset. Currently done manually
AUTH_KEY = '8b26e0e0831556feead41d7fc3af5debc77a2984faad5543960272da6410b246'
PKB_ID = '55dd03c28b4efd740fd64e69'
# Secret:a3dbbc2923da49117c1ac34c14292fa8b40e1c78e8ea30bb55c500dc30d6782b

def main():
    tapi = trello.TrelloApi(API_KEY)
    tapi.set_token(AUTH_KEY)

#    pk_board = tapi.boards.get(PKB_ID, lists='open',fields='name',list_fields='name')

#    for l in pk_board['lists']:
#        print("{}:{}".format(l['id'],l['name']))

    # This shows the card updates as they moved from one list to another
    pk_board = tapi.boards.get_action(PKB_ID,filter='updateCard:idList',fields='date,data')
    for act in pk_board:
         print("{}:{} -> {}".format(act['date'],act['data']['listBefore']['name'],act['data']['listAfter']['name']))
        #print(act['data']['listBefore'])

if __name__ == '__main__':
    main()

