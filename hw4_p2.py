import random
import sys
Preprocessing: Create deck of cards
deck = []
suits=['SPADE', 'HEART', 'DIAMOND','CLUB']
ranks = L'ACE'
for suit in suits:
	for rank in ranks:
	deck.append (rank + '-' + suit)
'7', 'g', 19, '10', 'JACK', 'QUEEN', 'KING'
＃洗牌
random.shuffle (deck)
＃玩家第一輪的牌
Dlarer_ cards = [deck.pop (), deck.pop ()]
＃莊家第一輪的牌
dealer cards = rdeck.pop (), deck.pop ()
岳建立分數清單
player point=rJ
for card in player cards:
	if card.split (T_r)[Ol=='ACE':
		player point.append (11)
	else:
		card.split ('-') [0]==' JACK':
		player point. append (10)
	else:
 		card.split ('-') [0]=='QUEEN'
 		player point.append (10)
	else: card.split ('-') [0]=='KING' 
		player point.append (10)
	else:
		player point. append (int (card.split ('-') (01 ))
player score=sum (player point)
＃檢查用
#print (plaver cards)