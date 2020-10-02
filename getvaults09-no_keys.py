from web3 import Web3
import time
import numpy as np
from numpy import array
import json
import requests
from random import *
import configparser
import pickle
import sys
import argparse
import csv
import datetime
import math


web3 = Web3(Web3.HTTPProvider('http://192.168.0.40:8545'))
#web3_infura = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/fc'))



cc_eth_root_url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=ETH&tsym=USD&e=Coinbase&limit=1'
cc_bat_root_url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BAT&tsym=USDC&e=Coinbase&limit=1'
cc_key = '&api_key=03d'

USDC_SCALE = 1000000
WBTC_SCALE = 100000000
ETH_SCALE = 1000000000000000000
ETH27_SCALE = 1000000000000000000000000000
ETH44_SCALE = 1000000000000000000000000000000000000000000000

FIRST_BLOCK = 8920000
#FIRST_BLOCK = 9100000
LAST_BLOCK = 9000000


vat0x = '0x35D1b3F3D7966A1DFe207aa4514C12a259A0492B'
flippermom0x = '0x9BdDB99625A711bf9bda237044924E34E8570f75'
ethAflip0xv0 = '0xd8a04F5412223F513DC55F839574430f5EC15531'
ethAflip0xv1 = '0x0F398a2DaAa134621e4b687FCcfeE4CE47599Cc1'
ethAflip0xv2 = '0xF32836B9E1f47a0515c6Ec431592D5EbC276407f'
batAflip0xv0 = '0xaA745404d55f88C108A28c86abE7b5A1E7817c07'
batAflip0xv1 = '0x5EdF770FC81E7b8C2c89f71F30f211226a4d7495'
batAflip0xv2 = '0xF7C569B2B271354179AaCC9fF1e42390983110BA'
usdcAflip0xv0 = '0xE6ed1d09a19Bd335f051d78D5d22dF3bfF2c28B1'
usdcAflip0xv1 = '0x545521e0105C5698f75D6b3C3050CfCC62FB0C12'
usdcAflip0xv2 = '0xbe359e53038E41a1ffA47DAE39645756C80e557a'
usdcBflip0xv0 = '0xec25Ca3fFa512afbb1784E17f1D414E16D01794F'
usdcBflip0xv1 = '0x6002d3B769D64A9909b0B26fC00361091786fe48'
usdcBflip0xv2 = '0x77282aD36aADAfC16bCA42c865c674F108c4a616'
wbtcAflip0xv0 = '0x3E115d85D4d7253b05fEc9C0bB5b08383C2b0603'
wbtcAflip0xv1 = '0xF70590Fa4AaBe12d3613f5069D02B8702e058569'
wbtcAflip0xv2 = '0x58CD24ac7322890382eE45A3E4F903a5B22Ee930'
tusdAflip0xv0 = '0xba3f6a74BD12Cf1e48d4416c7b50963cA98AfD61'
tusdAflip0xv1 = '0x04C42fAC3e29Fd27118609a5c36fD0b3Cb8090b3'
tusdAflip0xv2 = '0x9E4b213C4defbce7564F2Ac20B6E3bF40954C440'
zrxAflip0xv0 = '0x08c89251FC058cC97d5bA5F06F95026C0A5CF9B0'
zrxAflip0xv1 = '0x92645a34d07696395b6e5b8330b000D0436A9aAD'
zrxAflip0xv2 = '0xa4341cAf9F9F098ecb20fb2CeE2a0b8C78A18118'
kncAflip0xv0 = '0xAbBCB9Ae89cDD3C27E02D279480C7fF33083249b'
kncAflip0xv1 = '0xAD4a0B5F3c6Deb13ADE106Ba6E80Ca6566538eE6'
kncAflip0xv2 = '0x57B01F1B3C59e2C0bdfF3EC9563B71EEc99a3f2f'
manaAflip0xv1 = '0x4bf9D2EBC4c57B9B783C12D30076507660B58b3a'
manaAflip0xv2 = '0x0a1D75B4f49BA80724a214599574080CD6B68357'
usdtAflip0xv2 = '0x667F41d0fDcE1945eE0f56A79dd6c142E37fCC26'
paxAflip0xv2 = '0x52D5D1C05CC79Fc24A629Cb24cB06C5BE5d766E7'

ilk_registry = '0x8b4ce5DCbb01e0e1f0521cd8dCfb31B308E52c24'
osm_mom = '0x76416A4d5190d071bfed309861527431304aA14f'
cat0x = '0xa5679C04fc3d9d8b0AaB1F0ab83555b301cA70Ea'
spotter0x = '0x65C79fcB50Ca1594B025960e539eD7A9a6D434A3'
osmweth0x = '0x81FE72B5A8d1A857d176C3E7d5Bd2679A9B85763'
osmbat0x = '0xB4eb54AF9Cc7882DF0121d26c5b97E802915ABe6'
vaultmanager0x = '0x5ef30b9986345249bc32d8928B7ee64DE9435E39'
daijoin0x = '0x9759A6Ac90977b93B58547b4A71c78317f391A28'
migrationdaijoin0x = '0xad37fd42185Ba63009177058208dd1be4b136e6b'
dsproxycache0x = '0x271293c67E2D3140a0E9381EfF1F9b01E07B0795'
#oasiscdpmanager = '0x60762005BE465901cA18BA34416B35143De72c0c'
instaindex0x = '0x2971AdFa57b20E5a416aE5a708A8655A9c74f723'
instaregistry0x = '0x498b3BfaBE9F73db90D252bCD4Fa9548Cd0Fd981'
ethdaiuniswapstaking0x = '0xa1484C3aa22a66C62b77E0AE78E15258bd0cB711'
ethdaiuniswap0x = '0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11'
ydaidaiuniswap0x = '0x94cDd18F53a8f3EC9A3Ec0CBE897aED5ea009c43'
daiusdcuniswap0x = '0xAE461cA67B15dc8dc81CE7615e0320dA1A9aB8D5'
daiusdtuniswap0x = '0xB20bd5D04BE54f870D5C0d3cA85d82b34B836405'
unilplist = [ethdaiuniswap0x, ydaidaiuniswap0x, daiusdcuniswap0x, daiusdtuniswap0x]

balancersafe = '0x3031745E732dcE8fECccc94AcA13D5fa18F1012d'
balancerethdai = '0x99e582374015c1d2F3C0f98d0763B4B1145772B7'
balanceryfi = '0x16cAC1403377978644e78769Daa49d8f6B6CF565'
balancerlplist = [balancersafe, balancerethdai, balanceryfi]

weth0x = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
dai0x = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
usdc0x = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
bat0x = '0x0D8775F648430679A709E98d2b0Cb6250d2887EF'
wbtc0x = '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599'
tusd0x = '0x0000000000085d4780B73119b644AE5ecd22b376'
zrx0x = '0xE41d2489571d322189246DaFA5ebDe1F4699F498'
knc0x = '0xdd974D5C2e2928deA5F71b9825b8b646686BD200'
mana0x = '0x0F5D2fB29fb7d3CFeE444a200298f468908cC942'
usdt0x = '0xdAC17F958D2ee523a2206206994597C13D831ec7'
pax0x = '0x8E870D67F660D95d5be530380D0eC0bd388289E1'






ceth0x = '0x4Ddc2D193948926D02f9B1fE9e1daa0718270ED5'
cdai0x = '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643'
cusdc0x = '0x39AA39c021dfbaE8faC545936693aC917d5E7563'
cbat0x = '0x6C8c6b02E7b2BE14d4fA6022Dfd6d75921D90E4E'
cusdt0x = '0xf650C3d88D12dB855b8bf7D11Be6C55A4e07dCC9'
czrx0x = '0xB3319f5D18Bc0D84dD1b4825Dcde5d5f7266d407'
cwbtc0x = '0xC11b1268C1A384e55C48c2391d8d480264A3A7F4'
crep0x = '0x158079Ee67Fce2f58472A96584A73C7Ab9AC95c1'
ctokenlist = [ceth0x, cdai0x, cusdc0x, cbat0x, cusdt0x, czrx0x, cwbtc0x, crep0x]

curvecomp0x = '0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56'
curveusdt0x = '0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C'
curvey0x = '0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51'
curvebusd0x = '0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27'
curvesusd0x = '0xA5407eAE9Ba41422680e2e00537571bcC53efBfD'
curvepax0x = '0x06364f10B501e868329afBc005b3492902d6C763'
curve30x = '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'
curvelist = [curvecomp0x, curveusdt0x, curvey0x, curvebusd0x, curvesusd0x, curvepax0x, curve30x]

aeth0x = '0x3a3A65aAb0dd2A17E3F1947bA16138cd37d08c04'
adai0x = '0xfC1E690f61EFd961294b3e1Ce3313fBD8aa4f85d'
ausdc0x = '0x9bA00D6856a4eDF4665BcA2C2309936572473B7E'
asusd0x = '0x625aE63000f46200499120B906716420bd059240'
atusd0x = '0x4DA9b813057D04BAef4e5800E36083717b4a0341'
ausdt0x = '0x71fc860F7D3A592A4a98740e39dB31d25db65ae8'
abusd0x = '0x6Ee0f7BB50a54AB5253dA0667B0Dc2ee526C30a8'
abat0x = '0xE1BA0FB44CCb0D11b80F92f4f8Ed94CA3fF51D00'
aenj0x = '0x712DB54daA836B53Ef1EcBb9c6ba3b9Efb073F40'
aknc0x = '0x9D91BE44C06d373a8a226E1f3b146956083803eB'
alend0x = '0x7D2D3688Df45Ce7C552E19c27e007673da9204B8'
alink0x = '0xA64BD6C70Cb9051F6A9ba1F163Fdc07E0DfB5F84'
amana0x = '0x6FCE4A401B6B80ACe52baAefE4421Bd188e76F6f'
amkr0x = '0x7deB5e830be29F91E298ba5FF1356BB7f8146998'
aren0x = '0x69948cC03f478B95283F7dbf1CE764d0fc7EC54C'
arep0x = '0x71010A9D003445aC60C4e6A7017c1E89A477B438'
asnx0x = '0x328C4c80BC7aCa0834Db37e6600A6c49E12Da4DE'
awbtc0x = '0xFC4B8ED459e00e5400be803A9BB3954234FD50e3'
ayfi0x = '0x12e51E77DAAA58aA0E9247db7510Ea4B46F9bEAd'
azrx0x = '0x6Fb0855c404E09c47C3fBCA25f08d4E41f9F062f'
atokenlist = [aeth0x, adai0x, ausdc0x, asusd0x, atusd0x, ausdt0x, abusd0x, abat0x, aenj0x, aknc0x, alend0x, alink0x, amana0x, amkr0x, aren0x, arep0x, asnx0x, awbtc0x, ayfi0x, azrx0x]

wethAjoin0x = '0x2F0b23f53734252Bda2277357e97e1517d6B042A'
batAjoin0x = '0x3D0B1912B66114d4096F48A8CEe3A56C231772cA'
usdcAjoin0x = '0xA191e578a6736167326d05c119CE0c90849E84B7'
usdcBjoin0x = '0x2600004fd1585f7270756DDc88aD9cfA10dD0428'
wbtcAjoin0x = '0xBF72Da2Bd84c5170618Fbe5914B0ECA9638d5eb5'
tusdAjoin0x = '0x4454aF7C8bb9463203b66C816220D41ED7837f44'
zrxAjoin0x = '0xc7e8Cd72BDEe38865b4F5615956eF47ce1a7e5D0'
kncAjoin0x = '0x475F1a89C1ED844A08E8f6C50A00228b5E59E4A9'
manaAjoin0x = '0xA6EA3b9C04b8a38Ff5e224E7c3D6937ca44C0ef9'
usdtAjoin0x = '0x0Ac6A1D74E84C2dF9063bDDc31699FF2a2BB22A2'
paxAjoin0x = '0x7e62B7E279DFC78DEB656E34D6a435cC08a44666'



ethAflipabiv0 = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"},{"internalType":"bytes32","name":"ilk_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lot","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"gal","type":"address"}],"name":"Kick","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"beg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bids","outputs":[{"internalType":"uint256","name":"bid","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint48","name":"tic","type":"uint48"},{"internalType":"uint48","name":"end","type":"uint48"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"deal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"dent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ilk","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"kick","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kicks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tau","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"tend","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tick","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ttl","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"yank","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
batAflipabiv0 = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"},{"internalType":"bytes32","name":"ilk_","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lot","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"bid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"gal","type":"address"}],"name":"Kick","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"beg","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"bids","outputs":[{"internalType":"uint256","name":"bid","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"address","name":"guy","type":"address"},{"internalType":"uint48","name":"tic","type":"uint48"},{"internalType":"uint48","name":"end","type":"uint48"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"deal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"dent","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ilk","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"address","name":"gal","type":"address"},{"internalType":"uint256","name":"tab","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"kick","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kicks","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"tau","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"lot","type":"uint256"},{"internalType":"uint256","name":"bid","type":"uint256"}],"name":"tend","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"tick","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"ttl","outputs":[{"internalType":"uint48","name":"","type":"uint48"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"yank","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
catabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"ilk","type":"bytes32"},{"indexed":true,"internalType":"address","name":"urn","type":"address"},{"indexed":false,"internalType":"uint256","name":"ink","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"art","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tab","type":"uint256"},{"indexed":false,"internalType":"address","name":"flip","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"Bite","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"urn","type":"address"}],"name":"bite","outputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"data","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"address","name":"flip","type":"address"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"ilks","outputs":[{"internalType":"address","name":"flip","type":"address"},{"internalType":"uint256","name":"chop","type":"uint256"},{"internalType":"uint256","name":"lump","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"contract VatLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vow","outputs":[{"internalType":"contract VowLike","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
vatabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg3","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"constant":true,"inputs":[],"name":"Line","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"cage","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"can","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"dai","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"debt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"deny","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"what","type":"bytes32"},{"internalType":"uint256","name":"data","type":"uint256"}],"name":"file","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"int256","name":"rate","type":"int256"}],"name":"fold","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"fork","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"address","name":"w","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"frob","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"},{"internalType":"address","name":"","type":"address"}],"name":"gem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"i","type":"bytes32"},{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"address","name":"w","type":"address"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"grab","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"heal","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"hope","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"ilks","outputs":[{"internalType":"uint256","name":"Art","type":"uint256"},{"internalType":"uint256","name":"rate","type":"uint256"},{"internalType":"uint256","name":"spot","type":"uint256"},{"internalType":"uint256","name":"line","type":"uint256"},{"internalType":"uint256","name":"dust","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"}],"name":"init","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"live","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"nope","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"}],"name":"rely","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"sin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"int256","name":"wad","type":"int256"}],"name":"slip","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"u","type":"address"},{"internalType":"address","name":"v","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"suck","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"},{"internalType":"address","name":"","type":"address"}],"name":"urns","outputs":[{"internalType":"uint256","name":"ink","type":"uint256"},{"internalType":"uint256","name":"art","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
vaultmanagerabi = json.loads('[{"inputs":[{"internalType":"address","name":"vat_","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"usr","type":"address"},{"indexed":true,"internalType":"address","name":"own","type":"address"},{"indexed":true,"internalType":"uint256","name":"cdp","type":"uint256"}],"name":"NewCdp","type":"event"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"ok","type":"uint256"}],"name":"cdpAllow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"cdpCan","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"cdpi","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"count","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"uint256","name":"cdp","type":"uint256"}],"name":"enter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"first","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"flux","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"int256","name":"dink","type":"int256"},{"internalType":"int256","name":"dart","type":"int256"}],"name":"frob","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"}],"name":"give","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"ilks","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"last","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"list","outputs":[{"internalType":"uint256","name":"prev","type":"uint256"},{"internalType":"uint256","name":"next","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"rad","type":"uint256"}],"name":"move","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes32","name":"ilk","type":"bytes32"},{"internalType":"address","name":"usr","type":"address"}],"name":"open","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"owns","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdp","type":"uint256"},{"internalType":"address","name":"dst","type":"address"}],"name":"quit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"cdpSrc","type":"uint256"},{"internalType":"uint256","name":"cdpDst","type":"uint256"}],"name":"shift","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"ok","type":"uint256"}],"name":"urnAllow","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"urnCan","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"urns","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"vat","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
dsproxyabi = json.loads('[{"constant":false,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_target","type":"address"},{"name":"_data","type":"bytes"}],"name":"execute","outputs":[{"name":"response","type":"bytes32"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":false,"inputs":[{"name":"_code","type":"bytes"},{"name":"_data","type":"bytes"}],"name":"execute","outputs":[{"name":"target","type":"address"},{"name":"response","type":"bytes32"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"cache","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_cacheAddr","type":"address"}],"name":"setCache","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_cacheAddr","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":true,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":true,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]')
instaaccountabi1 = json.loads('[{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"origin","type":"address"}],"name":"LogAccountCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_newAccount","type":"address"},{"indexed":true,"internalType":"address","name":"_connectors","type":"address"},{"indexed":true,"internalType":"address","name":"_check","type":"address"}],"name":"LogNewAccount","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"accountVersion","type":"uint256"},{"indexed":true,"internalType":"address","name":"check","type":"address"}],"name":"LogNewCheck","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"master","type":"address"}],"name":"LogNewMaster","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"master","type":"address"}],"name":"LogUpdateMaster","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"account","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_newAccount","type":"address"},{"internalType":"address","name":"_connectors","type":"address"},{"internalType":"address","name":"_check","type":"address"}],"name":"addNewAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"accountVersion","type":"uint256"},{"internalType":"address","name":"_origin","type":"address"}],"name":"build","outputs":[{"internalType":"address","name":"_account","type":"address"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"},{"internalType":"uint256","name":"accountVersion","type":"uint256"},{"internalType":"address[]","name":"_targets","type":"address[]"},{"internalType":"bytes[]","name":"_datas","type":"bytes[]"},{"internalType":"address","name":"_origin","type":"address"}],"name":"buildWithCast","outputs":[{"internalType":"address","name":"_account","type":"address"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"accountVersion","type":"uint256"},{"internalType":"address","name":"_newCheck","type":"address"}],"name":"changeCheck","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_newMaster","type":"address"}],"name":"changeMaster","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"check","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"connectors","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"version","type":"uint256"},{"internalType":"address","name":"query","type":"address"}],"name":"isClone","outputs":[{"internalType":"bool","name":"result","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"list","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"master","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_master","type":"address"},{"internalType":"address","name":"_list","type":"address"},{"internalType":"address","name":"_account","type":"address"},{"internalType":"address","name":"_connectors","type":"address"}],"name":"setBasics","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"updateMaster","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"versionCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
instaaccountabi2 = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"origin","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"LogCast","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"LogDisable","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"LogEnable","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"_shield","type":"bool"}],"name":"LogSwitchShield","type":"event"},{"inputs":[{"internalType":"address[]","name":"_targets","type":"address[]"},{"internalType":"bytes[]","name":"_datas","type":"bytes[]"},{"internalType":"address","name":"_origin","type":"address"}],"name":"cast","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"disable","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"enable","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"instaIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"isAuth","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"shield","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"_shield","type":"bool"}],"name":"switchShield","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"version","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
userwalletabi = json.loads('[{"constant":false,"inputs":[{"name":"nextOwner","type":"address"}],"name":"setOwner","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"src","type":"address"}],"name":"isAuth","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"registry","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_target","type":"address"},{"name":"_data","type":"bytes"},{"name":"_src","type":"uint256"},{"name":"_session","type":"uint256"}],"name":"execute","outputs":[{"name":"response","type":"bytes"}],"payable":true,"stateMutability":"payable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"target","type":"address"},{"indexed":false,"name":"srcNum","type":"uint256"},{"indexed":false,"name":"sessionNum","type":"uint256"}],"name":"LogExecute","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"sig","type":"bytes4"},{"indexed":true,"name":"guy","type":"address"},{"indexed":true,"name":"foo","type":"bytes32"},{"indexed":false,"name":"bar","type":"bytes32"},{"indexed":false,"name":"wad","type":"uint256"},{"indexed":false,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"}]')
cdaiabi = json.loads('[{"inputs":[{"internalType":"address","name":"underlying_","type":"address"},{"internalType":"contract ComptrollerInterface","name":"comptroller_","type":"address"},{"internalType":"contract InterestRateModel","name":"interestRateModel_","type":"address"},{"internalType":"uint256","name":"initialExchangeRateMantissa_","type":"uint256"},{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"uint8","name":"decimals_","type":"uint8"},{"internalType":"address payable","name":"admin_","type":"address"},{"internalType":"address","name":"implementation_","type":"address"},{"internalType":"bytes","name":"becomeImplementationData","type":"bytes"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"cashPrior","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"interestAccumulated","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"borrowIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"AccrueInterest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"borrower","type":"address"},{"indexed":false,"internalType":"uint256","name":"borrowAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrows","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"Borrow","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"error","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"info","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"detail","type":"uint256"}],"name":"Failure","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"liquidator","type":"address"},{"indexed":false,"internalType":"address","name":"borrower","type":"address"},{"indexed":false,"internalType":"uint256","name":"repayAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"cTokenCollateral","type":"address"},{"indexed":false,"internalType":"uint256","name":"seizeTokens","type":"uint256"}],"name":"LiquidateBorrow","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"minter","type":"address"},{"indexed":false,"internalType":"uint256","name":"mintAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"mintTokens","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"NewAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contract ComptrollerInterface","name":"oldComptroller","type":"address"},{"indexed":false,"internalType":"contract ComptrollerInterface","name":"newComptroller","type":"address"}],"name":"NewComptroller","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldImplementation","type":"address"},{"indexed":false,"internalType":"address","name":"newImplementation","type":"address"}],"name":"NewImplementation","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"contract InterestRateModel","name":"oldInterestRateModel","type":"address"},{"indexed":false,"internalType":"contract InterestRateModel","name":"newInterestRateModel","type":"address"}],"name":"NewMarketInterestRateModel","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldPendingAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newPendingAdmin","type":"address"}],"name":"NewPendingAdmin","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldReserveFactorMantissa","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newReserveFactorMantissa","type":"uint256"}],"name":"NewReserveFactor","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"redeemer","type":"address"},{"indexed":false,"internalType":"uint256","name":"redeemAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"redeemTokens","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"payer","type":"address"},{"indexed":false,"internalType":"address","name":"borrower","type":"address"},{"indexed":false,"internalType":"uint256","name":"repayAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"accountBorrows","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"totalBorrows","type":"uint256"}],"name":"RepayBorrow","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"benefactor","type":"address"},{"indexed":false,"internalType":"uint256","name":"addAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTotalReserves","type":"uint256"}],"name":"ReservesAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"admin","type":"address"},{"indexed":false,"internalType":"uint256","name":"reduceAmount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newTotalReserves","type":"uint256"}],"name":"ReservesReduced","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Transfer","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":false,"inputs":[],"name":"_acceptAdmin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"addAmount","type":"uint256"}],"name":"_addReserves","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"reduceAmount","type":"uint256"}],"name":"_reduceReserves","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"contract ComptrollerInterface","name":"newComptroller","type":"address"}],"name":"_setComptroller","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"implementation_","type":"address"},{"internalType":"bool","name":"allowResign","type":"bool"},{"internalType":"bytes","name":"becomeImplementationData","type":"bytes"}],"name":"_setImplementation","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"contract InterestRateModel","name":"newInterestRateModel","type":"address"}],"name":"_setInterestRateModel","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address payable","name":"newPendingAdmin","type":"address"}],"name":"_setPendingAdmin","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"newReserveFactorMantissa","type":"uint256"}],"name":"_setReserveFactor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"accrualBlockNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"accrueInterest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"admin","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOfUnderlying","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"borrowAmount","type":"uint256"}],"name":"borrow","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"borrowBalanceCurrent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"borrowBalanceStored","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"borrowRatePerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"comptroller","outputs":[{"internalType":"contract ComptrollerInterface","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],"name":"delegateToImplementation","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes","name":"data","type":"bytes"}],"name":"delegateToViewImplementation","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"exchangeRateCurrent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"exchangeRateStored","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getAccountSnapshot","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCash","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"interestRateModel","outputs":[{"internalType":"contract InterestRateModel","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isCToken","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"repayAmount","type":"uint256"},{"internalType":"contract CTokenInterface","name":"cTokenCollateral","type":"address"}],"name":"liquidateBorrow","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"mintAmount","type":"uint256"}],"name":"mint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"pendingAdmin","outputs":[{"internalType":"address payable","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"redeemTokens","type":"uint256"}],"name":"redeem","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"redeemAmount","type":"uint256"}],"name":"redeemUnderlying","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"repayAmount","type":"uint256"}],"name":"repayBorrow","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"repayAmount","type":"uint256"}],"name":"repayBorrowBehalf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"reserveFactorMantissa","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"liquidator","type":"address"},{"internalType":"address","name":"borrower","type":"address"},{"internalType":"uint256","name":"seizeTokens","type":"uint256"}],"name":"seize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"supplyRatePerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalBorrows","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"totalBorrowsCurrent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalReserves","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"underlying","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
aethabi = json.loads('[{"inputs":[{"internalType":"contract LendingPoolAddressesProvider","name":"_addressesProvider","type":"address"},{"internalType":"address","name":"_underlyingAsset","type":"address"},{"internalType":"uint8","name":"_underlyingAssetDecimals","type":"uint8"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_toBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_toIndex","type":"uint256"}],"name":"BalanceTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromIndex","type":"uint256"}],"name":"BurnOnLiquidation","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"}],"name":"InterestRedirectionAllowanceChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_redirectedBalance","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromIndex","type":"uint256"}],"name":"InterestStreamRedirected","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromIndex","type":"uint256"}],"name":"MintOnDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_fromIndex","type":"uint256"}],"name":"Redeem","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_targetAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"_targetBalanceIncrease","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_targetIndex","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_redirectedBalanceAdded","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"_redirectedBalanceRemoved","type":"uint256"}],"name":"RedirectedBalanceUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"UINT_MAX_VALUE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"allowInterestRedirectionTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"burnOnLiquidation","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getInterestRedirectionAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getRedirectedBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"isTransferAllowed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_account","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mintOnDeposit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"principalBalanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"redeem","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_to","type":"address"}],"name":"redirectInterestStream","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"}],"name":"redirectInterestStreamOf","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferOnLiquidation","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"underlyingAssetAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"}]')
ethdaiunilpabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
balancerlpabi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"dst","type":"address"},{"indexed":false,"internalType":"uint256","name":"amt","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":false,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LOG_CALL","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":true,"internalType":"address","name":"tokenOut","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmountOut","type":"uint256"}],"name":"LOG_EXIT","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":true,"internalType":"address","name":"tokenIn","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmountIn","type":"uint256"}],"name":"LOG_JOIN","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"caller","type":"address"},{"indexed":true,"internalType":"address","name":"tokenIn","type":"address"},{"indexed":true,"internalType":"address","name":"tokenOut","type":"address"},{"indexed":false,"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"tokenAmountOut","type":"uint256"}],"name":"LOG_SWAP","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"src","type":"address"},{"indexed":true,"internalType":"address","name":"dst","type":"address"},{"indexed":false,"internalType":"uint256","name":"amt","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"BONE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"BPOW_PRECISION","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"EXIT_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"INIT_POOL_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_BOUND_TOKENS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_BPOW_BASE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_IN_RATIO","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_OUT_RATIO","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_TOTAL_WEIGHT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MAX_WEIGHT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MIN_BALANCE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MIN_BOUND_TOKENS","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MIN_BPOW_BASE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MIN_FEE","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MIN_WEIGHT","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"whom","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"denorm","type":"uint256"}],"name":"bind","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceIn","type":"uint256"},{"internalType":"uint256","name":"tokenWeightIn","type":"uint256"},{"internalType":"uint256","name":"tokenBalanceOut","type":"uint256"},{"internalType":"uint256","name":"tokenWeightOut","type":"uint256"},{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcInGivenOut","outputs":[{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceIn","type":"uint256"},{"internalType":"uint256","name":"tokenWeightIn","type":"uint256"},{"internalType":"uint256","name":"tokenBalanceOut","type":"uint256"},{"internalType":"uint256","name":"tokenWeightOut","type":"uint256"},{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcOutGivenIn","outputs":[{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceOut","type":"uint256"},{"internalType":"uint256","name":"tokenWeightOut","type":"uint256"},{"internalType":"uint256","name":"poolSupply","type":"uint256"},{"internalType":"uint256","name":"totalWeight","type":"uint256"},{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcPoolInGivenSingleOut","outputs":[{"internalType":"uint256","name":"poolAmountIn","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceIn","type":"uint256"},{"internalType":"uint256","name":"tokenWeightIn","type":"uint256"},{"internalType":"uint256","name":"poolSupply","type":"uint256"},{"internalType":"uint256","name":"totalWeight","type":"uint256"},{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcPoolOutGivenSingleIn","outputs":[{"internalType":"uint256","name":"poolAmountOut","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceIn","type":"uint256"},{"internalType":"uint256","name":"tokenWeightIn","type":"uint256"},{"internalType":"uint256","name":"poolSupply","type":"uint256"},{"internalType":"uint256","name":"totalWeight","type":"uint256"},{"internalType":"uint256","name":"poolAmountOut","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcSingleInGivenPoolOut","outputs":[{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceOut","type":"uint256"},{"internalType":"uint256","name":"tokenWeightOut","type":"uint256"},{"internalType":"uint256","name":"poolSupply","type":"uint256"},{"internalType":"uint256","name":"totalWeight","type":"uint256"},{"internalType":"uint256","name":"poolAmountIn","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcSingleOutGivenPoolIn","outputs":[{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenBalanceIn","type":"uint256"},{"internalType":"uint256","name":"tokenWeightIn","type":"uint256"},{"internalType":"uint256","name":"tokenBalanceOut","type":"uint256"},{"internalType":"uint256","name":"tokenWeightOut","type":"uint256"},{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"calcSpotPrice","outputs":[{"internalType":"uint256","name":"spotPrice","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"decreaseApproval","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"poolAmountIn","type":"uint256"},{"internalType":"uint256[]","name":"minAmountsOut","type":"uint256[]"}],"name":"exitPool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"},{"internalType":"uint256","name":"maxPoolAmountIn","type":"uint256"}],"name":"exitswapExternAmountOut","outputs":[{"internalType":"uint256","name":"poolAmountIn","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"poolAmountIn","type":"uint256"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"}],"name":"exitswapPoolAmountIn","outputs":[{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"finalize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getColor","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getController","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getCurrentTokens","outputs":[{"internalType":"address[]","name":"tokens","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"getDenormalizedWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getFinalTokens","outputs":[{"internalType":"address[]","name":"tokens","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"getNormalizedWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getNumTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"}],"name":"getSpotPrice","outputs":[{"internalType":"uint256","name":"spotPrice","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"}],"name":"getSpotPriceSansFee","outputs":[{"internalType":"uint256","name":"spotPrice","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getSwapFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getTotalDenormalizedWeight","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"gulp","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"increaseApproval","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"t","type":"address"}],"name":"isBound","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isFinalized","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isPublicSwap","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"poolAmountOut","type":"uint256"},{"internalType":"uint256[]","name":"maxAmountsIn","type":"uint256[]"}],"name":"joinPool","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"internalType":"uint256","name":"minPoolAmountOut","type":"uint256"}],"name":"joinswapExternAmountIn","outputs":[{"internalType":"uint256","name":"poolAmountOut","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"poolAmountOut","type":"uint256"},{"internalType":"uint256","name":"maxAmountIn","type":"uint256"}],"name":"joinswapPoolAmountOut","outputs":[{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"balance","type":"uint256"},{"internalType":"uint256","name":"denorm","type":"uint256"}],"name":"rebind","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"manager","type":"address"}],"name":"setController","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"bool","name":"public_","type":"bool"}],"name":"setPublicSwap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"swapFee","type":"uint256"}],"name":"setSwapFee","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"minAmountOut","type":"uint256"},{"internalType":"uint256","name":"maxPrice","type":"uint256"}],"name":"swapExactAmountIn","outputs":[{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"},{"internalType":"uint256","name":"spotPriceAfter","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"uint256","name":"maxAmountIn","type":"uint256"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint256","name":"tokenAmountOut","type":"uint256"},{"internalType":"uint256","name":"maxPrice","type":"uint256"}],"name":"swapExactAmountOut","outputs":[{"internalType":"uint256","name":"tokenAmountIn","type":"uint256"},{"internalType":"uint256","name":"spotPriceAfter","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"amt","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"token","type":"address"}],"name":"unbind","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
curvelpabi = json.loads('[{"name":"Deposit","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256","name":"value","indexed":false}],"anonymous":false,"type":"event"},{"name":"Withdraw","inputs":[{"type":"address","name":"provider","indexed":true},{"type":"uint256","name":"value","indexed":false}],"anonymous":false,"type":"event"},{"name":"UpdateLiquidityLimit","inputs":[{"type":"address","name":"user","indexed":false},{"type":"uint256","name":"original_balance","indexed":false},{"type":"uint256","name":"original_supply","indexed":false},{"type":"uint256","name":"working_balance","indexed":false},{"type":"uint256","name":"working_supply","indexed":false}],"anonymous":false,"type":"event"},{"outputs":[],"inputs":[{"type":"address","name":"lp_addr"},{"type":"address","name":"_minter"}],"stateMutability":"nonpayable","type":"constructor"},{"name":"user_checkpoint","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"addr"}],"stateMutability":"nonpayable","type":"function","gas":2079152},{"name":"claimable_tokens","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"addr"}],"stateMutability":"nonpayable","type":"function","gas":1998318},{"name":"kick","outputs":[],"inputs":[{"type":"address","name":"addr"}],"stateMutability":"nonpayable","type":"function","gas":2084532},{"name":"set_approve_deposit","outputs":[],"inputs":[{"type":"address","name":"addr"},{"type":"bool","name":"can_deposit"}],"stateMutability":"nonpayable","type":"function","gas":35766},{"name":"deposit","outputs":[],"inputs":[{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function"},{"name":"deposit","outputs":[],"inputs":[{"type":"uint256","name":"_value"},{"type":"address","name":"addr"}],"stateMutability":"nonpayable","type":"function"},{"name":"withdraw","outputs":[],"inputs":[{"type":"uint256","name":"_value"}],"stateMutability":"nonpayable","type":"function","gas":2208318},{"name":"integrate_checkpoint","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":2297},{"name":"minter","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1421},{"name":"crv_token","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1451},{"name":"lp_token","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1481},{"name":"controller","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1511},{"name":"voting_escrow","outputs":[{"type":"address","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1541},{"name":"balanceOf","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":1725},{"name":"totalSupply","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1601},{"name":"future_epoch_time","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1631},{"name":"approved_to_deposit","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"arg0"},{"type":"address","name":"arg1"}],"stateMutability":"view","type":"function","gas":1969},{"name":"working_balances","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":1845},{"name":"working_supply","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1721},{"name":"period","outputs":[{"type":"int128","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1751},{"name":"period_timestamp","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":1890},{"name":"integrate_inv_supply","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"uint256","name":"arg0"}],"stateMutability":"view","type":"function","gas":1920},{"name":"integrate_inv_supply_of","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":1995},{"name":"integrate_checkpoint_of","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":2025},{"name":"integrate_fraction","outputs":[{"type":"uint256","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":2055},{"name":"inflation_rate","outputs":[{"type":"uint256","name":""}],"inputs":[],"stateMutability":"view","type":"function","gas":1931}]')
sushimasterchefabi = json.loads('[{"inputs":[{"internalType":"contract SushiToken","name":"_sushi","type":"address"},{"internalType":"address","name":"_devaddr","type":"address"},{"internalType":"uint256","name":"_sushiPerBlock","type":"uint256"},{"internalType":"uint256","name":"_startBlock","type":"uint256"},{"internalType":"uint256","name":"_bonusEndBlock","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"EmergencyWithdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"pid","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw","type":"event"},{"inputs":[],"name":"BONUS_MULTIPLIER","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"contract IERC20","name":"_lpToken","type":"address"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"bonusEndBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_devaddr","type":"address"}],"name":"dev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"devaddr","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"emergencyWithdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_from","type":"uint256"},{"internalType":"uint256","name":"_to","type":"uint256"}],"name":"getMultiplier","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"massUpdatePools","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"migrator","outputs":[{"internalType":"contract IMigratorChef","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"pendingSushi","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"poolInfo","outputs":[{"internalType":"contract IERC20","name":"lpToken","type":"address"},{"internalType":"uint256","name":"allocPoint","type":"uint256"},{"internalType":"uint256","name":"lastRewardBlock","type":"uint256"},{"internalType":"uint256","name":"accSushiPerShare","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"poolLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_allocPoint","type":"uint256"},{"internalType":"bool","name":"_withUpdate","type":"bool"}],"name":"set","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigratorChef","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sushi","outputs":[{"internalType":"contract SushiToken","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"sushiPerBlock","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalAllocPoint","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"}],"name":"updatePool","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"name":"userInfo","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"rewardDebt","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_pid","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
ethAflipv0 = web3.eth.contract(address=ethAflip0xv0, abi=ethAflipabiv0)
batAflipv0 = web3.eth.contract(address=batAflip0xv0, abi=batAflipabiv0)
cat = web3.eth.contract(address=cat0x, abi=catabi)
vat = web3.eth.contract(address=vat0x, abi=vatabi)
vault_manager = web3.eth.contract(address=vaultmanager0x, abi=vaultmanagerabi)


TEND_TOPIC = ['0x4b43ed1200000000000000000000000000000000000000000000000000000000']
DENT_TOPIC = ['0x5ff3a38200000000000000000000000000000000000000000000000000000000']
DEAL_TOPIC = ['0xc959c42b00000000000000000000000000000000000000000000000000000000']
BITE_TOPIC = ['0xa716da86bc1fb6d43d1493373f34d7a418b619681cd7b90f7ea667ba1489be28']
KICK_TOPIC = ['0xc84ce3a1172f0dec3173f04caaa6005151a4bfe40d4c9f3ea28dba5f719b2a7a']
NEW_VAULT_TOPIC = ['0xd6be0bc178658a382ff4f91c8c68b542aa6b71685b8fe427966b87745c3ea7a2']
POKE_TOPIC = ['0xdfd7467e425a8107cfd368d159957692c25085aacbcf5228ce08f10f2146486e']
LOGVALUE_TOPIC = ['0x296ba4ca62c6c21c95e828080cb8aec7481b71390585605300a8a76f9e95b527']
DSR_JOIN_TOPIC = ['0xbb35783b00000000000000000000000000000000000000000000000000000000']
DAI_JOIN_DRAW_TOPIC = ['0xef693bed00000000000000000000000000000000000000000000000000000000']
DAI_JOIN_WIPE_TOPIC = ['0x3b4da69f00000000000000000000000000000000000000000000000000000000']
JOIN_LOCK_TOPIC = ['0x3b4da69f00000000000000000000000000000000000000000000000000000000']
JOIN_FREE_TOPIC = ['0xef693bed00000000000000000000000000000000000000000000000000000000']
SHIFT_TOPIC = ['0xe50322a200000000000000000000000000000000000000000000000000000000']
OPEN_EVENT_TOPIC = ['0x63be0c612ee6020e80cb90261895d4d0ab79074ff37cc5e7b58769eaad9959a2']
GIVE_TOPIC = ['0xfcafcc6800000000000000000000000000000000000000000000000000000000']
INSTA_ACCOUNT_CREATED_TOPIC = ['0x83435eca805f6256e4aa778ee8b2e8aec7485fa4b643a0fff05b7df6bf688389']
DAI_DRAW_MANAGER_TOPIC = ['0x45e6bdcd00000000000000000000000000000000000000000000000000000000']
DAI_WIPE_MANAGER_TOPIC = ['0x45e6bdcd00000000000000000000000000000000000000000000000000000000']


INSTA_ACCOUNT_CREATED_TOPIC = '0x83435eca805f6256e4aa778ee8b2e8aec7485fa4b643a0fff05b7df6bf688389'
OPEN_EVENT_TOPI = '0x63be0c612ee6020e80cb90261895d4d0ab79074ff37cc5e7b58769eaad9959a2'
GIVE_TOPI = '0xfcafcc6800000000000000000000000000000000000000000000000000000000'
URN_TOPI = '0x7608870300000000000000000000000000000000000000000000000000000000'
ETH_A_ILK = '0x4554482d41000000000000000000000000000000000000000000000000000000'
BAT_A_ILK = '0x4241542d41000000000000000000000000000000000000000000000000000000'
USDC_A_ILK = '0x555344432d410000000000000000000000000000000000000000000000000000'
USDC_B_ILK = '0x555344432d420000000000000000000000000000000000000000000000000000'
WBTC_A_ILK = '0x574254432d410000000000000000000000000000000000000000000000000000'
TUSD_A_ILK = '0x545553442d410000000000000000000000000000000000000000000000000000'
ZRX_A_ILK = '0x5a52582d41000000000000000000000000000000000000000000000000000000'
KNC_A_ILK = '0x4b4e432d41000000000000000000000000000000000000000000000000000000'
MANA_A_ILK = '0x4d414e412d410000000000000000000000000000000000000000000000000000'
USDT_A_ILK = '0x555344542d410000000000000000000000000000000000000000000000000000'
PAX_A_ILK = '0x5041585553442d41000000000000000000000000000000000000000000000000'

QUICK_DICT_PATCH = {'ETHA':ETH_A_ILK,
	'BATA':BAT_A_ILK,
	'USDCA':USDC_A_ILK,
	'USDCB':USDC_B_ILK,
	'WBTCA':WBTC_A_ILK,
	'TUSDA':TUSD_A_ILK,
	'ZRXA':ZRX_A_ILK,
	'KNCA':KNC_A_ILK,
	'MANAA':MANA_A_ILK,
	'USDTA':USDT_A_ILK,
	'PAXA':PAX_A_ILK,
	'XXXX':'0x0000000000000000000000000000000000000000000000000000000000000000'
	}

MIGRATED_ILK = '0x5341490000000000000000000000000000000000000000000000000000000000'
DAI_DRAW_MANAGI = '0x45e6bdcd00000000000000000000000000000000000000000000000000000000'
DAI_WIPE_MANAGI = '0x45e6bdcd00000000000000000000000000000000000000000000000000000000'

VAULT_OBJ_FILENAME = 'vaultids.obj'
STRAT_OBJ_FILENAME = 'strats.obj'
STRAT_INTERESTING_OBJ_FILENAME = 'interestingstrats.obj'
FARMING_CSV_FILENAME = 'vaultfarmers.csv'
ACTUAL_OWNERS_OBJ_FILENAME = 'actualowners.obj'
URN_TO_ID_DICT_FILENAME = 'urntoiddict.obj'
LID_V0_TO_ID_DICT_FILENAME = 'lidv0toiddict.obj'
LID_V1_TO_ID_DICT_FILENAME = 'lidv1toiddict.obj'
LID_V2_TO_ID_DICT_FILENAME = 'lidv2toiddict.obj'
WETH_OSM_PRICES_FILENAME = 'wethosmprices.obj'
BAT_OSM_PRICES_FILENAME = 'batosmprices.obj'
LIQUIDATED_VAULTS_FILENAME = 'liquidatedvaultids.obj'
LIQUIDATED_DEALS_FILENAME = 'liquidateddeals.obj'
VAULT_INIT_FILENAME = 'vaultinit.csv'
VAULT_INTERACTIONS_FILENAME = 'vaultinteractions.csv'
VAULTS_I_CARE_ABOUT_CSV = 'vaultsIcareabout.csv'
DEALS_FILENAME = 'deals.csv'
ETH_PRICE_CSV = 'ethosm.csv'
BAT_PRICE_CSV = 'batosm.csv'

STEP_SIZE = 100

AMMS = {'0xA478c2975Ab1Ea89e8196811F51A7B7Ade33eB11':'Uniswap ETH/DAI',
	'0x94cDd18F53a8f3EC9A3Ec0CBE897aED5ea009c43':'Uniswap yDAI/DAI',
	'0xAE461cA67B15dc8dc81CE7615e0320dA1A9aB8D5':'Uniswap DAI/USDC',
	'0xB20bd5D04BE54f870D5C0d3cA85d82b34B836405':'Uniswap DAI/USDT',
	'0x3031745E732dcE8fECccc94AcA13D5fa18F1012d':'Balancer SAFE(2)/DAI(98)',
	'0x99e582374015c1d2F3C0f98d0763B4B1145772B7':'Balancer ETH(50)/DAI(50)',
	'0x16cAC1403377978644e78769Daa49d8f6B6CF565':'Balancer YFII(2)/DAI(98)',
	'0xA2B47E3D5c44877cca798226B7B8118F9BFb7A56':'Curve (Compound Pool)',
	'0x52EA46506B9CC5Ef470C5bf89f17Dc28bB35D85C':'Curve (USDT Pool)',
	'0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51':'Curve (y Pool)',
	'0x79a8C46DeA5aDa233ABaFFD40F3A0A2B1e5A4F27':'Curve (BUSD Pool)',
	'0xA5407eAE9Ba41422680e2e00537571bcC53efBfD':'Curve (sUSDv2 Pool)',
	'0x06364f10B501e868329afBc005b3492902d6C763':'Curve (PAX Pool)',
	'0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7':'Curve (3 Pool)',
	'0xC3D03e4F041Fd4cD388c549Ee2A29a9E5075882f':'Sushiswap ETH/DAI',
	
	'0x329239599afB305DA0A2eC69c58F8a6697F9F88d':'Swerve (y Pool)',
	'0xC2D55CE14a8e04AEF9B6bCfD105079b63C6a0AC8':'YFV Seed Pool v2',
	'0x31631b3DD6C697E574d6B886708cd44f5ccf258F':'Mooniswap DAI(50)/USDC(50)',
	'0x0355F9041Be739F5BbF548577C535DD2F4f48473':'Oneswap ETH/DAI',


	
	}


MISC = {'0xACd43E627e64355f1861cEC6d3a6688B31a6F952':'DAI Curve yVault',
	'0xfB76E9be55758d0042e003c1E46E186360F0627e':'aavegotchi', # an aragon DAO NFT bonding curve thing. check hashes here: https://scout.cool/
	'0xC2cB1040220768554cf699b0d863A3cd4324ce32':'yDAI1',
	'0x16de59092dAE5CcF4A1E6439D611fd0653f0Bd01':'yDAI2',
	'0x99d1Fa417f94dcD62BfE781a1213c092a47041Bc':'ycDAI (',
	'0x794e6e91555438aFc3ccF1c5076A74F42133d08D':'Oasis',
	'0xD621CaF5bF045F82f746df295c86fDF5E42c8461':'Kani Rewards',
	'0xC6635074d5cF8C47585Fab0B3EBF15C56fc6af53':'Hotpot',

}


LENDING = {'0x3dfd23A6c5E8BbcFc9581d2E864a68feb6a076d3':'Aave',
	'0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e':'dydx Solo Margin',
	'0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643':'Compound Dai'
}

CEXS = {'0x6DCb8492B5De636fD9e0a32413514647D00eF8D0':'CEX1',
	'0xC9390c509EBaaC49E89581FE725E55C3d5E9ab14':'CEX2',
	'0x131a9A36Ea25aFB4Ed1a4510eE4B36E369d0F699':'CEX3',
	'0x897607AB556177B0E0938541073Ac1E01c55e483':'CEX4',
	'0x66c57bF505A85A74609D2C83E94Aabb26d691E1F':'CEX5',
	'0xc5e66aaBb96a642e06c1765eFEFA5a88e7AfBD89':'CEX6',
	'0xE93381fB4c4F14bDa253907b18faD305D799241a':'Huobi 10',
	'0x876EabF441B2EE5B5b0554Fd502a8E0600950cFa':'Bitfinex 3',



	'0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE':'Binance 1',
	'0xD551234Ae421e3BCBA99A0Da6d736074f22192FF':'Binance 2',
	'0x564286362092D8e7936f0549571a803B203aAceD':'Binance 3',
	'0x0681d8Db095565FE8A346fA0277bFfdE9C0eDBBF':'Binance 4'




}
class Strat():
	def __init__(self):
		self.vaultid = 0
		self.vault_owner = ''
		self.actual_owner = ''
		self.strategy = []
		self.current_debt = 0
		self.current_collateral = 0
		self.current_ratio = 0
		self.ilk_type = ''

	def check_brrr(self):
		if((self.ilk_type == 'USDCA') or (self.ilk_type == 'TUSDA') or (self.ilk_type == 'PAXA')):
			if(self.current_ratio <= 1.01):
				self.strategy.append('BRRRRRRR')

	def check_list(self):
		# fix this to acount for dollar value not just 10
		bal_threshold = 10
		# dust token threshold is very tiny
		dust_threshold = 0.0001
		# get the compound ctoken balances
		for i in ctokenlist:
			bal = 0
			bal, nam = getctokenbalance(self.actual_owner, i)
			if(bal > bal_threshold):
				self.strategy.append(nam)
		# aave atokens
		for i in atokenlist:
			bal = 0
			bal, nam = getatokenbalance(self.actual_owner, i)
			if (bal > bal_threshold):
				self.strategy.append(nam)

		# check uni lp tokens
		for i in unilplist:
			bal = 0
			bal, nam = getunilptokenbalance(self.actual_owner, i)
			if(bal > dust_threshold):
				self.strategy.append(nam)

		# check special case of uni farming
		unirewards_contract = web3.eth.contract(address=ethdaiuniswapstaking0x, abi=ethdaiunilpabi)
		bal = 0
		bal = unirewards_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming UNI in ETH/DAI pool")

		# check balancer lp tokens
		for i in balancerlplist:
			bal = 0
			bal, nam = getbalancerlptokenbalance(self.actual_owner, i)
			if(bal > dust_threshold):
				self.strategy.append(nam)

		# #check curve 
		# for i in curvelist:
		# 	bal = 0 # yes this is the same as above, who cares
		# 	bal, nam = getcurvelptokenbalance(self.actual_owner, i)
		# 	if(bal >  dust_threshold):
		# 		self.strategy.append(nam)

		#check curve gauges manually 
		gauge_comp_contract = web3.eth.contract(address='0x7ca5b0a2910B33e9759DC7dDB0413949071D7575', abi=ethdaiunilpabi)
		bal = 0
		bal = gauge_comp_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming CRV in comp pool")

		gauge_y_contract = web3.eth.contract(address='0xFA712EE4788C042e2B7BB55E6cb8ec569C4530c1', abi=ethdaiunilpabi)
		bal = 0
		bal = gauge_y_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming CRV in y pool")

		gauge_busd_contract = web3.eth.contract(address='0x69Fb7c45726cfE2baDeE8317005d3F94bE838840', abi=ethdaiunilpabi)
		bal = 0
		bal = gauge_busd_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming CRV in busd pool")

		gauge_pax_contract = web3.eth.contract(address='0x64E3C23bfc40722d3B649844055F1D51c1ac041d', abi=ethdaiunilpabi)
		bal = 0
		bal = gauge_pax_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming CRV in pax pool")

		gauge_3_contract = web3.eth.contract(address='0xbFcF63294aD7105dEa65aA58F8AE5BE2D9d0952A', abi=ethdaiunilpabi)
		bal = 0
		bal = gauge_3_contract.functions.balanceOf(self.actual_owner).call() / ETH_SCALE
		if(bal > dust_threshold):
			self.strategy.append("farming CRV in 3 pool")

		#check sushiswap
		sushi_rewards_contract = web3.eth.contract(address='0xc2EdaD668740f1aA35E4D8f227fB8E17dcA888Cd', abi=sushimasterchefabi)
		bal = 0
		#eth/dai pool
		pool_id = 2
		iss = sushi_rewards_contract.functions.userInfo(pool_id, web3.toChecksumAddress(self.actual_owner)).call()
		bal = iss[0]
		if(bal > dust_threshold):
			self.strategy.append("farming Sushi in ETH/DAI pool")






def getcurvelptokenbalance(own, curvelptoke):
	unilp_contract = web3.eth.contract(address=curvelptoke, abi=curvelpabi)
	balan = unilp_contract.functions.balanceOf(own).call() / ETH_SCALE
	name = AMMS[curvelptoke]
	return balan, name

def getbalancerlptokenbalance(own, balancerlptoke):
	unilp_contract = web3.eth.contract(address=balancerlptoke, abi=balancerlpabi)
	balan = unilp_contract.functions.balanceOf(own).call() / ETH_SCALE
	name = AMMS[balancerlptoke]
	return balan, name

def getunilptokenbalance(own, unilptoke):
	unilp_contract = web3.eth.contract(address=unilptoke, abi=ethdaiunilpabi)
	balan = unilp_contract.functions.balanceOf(own).call() / ETH_SCALE
	name = AMMS[unilptoke]
	return balan, name


def getatokenbalance(own, atoke):
	atoke_contract = web3.eth.contract(address=atoke, abi=aethabi)
	divisor = math.pow(10, atoke_contract.functions.decimals().call())
	balan = 0
	try:
		balan = atoke_contract.functions.balanceOf(own).call() / divisor
	except:
		balan = 0
		print('unknown divide by zero error')

	
	name = atoke_contract.functions.name().call()
	return balan, name


def getctokenbalance(own, ctoke):
	ctoke_contract = web3.eth.contract(address=ctoke, abi=cdaiabi)
	balan = ctoke_contract.functions.balanceOfUnderlying(own).call()
	name = ctoke_contract.functions.name().call()
	if((ctoke == cusdc0x) or (ctoke == cusdt0x)):
		balan = balan / USDC_SCALE
	else:
		balan = balan / ETH_SCALE
	
	return balan, name


		

class Vault():
	def __init__(self):
		self.vaultid = 0
		self.block_created = 0
		self.actions = []
		self.flipper_version = 0
		self.kicks = []
		self.tends = []
		self.winning_tends = []
		self.dents = []
		self.winning_dents = []
		self.deals = []
		self.debt = 0
		self.max_debt = 0
		self.owners = []
		self.urn = ''
		self.ilk_type = ''

	def display_vault(self):
		print('id: {0}\n bc: {1}\n actions: {2}\n owners: {3}\n kicks: {4}\n tends{5}\n winning_tends {6}\n dents {7}\n winning_dents\n {8} deals{9}\n urn: {10}\n'.format(self.vaultid, self.block_created, self.actions, self.owners, self.kicks, self.tends, self.winning_tends, self.dents, self.winning_dents, self.deals, self.urn))
	def display_actions(self):
		for p in self.actions:
			print(p)





def get_filled_vault_id():
	try:
		with (open(VAULT_OBJ_FILENAME, "rb")) as openfile:
			while True:
				try:
					return pickle.load(openfile)
				except EOFError:
					break
	except FileNotFoundError:
		print("\nFile " + CDP_OBJ_FILENAME + " does not exist. Run 'update_spells' command.\n")
		sys.exit(-1)

#BE SURE YOU GCHANGE LATEST_UPDATE_BLOCK AND BLOCK TO GO TO
def update_vault_id(latest_update_block, block_to_go_to, write_objs, step_siz):
	vaults = []
	urn_to_id_dict = {}
	lid_v0_to_id_dict = {}
	lid_v1_to_id_dict = {}
	lid_v2_to_id_dict = {}
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	urn_to_id_dict = get_pickle(URN_TO_ID_DICT_FILENAME)
	lid_v0_to_id_dict = get_pickle(LID_V0_TO_ID_DICT_FILENAME)
	lid_v1_to_id_dict = get_pickle(LID_V1_TO_ID_DICT_FILENAME)
	lid_v2_to_id_dict = get_pickle(LID_V2_TO_ID_DICT_FILENAME)

	meat_and_potato(vaults, urn_to_id_dict,  lid_v0_to_id_dict, lid_v1_to_id_dict, lid_v2_to_id_dict, latest_update_block, block_to_go_to, write_objs, step_siz)
	
# only run this if you don't have any .obj files
def get_vault_id():
	vaults = []
	urn_to_id_dict = {}
	lid_v0_to_id_dict = {}
	lid_v1_to_id_dict = {}
	lid_v2_to_id_dict = {}
	print("getting the ids starting with 1")
	vv = Vault()
	# this is the dummy vault
	vv.vaultid = 0
	vv.owners = ['0x0000000000000000000000000000000000000002']
	vv.block_created = FIRST_BLOCK
	vv.actions = []
	vv.kicks = []
	vv.tends = []
	vv.winning_tends = []
	vv.winning_dents = []
	vv.dents = []
	vv.deals = []
	vv.ilk_type = 'ETHA'
	vv.urn = '0x0000000000000000000000000000000000000003'
	vaults.append(vv)

	meat_and_potato(vaults, urn_to_id_dict, lid_v0_to_id_dict, lid_v1_to_id_dict, lid_v2_to_id_dict, FIRST_BLOCK, LAST_BLOCK, True, STEP_SIZE)


def meat_and_potato(vaults, urn_to_id_dict, lid_v0_to_id_dict, lid_v1_to_id_dict, lid_v2_to_id_dict, latest_update_block, block_to_go_to, write_objs, step_siz):
	for i in range(latest_update_block, block_to_go_to, step_siz):
		#doing this because it goes so slow here and through 8965000ish for some reason
		if ((i > 8944000) and (i < 8952500)):
			continue
		newcup_pre = []
		newdraw_pre = []
		newwipe_pre = []
		newlock_pre = []
		newfree_pre = []
		newkick_pre = []
		newcup = []
		newdraw = []
		newwipe = []
		newlock = []
		newfree = []
		newkick = []
		newgive = []
		print("getting ids for block {0}".format(i))

		newcup_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":NEW_VAULT_TOPIC})
		newdraw_filter = web3.eth.filter({"address":daijoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DAI_JOIN_DRAW_TOPIC})
		newmigratedraw_filter = web3.eth.filter({"address":migrationdaijoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DAI_JOIN_DRAW_TOPIC})
		newwipe_filter = web3.eth.filter({"address":daijoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DAI_JOIN_WIPE_TOPIC})
		newshift_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":SHIFT_TOPIC})
		newgive_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":GIVE_TOPIC})

		newwethAlock_filter = web3.eth.filter({"address":wethAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newwethAfree_filter = web3.eth.filter({"address":wethAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newwethAkickv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwethAtendv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwethAdentv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwethAdealv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newwethAkickv1_filter = web3.eth.filter({"address":ethAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwethAtendv1_filter = web3.eth.filter({"address":ethAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwethAdentv1_filter = web3.eth.filter({"address":ethAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwethAdealv1_filter = web3.eth.filter({"address":ethAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newwethAkickv2_filter = web3.eth.filter({"address":ethAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwethAtendv2_filter = web3.eth.filter({"address":ethAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwethAdentv2_filter = web3.eth.filter({"address":ethAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwethAdealv2_filter = web3.eth.filter({"address":ethAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		
		newbatAlock_filter = web3.eth.filter({"address":batAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newbatAfree_filter = web3.eth.filter({"address":batAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newbatAkickv0_filter = web3.eth.filter({"address":batAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newbatAtendv0_filter = web3.eth.filter({"address":batAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newbatAdentv0_filter = web3.eth.filter({"address":batAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newbatAdealv0_filter = web3.eth.filter({"address":batAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newbatAkickv1_filter = web3.eth.filter({"address":batAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newbatAtendv1_filter = web3.eth.filter({"address":batAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newbatAdentv1_filter = web3.eth.filter({"address":batAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newbatAdealv1_filter = web3.eth.filter({"address":batAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newbatAkickv2_filter = web3.eth.filter({"address":batAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newbatAtendv2_filter = web3.eth.filter({"address":batAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newbatAdentv2_filter = web3.eth.filter({"address":batAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newbatAdealv2_filter = web3.eth.filter({"address":batAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newusdcAlock_filter = web3.eth.filter({"address":usdcAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newusdcAfree_filter = web3.eth.filter({"address":usdcAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newusdcAkickv0_filter = web3.eth.filter({"address":usdcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcAtendv0_filter = web3.eth.filter({"address":usdcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcAdentv0_filter = web3.eth.filter({"address":usdcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcAdealv0_filter = web3.eth.filter({"address":usdcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newusdcAkickv1_filter = web3.eth.filter({"address":usdcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcAtendv1_filter = web3.eth.filter({"address":usdcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcAdentv1_filter = web3.eth.filter({"address":usdcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcAdealv1_filter = web3.eth.filter({"address":usdcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newusdcAkickv2_filter = web3.eth.filter({"address":usdcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcAtendv2_filter = web3.eth.filter({"address":usdcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcAdentv2_filter = web3.eth.filter({"address":usdcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcAdealv2_filter = web3.eth.filter({"address":usdcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newusdcBlock_filter = web3.eth.filter({"address":usdcBjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newusdcBfree_filter = web3.eth.filter({"address":usdcBjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newusdcBkickv0_filter = web3.eth.filter({"address":usdcBflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcBtendv0_filter = web3.eth.filter({"address":usdcBflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcBdentv0_filter = web3.eth.filter({"address":usdcBflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcBdealv0_filter = web3.eth.filter({"address":usdcBflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newusdcBkickv1_filter = web3.eth.filter({"address":usdcBflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcBtendv1_filter = web3.eth.filter({"address":usdcBflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcBdentv1_filter = web3.eth.filter({"address":usdcBflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcBdealv1_filter = web3.eth.filter({"address":usdcBflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newusdcBkickv2_filter = web3.eth.filter({"address":usdcBflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdcBtendv2_filter = web3.eth.filter({"address":usdcBflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdcBdentv2_filter = web3.eth.filter({"address":usdcBflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdcBdealv2_filter = web3.eth.filter({"address":usdcBflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newwbtcAlock_filter = web3.eth.filter({"address":wbtcAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newwbtcAfree_filter = web3.eth.filter({"address":wbtcAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newwbtcAkickv0_filter = web3.eth.filter({"address":wbtcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwbtcAtendv0_filter = web3.eth.filter({"address":wbtcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwbtcAdentv0_filter = web3.eth.filter({"address":wbtcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwbtcAdealv0_filter = web3.eth.filter({"address":wbtcAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newwbtcAkickv1_filter = web3.eth.filter({"address":wbtcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwbtcAtendv1_filter = web3.eth.filter({"address":wbtcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwbtcAdentv1_filter = web3.eth.filter({"address":wbtcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwbtcAdealv1_filter = web3.eth.filter({"address":wbtcAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newwbtcAkickv2_filter = web3.eth.filter({"address":wbtcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newwbtcAtendv2_filter = web3.eth.filter({"address":wbtcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newwbtcAdentv2_filter = web3.eth.filter({"address":wbtcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newwbtcAdealv2_filter = web3.eth.filter({"address":wbtcAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newtusdAlock_filter = web3.eth.filter({"address":tusdAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newtusdAfree_filter = web3.eth.filter({"address":tusdAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newtusdAkickv0_filter = web3.eth.filter({"address":tusdAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newtusdAtendv0_filter = web3.eth.filter({"address":tusdAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newtusdAdentv0_filter = web3.eth.filter({"address":tusdAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newtusdAdealv0_filter = web3.eth.filter({"address":tusdAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newtusdAkickv1_filter = web3.eth.filter({"address":tusdAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newtusdAtendv1_filter = web3.eth.filter({"address":tusdAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newtusdAdentv1_filter = web3.eth.filter({"address":tusdAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newtusdAdealv1_filter = web3.eth.filter({"address":tusdAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newtusdAkickv2_filter = web3.eth.filter({"address":tusdAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newtusdAtendv2_filter = web3.eth.filter({"address":tusdAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newtusdAdentv2_filter = web3.eth.filter({"address":tusdAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newtusdAdealv2_filter = web3.eth.filter({"address":tusdAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newzrxAlock_filter = web3.eth.filter({"address":zrxAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newzrxAfree_filter = web3.eth.filter({"address":zrxAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newzrxAkickv0_filter = web3.eth.filter({"address":zrxAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newzrxAtendv0_filter = web3.eth.filter({"address":zrxAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newzrxAdentv0_filter = web3.eth.filter({"address":zrxAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newzrxAdealv0_filter = web3.eth.filter({"address":zrxAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newzrxAkickv1_filter = web3.eth.filter({"address":zrxAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newzrxAtendv1_filter = web3.eth.filter({"address":zrxAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newzrxAdentv1_filter = web3.eth.filter({"address":zrxAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newzrxAdealv1_filter = web3.eth.filter({"address":zrxAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newzrxAkickv2_filter = web3.eth.filter({"address":zrxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newzrxAtendv2_filter = web3.eth.filter({"address":zrxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newzrxAdentv2_filter = web3.eth.filter({"address":zrxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newzrxAdealv2_filter = web3.eth.filter({"address":zrxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newkncAlock_filter = web3.eth.filter({"address":kncAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newkncAfree_filter = web3.eth.filter({"address":kncAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newkncAkickv0_filter = web3.eth.filter({"address":kncAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newkncAtendv0_filter = web3.eth.filter({"address":kncAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newkncAdentv0_filter = web3.eth.filter({"address":kncAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newkncAdealv0_filter = web3.eth.filter({"address":kncAflip0xv0, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newkncAkickv1_filter = web3.eth.filter({"address":kncAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newkncAtendv1_filter = web3.eth.filter({"address":kncAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newkncAdentv1_filter = web3.eth.filter({"address":kncAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newkncAdealv1_filter = web3.eth.filter({"address":kncAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newkncAkickv2_filter = web3.eth.filter({"address":kncAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newkncAtendv2_filter = web3.eth.filter({"address":kncAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newkncAdentv2_filter = web3.eth.filter({"address":kncAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newkncAdealv2_filter = web3.eth.filter({"address":kncAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newmanaAlock_filter = web3.eth.filter({"address":manaAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newmanaAfree_filter = web3.eth.filter({"address":manaAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newmanaAkickv1_filter = web3.eth.filter({"address":manaAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newmanaAtendv1_filter = web3.eth.filter({"address":manaAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newmanaAdentv1_filter = web3.eth.filter({"address":manaAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newmanaAdealv1_filter = web3.eth.filter({"address":manaAflip0xv1, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})
		newmanaAkickv2_filter = web3.eth.filter({"address":manaAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newmanaAtendv2_filter = web3.eth.filter({"address":manaAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newmanaAdentv2_filter = web3.eth.filter({"address":manaAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newmanaAdealv2_filter = web3.eth.filter({"address":manaAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newusdtAlock_filter = web3.eth.filter({"address":usdtAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newusdtAfree_filter = web3.eth.filter({"address":usdtAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newusdtAkickv2_filter = web3.eth.filter({"address":usdtAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newusdtAtendv2_filter = web3.eth.filter({"address":usdtAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newusdtAdentv2_filter = web3.eth.filter({"address":usdtAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newusdtAdealv2_filter = web3.eth.filter({"address":usdtAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})

		newpaxAlock_filter = web3.eth.filter({"address":paxAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_LOCK_TOPIC})
		newpaxAfree_filter = web3.eth.filter({"address":paxAjoin0x, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":JOIN_FREE_TOPIC})
		newpaxAkickv2_filter = web3.eth.filter({"address":paxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":KICK_TOPIC})
		newpaxAtendv2_filter = web3.eth.filter({"address":paxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":TEND_TOPIC})
		newpaxAdentv2_filter = web3.eth.filter({"address":paxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DENT_TOPIC})
		newpaxAdealv2_filter = web3.eth.filter({"address":paxAflip0xv2, "fromBlock":i, "toBlock":i + step_siz - 1, "topics":DEAL_TOPIC})


		newcup_pre = newcup_filter.get_all_entries()
		newdraw_pre = newdraw_filter.get_all_entries()
		newmigratedraw_pre = newmigratedraw_filter.get_all_entries()
		newwipe_pre = newwipe_filter.get_all_entries()
		newshift_pre = newshift_filter.get_all_entries()
		newgive_pre = newgive_filter.get_all_entries()

		newwethAlock_pre = newwethAlock_filter.get_all_entries()
		newwethAfree_pre = newwethAfree_filter.get_all_entries()
		newwethAkickv0_pre = newwethAkickv0_filter.get_all_entries()
		newwethAtendv0_pre = newwethAtendv0_filter.get_all_entries()
		newwethAdentv0_pre = newwethAdentv0_filter.get_all_entries()
		newwethAdealv0_pre = newwethAdealv0_filter.get_all_entries()
		newwethAkickv1_pre = newwethAkickv1_filter.get_all_entries()
		newwethAtendv1_pre = newwethAtendv1_filter.get_all_entries()
		newwethAdentv1_pre = newwethAdentv1_filter.get_all_entries()
		newwethAdealv1_pre = newwethAdealv1_filter.get_all_entries()
		newwethAkickv2_pre = newwethAkickv2_filter.get_all_entries()
		newwethAtendv2_pre = newwethAtendv2_filter.get_all_entries()
		newwethAdentv2_pre = newwethAdentv2_filter.get_all_entries()
		newwethAdealv2_pre = newwethAdealv2_filter.get_all_entries()

		newbatAlock_pre = newbatAlock_filter.get_all_entries()
		newbatAfree_pre = newbatAfree_filter.get_all_entries()
		newbatAkickv0_pre = newbatAkickv0_filter.get_all_entries()
		newbatAtendv0_pre = newbatAtendv0_filter.get_all_entries()
		newbatAdentv0_pre = newbatAdentv0_filter.get_all_entries()
		newbatAdealv0_pre = newbatAdealv0_filter.get_all_entries()
		newbatAkickv1_pre = newbatAkickv1_filter.get_all_entries()
		newbatAtendv1_pre = newbatAtendv1_filter.get_all_entries()
		newbatAdentv1_pre = newbatAdentv1_filter.get_all_entries()
		newbatAdealv1_pre = newbatAdealv1_filter.get_all_entries()
		newbatAkickv2_pre = newbatAkickv2_filter.get_all_entries()
		newbatAtendv2_pre = newbatAtendv2_filter.get_all_entries()
		newbatAdentv2_pre = newbatAdentv2_filter.get_all_entries()
		newbatAdealv2_pre = newbatAdealv2_filter.get_all_entries()

		newusdcAlock_pre = newusdcAlock_filter.get_all_entries()
		newusdcAfree_pre = newusdcAfree_filter.get_all_entries()
		newusdcAkickv0_pre = newusdcAkickv0_filter.get_all_entries()
		newusdcAtendv0_pre = newusdcAtendv0_filter.get_all_entries()
		newusdcAdentv0_pre = newusdcAdentv0_filter.get_all_entries()
		newusdcAdealv0_pre = newusdcAdealv0_filter.get_all_entries()
		newusdcAkickv1_pre = newusdcAkickv1_filter.get_all_entries()
		newusdcAtendv1_pre = newusdcAtendv1_filter.get_all_entries()
		newusdcAdentv1_pre = newusdcAdentv1_filter.get_all_entries()
		newusdcAdealv1_pre = newusdcAdealv1_filter.get_all_entries()
		newusdcAkickv2_pre = newusdcAkickv2_filter.get_all_entries()
		newusdcAtendv2_pre = newusdcAtendv2_filter.get_all_entries()
		newusdcAdentv2_pre = newusdcAdentv2_filter.get_all_entries()
		newusdcAdealv2_pre = newusdcAdealv2_filter.get_all_entries()
		
		newusdcBlock_pre = newusdcBlock_filter.get_all_entries()
		newusdcBfree_pre = newusdcBfree_filter.get_all_entries()
		newusdcBkickv0_pre = newusdcBkickv0_filter.get_all_entries()
		newusdcBtendv0_pre = newusdcBtendv0_filter.get_all_entries()
		newusdcBdentv0_pre = newusdcBdentv0_filter.get_all_entries()
		newusdcBdealv0_pre = newusdcBdealv0_filter.get_all_entries()
		newusdcBkickv1_pre = newusdcBkickv1_filter.get_all_entries()
		newusdcBtendv1_pre = newusdcBtendv1_filter.get_all_entries()
		newusdcBdentv1_pre = newusdcBdentv1_filter.get_all_entries()
		newusdcBdealv1_pre = newusdcBdealv1_filter.get_all_entries()
		newusdcBkickv2_pre = newusdcBkickv2_filter.get_all_entries()
		newusdcBtendv2_pre = newusdcBtendv2_filter.get_all_entries()
		newusdcBdentv2_pre = newusdcBdentv2_filter.get_all_entries()
		newusdcBdealv2_pre = newusdcBdealv2_filter.get_all_entries()

		newwbtcAlock_pre = newwbtcAlock_filter.get_all_entries()
		newwbtcAfree_pre = newwbtcAfree_filter.get_all_entries()
		newwbtcAkickv0_pre = newwbtcAkickv0_filter.get_all_entries()
		newwbtcAtendv0_pre = newwbtcAtendv0_filter.get_all_entries()
		newwbtcAdentv0_pre = newwbtcAdentv0_filter.get_all_entries()
		newwbtcAdealv0_pre = newwbtcAdealv0_filter.get_all_entries()
		newwbtcAkickv1_pre = newwbtcAkickv1_filter.get_all_entries()
		newwbtcAtendv1_pre = newwbtcAtendv1_filter.get_all_entries()
		newwbtcAdentv1_pre = newwbtcAdentv1_filter.get_all_entries()
		newwbtcAdealv1_pre = newwbtcAdealv1_filter.get_all_entries()
		newwbtcAkickv2_pre = newwbtcAkickv2_filter.get_all_entries()
		newwbtcAtendv2_pre = newwbtcAtendv2_filter.get_all_entries()
		newwbtcAdentv2_pre = newwbtcAdentv2_filter.get_all_entries()
		newwbtcAdealv2_pre = newwbtcAdealv2_filter.get_all_entries()

		newtusdAlock_pre = newtusdAlock_filter.get_all_entries()
		newtusdAfree_pre = newtusdAfree_filter.get_all_entries()
		newtusdAkickv0_pre = newtusdAkickv0_filter.get_all_entries()
		newtusdAtendv0_pre = newtusdAtendv0_filter.get_all_entries()
		newtusdAdentv0_pre = newtusdAdentv0_filter.get_all_entries()
		newtusdAdealv0_pre = newtusdAdealv0_filter.get_all_entries()
		newtusdAkickv1_pre = newtusdAkickv1_filter.get_all_entries()
		newtusdAtendv1_pre = newtusdAtendv1_filter.get_all_entries()
		newtusdAdentv1_pre = newtusdAdentv1_filter.get_all_entries()
		newtusdAdealv1_pre = newtusdAdealv1_filter.get_all_entries()
		newtusdAkickv2_pre = newtusdAkickv2_filter.get_all_entries()
		newtusdAtendv2_pre = newtusdAtendv2_filter.get_all_entries()
		newtusdAdentv2_pre = newtusdAdentv2_filter.get_all_entries()
		newtusdAdealv2_pre = newtusdAdealv2_filter.get_all_entries()

		newzrxAlock_pre = newzrxAlock_filter.get_all_entries()
		newzrxAfree_pre = newzrxAfree_filter.get_all_entries()
		newzrxAkickv0_pre = newzrxAkickv0_filter.get_all_entries()
		newzrxAtendv0_pre = newzrxAtendv0_filter.get_all_entries()
		newzrxAdentv0_pre = newzrxAdentv0_filter.get_all_entries()
		newzrxAdealv0_pre = newzrxAdealv0_filter.get_all_entries()
		newzrxAkickv1_pre = newzrxAkickv1_filter.get_all_entries()
		newzrxAtendv1_pre = newzrxAtendv1_filter.get_all_entries()
		newzrxAdentv1_pre = newzrxAdentv1_filter.get_all_entries()
		newzrxAdealv1_pre = newzrxAdealv1_filter.get_all_entries()
		newzrxAkickv2_pre = newzrxAkickv2_filter.get_all_entries()
		newzrxAtendv2_pre = newzrxAtendv2_filter.get_all_entries()
		newzrxAdentv2_pre = newzrxAdentv2_filter.get_all_entries()
		newzrxAdealv2_pre = newzrxAdealv2_filter.get_all_entries()

		newkncAlock_pre = newkncAlock_filter.get_all_entries()
		newkncAfree_pre = newkncAfree_filter.get_all_entries()
		newkncAkickv0_pre = newkncAkickv0_filter.get_all_entries()
		newkncAtendv0_pre = newkncAtendv0_filter.get_all_entries()
		newkncAdentv0_pre = newkncAdentv0_filter.get_all_entries()
		newkncAdealv0_pre = newkncAdealv0_filter.get_all_entries()
		newkncAkickv1_pre = newkncAkickv1_filter.get_all_entries()
		newkncAtendv1_pre = newkncAtendv1_filter.get_all_entries()
		newkncAdentv1_pre = newkncAdentv1_filter.get_all_entries()
		newkncAdealv1_pre = newkncAdealv1_filter.get_all_entries()
		newkncAkickv2_pre = newkncAkickv2_filter.get_all_entries()
		newkncAtendv2_pre = newkncAtendv2_filter.get_all_entries()
		newkncAdentv2_pre = newkncAdentv2_filter.get_all_entries()
		newkncAdealv2_pre = newkncAdealv2_filter.get_all_entries()

		newmanaAlock_pre = newmanaAlock_filter.get_all_entries()
		newmanaAfree_pre = newmanaAfree_filter.get_all_entries()
		newmanaAkickv1_pre = newmanaAkickv1_filter.get_all_entries()
		newmanaAtendv1_pre = newmanaAtendv1_filter.get_all_entries()
		newmanaAdentv1_pre = newmanaAdentv1_filter.get_all_entries()
		newmanaAdealv1_pre = newmanaAdealv1_filter.get_all_entries()
		newmanaAkickv2_pre = newmanaAkickv2_filter.get_all_entries()
		newmanaAtendv2_pre = newmanaAtendv2_filter.get_all_entries()
		newmanaAdentv2_pre = newmanaAdentv2_filter.get_all_entries()
		newmanaAdealv2_pre = newmanaAdealv2_filter.get_all_entries()

		newusdtAlock_pre = newusdtAlock_filter.get_all_entries()
		newusdtAfree_pre = newusdtAfree_filter.get_all_entries()
		newusdtAkickv2_pre = newusdtAkickv2_filter.get_all_entries()
		newusdtAtendv2_pre = newusdtAtendv2_filter.get_all_entries()
		newusdtAdentv2_pre = newusdtAdentv2_filter.get_all_entries()
		newusdtAdealv2_pre = newusdtAdealv2_filter.get_all_entries()

		newpaxAlock_pre = newpaxAlock_filter.get_all_entries()
		newpaxAfree_pre = newpaxAfree_filter.get_all_entries()
		newpaxAkickv2_pre = newpaxAkickv2_filter.get_all_entries()
		newpaxAtendv2_pre = newpaxAtendv2_filter.get_all_entries()
		newpaxAdentv2_pre = newpaxAdentv2_filter.get_all_entries()
		newpaxAdealv2_pre = newpaxAdealv2_filter.get_all_entries()

		for j in range(0, len(newcup_pre)):
			vv = Vault()
			vv.vaultid = web3.toInt(newcup_pre[j]['topics'][3])
			vv.owners = []
			vv.owners.append(web3.toChecksumAddress(vault_manager.functions.owns(vv.vaultid).call()))
			vv.block_created = web3.toInt(newcup_pre[j]['blockNumber'])
			vv.actions = []
			vv.kicks = []
			vv.tends = []
			vv.winning_tends = []
			vv.dents = []
			vv.winning_dents = []
			vv.deals = []
			vv.urn = vault_manager.functions.urns(vv.vaultid).call()
			print(vv.vaultid)
			ii = web3.toHex(vault_manager.functions.ilks(vv.vaultid).call())
			urn_to_id_dict[vv.urn] = vv.vaultid
			
			
			if (ii == ETH_A_ILK):
				vv.ilk_type = 'ETHA'
			elif(ii == BAT_A_ILK):
				vv.ilk_type = 'BATA'
			elif(ii == USDC_A_ILK):
				vv.ilk_type = 'USDCA'
			elif(ii == USDC_B_ILK):
				vv.ilk_type = 'USDCB'
			elif(ii == WBTC_A_ILK):
				vv.ilk_type = 'WBTCA'
			elif(ii == TUSD_A_ILK):
				vv.ilk_type = 'TUSDA'
			elif(ii == ZRX_A_ILK):
				vv.ilk_type = 'ZRXA'
			elif(ii == KNC_A_ILK):
				vv.ilk_type = 'KNCA'
			elif(ii == MANA_A_ILK):
				vv.ilk_type = 'MANAA'
			elif(ii == USDT_A_ILK):
				vv.ilk_type = 'USDTA'
			elif(ii == PAX_A_ILK):
				vv.ilk_type = 'PAXA'
	
			vaults.append(vv)

		# draws
		for j in range(0, len(newdraw_pre)):
			amt = web3.toInt(newdraw_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newdraw_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_DRAW_MANAGI) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'draw', 'amount':amt, 'blockNumber':newdraw_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		#special migratation draws
		for j in range(0, len(newmigratedraw_pre)):
			amt = web3.toInt(newmigratedraw_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newmigratedraw_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_DRAW_MANAGI) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'draw', 'amount':amt, 'blockNumber':newmigratedraw_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break

		# wipes
		for j in range(0, len(newwipe_pre)):
			amt = web3.toInt(newwipe_pre[j]['topics'][3])
			rec = web3.eth.getTransactionReceipt(newwipe_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == DAI_WIPE_MANAGI) and (amt != 0)):
					ii = web3.toInt(k['topics'][2])
					act = {'action':'wipe', 'amount':amt, 'blockNumber':newwipe_pre[j]['blockNumber']}
					vaults[ii].actions.append(act)
					break


		# gives
		# new owners need to be added
		for j in range(0, len(newgive_pre)):
			vault_to_give = web3.toInt(newgive_pre[j]['topics'][2])
			address_to_give_to = web3.toChecksumAddress('0x' + web3.toHex(newgive_pre[j]['topics'][3])[26:])
			print("found a new give {0} to {1}".format(vault_to_give, address_to_give_to))
			rec = web3.eth.getTransactionReceipt(newgive_pre[j]['transactionHash'])
			for k in rec['logs']:
				if ((k['address'] == vaultmanager0x) and (web3.toHex(k['topics'][0]) == GIVE_TOPI)):
					vaults[vault_to_give].owners.append(address_to_give_to)
					break



			
					

		# locks
		vaults = lockit(vaults, newwethAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newbatAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newusdcAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newusdcBlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newwbtcAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newtusdAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newzrxAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newkncAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newmanaAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newusdtAlock_pre, urn_to_id_dict)
		vaults = lockit(vaults, newpaxAlock_pre, urn_to_id_dict)


		# frees
		vaults = freeit(vaults, newwethAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newbatAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newusdcAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newusdcBfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newwbtcAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newtusdAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newzrxAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newkncAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newmanaAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newusdtAfree_pre, urn_to_id_dict)
		vaults = freeit(vaults, newpaxAfree_pre, urn_to_id_dict)

		# kicks
		vaults, lid_v0_to_id_dict = kickit(vaults, newwethAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newwethAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newwethAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newbatAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newbatAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newbatAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newusdcAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newusdcAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newusdcAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newusdcBkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newusdcBkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newusdcBkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newwbtcAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newwbtcAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newwbtcAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newtusdAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newtusdAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newtusdAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newzrxAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newzrxAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newzrxAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v0_to_id_dict = kickit(vaults, newkncAkickv0_pre, urn_to_id_dict, lid_v0_to_id_dict, 0)
		vaults, lid_v1_to_id_dict = kickit(vaults, newkncAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newkncAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v1_to_id_dict = kickit(vaults, newmanaAkickv1_pre, urn_to_id_dict, lid_v1_to_id_dict, 1)
		vaults, lid_v2_to_id_dict = kickit(vaults, newmanaAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v2_to_id_dict = kickit(vaults, newusdtAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)
		vaults, lid_v2_to_id_dict = kickit(vaults, newpaxAkickv2_pre, urn_to_id_dict, lid_v2_to_id_dict, 2)

		# tends
		vaults = tendit(vaults, newwethAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newwethAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newwethAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newbatAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newbatAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newbatAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newusdcAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newusdcAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newusdcAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newusdcBtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newusdcBtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newusdcBtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newwbtcAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newwbtcAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newwbtcAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newtusdAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newtusdAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newtusdAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newzrxAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newzrxAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newzrxAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newkncAtendv0_pre, lid_v0_to_id_dict)
		vaults = tendit(vaults, newkncAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newkncAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newmanaAtendv1_pre, lid_v1_to_id_dict)
		vaults = tendit(vaults, newmanaAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newusdtAtendv2_pre, lid_v2_to_id_dict)
		vaults = tendit(vaults, newpaxAtendv2_pre, lid_v2_to_id_dict)

		# dents
		vaults = dentit(vaults, newwethAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newwethAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newwethAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newbatAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newbatAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newbatAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newusdcAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newusdcAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newusdcAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newusdcBdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newusdcBdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newusdcBdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newwbtcAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newwbtcAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newwbtcAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newtusdAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newtusdAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newtusdAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newzrxAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newzrxAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newzrxAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newkncAdentv0_pre, lid_v0_to_id_dict)
		vaults = dentit(vaults, newkncAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newkncAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newmanaAdentv1_pre, lid_v1_to_id_dict)
		vaults = dentit(vaults, newmanaAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newusdtAdentv2_pre, lid_v2_to_id_dict)
		vaults = dentit(vaults, newpaxAdentv2_pre, lid_v2_to_id_dict)

		# deals
		vaults = dealit(vaults, newwethAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newwethAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newwethAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newbatAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newbatAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newbatAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newusdcAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newusdcAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newusdcAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newusdcBdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newusdcBdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newusdcBdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newwbtcAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newwbtcAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newwbtcAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newtusdAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newtusdAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newtusdAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newzrxAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newzrxAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newzrxAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newkncAdealv0_pre, lid_v0_to_id_dict)
		vaults = dealit(vaults, newkncAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newkncAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newmanaAdealv1_pre, lid_v1_to_id_dict)
		vaults = dealit(vaults, newmanaAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newusdtAdealv2_pre, lid_v2_to_id_dict)
		vaults = dealit(vaults, newpaxAdealv2_pre, lid_v2_to_id_dict)


		# shift
		# this is really to account how instadapp was doing their migration tool
		# _i think_ they created new vaults each time there was enough SAI in the migration contract
		# then they would shift the vaults with an other vault that the user wanted
		# I'm not 100% sure. Let's see if this works
		# here are some hashes to look at in case it doesn't
		# https://oasis.app/borrow/1238
		# https://oasis.app/borrow/575
		# https://etherscan.io/tx/0x0ca52b8e154b06c8c432560cb9dbba23066329218a151b084be1617f2d14c81c
		# https://etherscan.io/loans/maker/cdp/147301?p=2
		# https://etherscan.io/tx/0x876b27ca03824c09ecc24e43e9c1f7cbaf7b558c7f44400fad1f9a8617bd44fc#eventlog
		for j in range(0, len(newshift_pre)):
			vault_to_close = web3.toInt(newshift_pre[j]['topics'][2])
			vault_to_shift_with = web3.toInt(newshift_pre[j]['topics'][3])
			print("found a new shift {0} into {1}".format(vault_to_close, vault_to_shift_with))
			for k in vaults[vault_to_close].actions:
				vaults[vault_to_shift_with].actions.append(k)
			vaults[vault_to_close].actions = []


		# removing losing tends
		for i in vaults:
			sorted_tends = sorted(i.tends, key=lambda x: x['liquidationid'])
			uniq_ids = []
			for j in sorted_tends:
				if(j['liquidationid'] not in uniq_ids):
					uniq_ids.append(j['liquidationid'])

			winning_tends = []
			for j in uniq_ids:
				current_winning_bid = 0
				winning_index = 0
				for k in range(0, len(sorted_tends)):
					if(j == sorted_tends[k]['liquidationid']):
						if(sorted_tends[k]['bid'] > current_winning_bid):
							current_winning_bid = sorted_tends[k]['bid']
							winning_index = k
				winning_tends.append(sorted_tends[winning_index])

			i.winning_tends = winning_tends

		# removing losing dents
		for i in vaults:
			sorted_dents = sorted(i.dents, key=lambda x: x['liquidationid'])
			uniq_ids = []
			for j in sorted_dents:
				if(j['liquidationid'] not in uniq_ids):
					uniq_ids.append(j['liquidationid'])

			winning_dents = []
			for j in uniq_ids:
				current_winning_lot = 99999999999999999999999999999999999999999999999999999
				winning_index = 0
				for k in range(0, len(sorted_dents)):
					if(j == sorted_dents[k]['liquidationid']):
						if(sorted_dents[k]['lot'] < current_winning_lot):
							current_winning_lot = sorted_dents[k]['lot']
							winning_index = k
				winning_dents.append(sorted_dents[winning_index])

			i.winning_dents = winning_dents

	


	#need to sort vault actions by bn
	for i in vaults:
		sorted_vault_actions = sorted(i.actions, key = lambda x: x['blockNumber'])
		i.actions = sorted_vault_actions
		sorted_vault_kicks = sorted(i.kicks, key = lambda x: x['blockNumber'])
		i.kicks = sorted_vault_kicks
		sorted_vault_deals = sorted(i.deals, key = lambda x: x['blockNumber'])
		i.deals = sorted_vault_deals


	if (write_objs):
		filehandler = open(VAULT_OBJ_FILENAME, 'wb')
		pickle.dump(vaults, filehandler)
		filehandler2 = open(URN_TO_ID_DICT_FILENAME, 'wb')
		pickle.dump(urn_to_id_dict, filehandler2)
		filehandler3 = open(LID_V0_TO_ID_DICT_FILENAME, 'wb')
		pickle.dump(lid_v0_to_id_dict, filehandler3)
		filehandler4 = open(LID_V1_TO_ID_DICT_FILENAME, 'wb')
		pickle.dump(lid_v1_to_id_dict, filehandler4)
		filehandler5 = open(LID_V2_TO_ID_DICT_FILENAME, 'wb')
		pickle.dump(lid_v2_to_id_dict, filehandler5)

def dealit(vaults, newpre, lid_vx_to_id_dict):
	for j in range(0, len(newpre)):
		liquidation_id = web3.toInt(hexstr=web3.toHex(newpre[j]['topics'][2]))
		keeper = web3.toChecksumAddress(web3.toHex(newpre[j]['topics'][1][12:]))
		act = {'action':'deal', 'liquidationid':liquidation_id, 'keeper':keeper, 'blockNumber':newpre[j]['blockNumber']}
		try:
			ii = lid_vx_to_id_dict[liquidation_id]
		except:
			print('keyerror from the fixes above deals')
			continue
		vaults[ii].deals.append(act)
		
	return vaults

def dentit (vaults, newpre, lid_vx_to_id_dict):
	for j in range(0, len(newpre)):
		liquidation_id = web3.toInt(hexstr=newpre[j]['data'][190:202].lstrip('0'))
		lot = web3.toInt(hexstr=newpre[j]['data'][230:266].lstrip('0'))
		bid = web3.toInt(hexstr=newpre[j]['data'][269:330].lstrip('0'))
		keeper = web3.toChecksumAddress(web3.toHex(newpre[j]['topics'][1][12:]))
		act = {'action':'dent', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newpre[j]['blockNumber']}
		try:
			ii = lid_vx_to_id_dict[liquidation_id]
		except:
			print('keyerror from the fixes above dents')
			continue
		vaults[ii].dents.append(act)
	return vaults

def tendit (vaults, newpre, lid_vx_to_id_dict):
	for j in range(0, len(newpre)):
		thash = web3.toHex(newpre[j]['transactionHash'])
		#print('th: {0}'.format(thash))
		liquidation_id = web3.toInt(hexstr=newpre[j]['data'][190:202].lstrip('0'))
		lot = web3.toInt(hexstr=newpre[j]['data'][230:266].lstrip('0'))
		bid = web3.toInt(hexstr=newpre[j]['data'][269:330].lstrip('0'))
		keeper = web3.toChecksumAddress(web3.toHex(newpre[j]['topics'][1][12:]))
		act = {'action':'tend', 'lot':lot, 'bid':bid, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newpre[j]['blockNumber']}
		try:
			ii = lid_vx_to_id_dict[liquidation_id]
		except:
			print('keyerror from the fixes above tends')
			continue
		vaults[ii].tends.append(act)
		
	return vaults

def kickit (vaults, newpre, urn_to_id_dict, lid_vx_to_id_dict, flip_version):
	for j in range(0, len(newpre)):
		liquidation_id = web3.toInt(hexstr=newpre[j]['data'][2:66].lstrip('0'))
		urnn = web3.toChecksumAddress(web3.toHex(newpre[j]['topics'][1][12:]))
		rec = web3.eth.getTransactionReceipt(newpre[j]['transactionHash'])
		keeper = web3.toChecksumAddress(rec['from'])
		# not sure why this is the case with the migration contracts, but whatever
		if(urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
			continue
		# this annoying bit is for if they messed up the urn
		try:
			ii = urndict[urnn]
		except:
			print('I think they messed up the urn')
			continue
		ii = urn_to_id_dict[urnn]
		lid_vx_to_id_dict[liquidation_id] = ii
		act = {'action':'kick', 'amount':0, 'liquidationid':liquidation_id, 'keeper': keeper, 'blockNumber':newpre[j]['blockNumber']}
		vaults[ii].kicks.append(act)
		vaults[ii].flipper_version = flip_version
	return vaults, lid_vx_to_id_dict

		

def lockit(vaults, newpre, urndict):
	for j in range(0, len(newpre)):
		amt = web3.toInt(newpre[j]['topics'][3])
		rec = web3.eth.getTransactionReceipt(newpre[j]['transactionHash'])
		for k in rec['logs']:
			if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPI) and (amt != 0)):
				urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
				# not sure why this is the case with the migration contracts, but whatever
				if(urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
					continue
				# this annoying bit is for if they messed up the urn
				try:
					ii = urndict[urnn]
				except:
					print('I think they messed up the urn')
					break
				act = {'action':'lock', 'amount':amt, 'blockNumber':newpre[j]['blockNumber']}
				vaults[ii].actions.append(act)
				break
	return vaults

def freeit(vaults, newpre, urndict):
	for j in range(0, len(newpre)):
		amt = web3.toInt(newpre[j]['topics'][3])
		rec = web3.eth.getTransactionReceipt(newpre[j]['transactionHash'])
		for k in rec['logs']:
			if ((k['address'] == vat0x) and (web3.toHex(k['topics'][0]) == URN_TOPI) and (amt != 0)):
				urnn = web3.toChecksumAddress(web3.toHex(k['topics'][2][12:]))
				# not sure why this is the case with the migration contracts, but whatever
				if(urnn == '0xc73e0383F3Aff3215E6f04B0331D58CeCf0Ab849'):
					continue
				# this annoying bit is for if they messed up the urn
				try:
					ii = urndict[urnn]
				except:
					print('I think they messed up the urn')
					break
				ii = urndict[urnn]
				act = {'action':'free', 'amount':amt, 'blockNumber':newpre[j]['blockNumber']}
				vaults[ii].actions.append(act)
				break
	return vaults

def get_eth_prices():
	weth_prices = []
	bat_prices = []
	for i in range(FIRST_BLOCK, LAST_BLOCK, STEP_SIZE):
		newpoke = []
		print("getting ids for block {0}".format(i))

		newwethlogvalue_filter = web3.eth.filter({"address":osmweth0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":LOGVALUE_TOPIC})
		newwethlogvalue_pre = newwethlogvalue_filter.get_all_entries()
		newbatlogvalue_filter = web3.eth.filter({"address":osmbat0x, "fromBlock":i, "toBlock":i + STEP_SIZE - 1, "topics":LOGVALUE_TOPIC})
		newbatlogvalue_pre = newbatlogvalue_filter.get_all_entries()

		for j in range(0, len(newwethlogvalue_pre)):

			price = {'value':web3.toInt(hexstr=newwethlogvalue_pre[j]['data']) / ETH_SCALE, 'blockNumber':newwethlogvalue_pre[j]['blockNumber']}
			weth_prices.append(price)
			print(price)
		for j in range(0, len(newbatlogvalue_pre)):
			price = {'value':web3.toInt(hexstr=newbatlogvalue_pre[j]['data']) / ETH_SCALE, 'blockNumber':newbatlogvalue_pre[j]['blockNumber']}
			bat_prices.append(price)
			print(price)

	
	sorted_weth_prices = sorted(weth_prices, key=lambda x: x['blockNumber'])
	weth_prices = sorted_weth_prices
	sorted_bat_prices = sorted(bat_prices, key=lambda x: x['blockNumber'])
	bat_prices = sorted_bat_prices

	filehandler1 = open(WETH_OSM_PRICES_FILENAME, 'wb')
	pickle.dump(weth_prices, filehandler1)
	filehandler2 = open(BAT_OSM_PRICES_FILENAME, 'wb')
	pickle.dump(bat_prices, filehandler2)

		

def get_pickle(fn):
	try:
		with (open(fn, "rb")) as openfile:
			while True:
				try:
					return pickle.load(openfile)
				except EOFError:
					break
	except FileNotFoundError:
		print("\nFile " + fn + " does not exist. Run 'update_spells' command.\n")
		sys.exit(-1)

def reduce_vaults():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	new_vaults = []

	for i in vaults:
		if(len(i.kicks) != 0):
			new_vaults.append(i)
	filehandler1 = open(LIQUIDATED_VAULTS_FILENAME, 'wb')
	pickle.dump(new_vaults, filehandler1)
	
	for i in new_vaults:
		i.display_vault()


def find_liquidation_purchase_price():
	vaults = get_pickle(LIQUIDATED_VAULTS_FILENAME)

	# init these because I didn't earlier
	for i in vaults:
		i.debt = 0
		i.max_debt = 0
	# calculating the max debt for ordering them
	for i in vaults:
		for k in i.actions:
			if(k['action'] == 'draw'):
				i.debt += k['amount']
			if(k['action'] == 'wipe'):
				i.debt -= k['amount']
			if(i.max_debt < i.debt):
				i.max_debt = i.debt
	
	for i in vaults:
		for j in i.deals:
			current_lid = j['liquidationid']
			tend_lot, tend_bid = find_auction_price(current_lid, i.tends)
			dent_lot, dent_bid = find_auction_price(current_lid, i.dents)
			deal_price = 0
			deal_lot = 0
			deal_bid = 0
			if(dent_lot == -1):
				deal_lot = tend_lot
				deal_bid = tend_bid
				deal_price = deal_bid / deal_lot
			else:
				deal_lot = dent_lot
				deal_bid = dent_bid
				deal_price = deal_bid / deal_lot
			j['deallot'] = deal_lot
			j['dealbid'] = deal_bid
			j['dealprice'] = deal_price
			p_at_deal = find_cc_p(j['blockNumber'], i.ilk_type)
			
			j['discount'] = (1 - (j['dealprice'] / p_at_deal)) * 100
			kicked_on = find_kicked_on(current_lid, i.kicks)
			j['kickedon'] = kicked_on
			print(j)
			
	filehandler1 = open(LIQUIDATED_DEALS_FILENAME, 'wb')
	pickle.dump(vaults, filehandler1)


def find_kicked_on(lid, kicks):
	kk = 0
	for f in kicks:
		if(f['liquidationid'] == lid):
			kk = f['blockNumber']
			break
	return kk

	


def find_cc_p(bn, ilk):
	p = -1
	if(ilk == 'ETHA'):
		ts = web3.eth.getBlock(bn)['timestamp']
		cc_built_url = cc_eth_root_url + '&toTs=' + str(ts + 3600) + cc_key
		pjson = requests.get(cc_built_url)
		pclose = pjson.json()['Data']['Data'][1]['close']
		popen = pjson.json()['Data']['Data'][1]['open']
		p = (pclose + popen) / 2
	elif(ilk == 'BATA'):
		ts = web3.eth.getBlock(bn)['timestamp']
		cc_built_url = cc_bat_root_url + '&toTs=' + str(ts + 3600) + cc_key
		pjson = requests.get(cc_built_url)
		pclose = pjson.json()['Data']['Data'][1]['close']
		popen = pjson.json()['Data']['Data'][1]['open']
		p = (pclose + popen) / 2
	return p




def find_auction_price(lid, tends):
	ll = -1
	bb = -1
	for f in tends:
		if(f['liquidationid'] == lid):
			bb = f['bid'] / ETH44_SCALE
			ll = f['lot'] / ETH_SCALE
			break
	return ll, bb

def output_auction_csvs():
	vaults = get_pickle(LIQUIDATED_DEALS_FILENAME)
	weth_prices = get_pickle(WETH_OSM_PRICES_FILENAME)
	bat_prices = get_pickle(BAT_OSM_PRICES_FILENAME)
	
	list_vaults = []
	for i in vaults:
		templ = [i.vaultid, i.block_created, i.ilk_type, i.max_debt / ETH_SCALE]
		list_vaults.append(templ)
	with open(VAULT_INIT_FILENAME, 'w') as myfile1:
		wr = csv.writer(myfile1)
		wr.writerow(["vaultid", "blockcreated", "ilktype", "maxdebt"],)
		for i in range(0, len(list_vaults)):
			wr.writerow([list_vaults[i][0], list_vaults[i][1], list_vaults[i][2], list_vaults[i][3],])

	list_vault_interactions = []
	for i in vaults:
		for k in i.actions:
			ff = float(k['amount'] / ETH_SCALE)
			list_vault_interactions.append([k['blockNumber'], i.vaultid, k['action'], "{0:.8f}".format(ff)])
	sorted_interactions = sorted(list_vault_interactions, key=lambda x: x[0])
	with open(VAULT_INTERACTIONS_FILENAME, 'w') as myfile2:
		wr = csv.writer(myfile2)
		wr.writerow(["block", "vaultid", "action", "amount"],)
		for i in range(0, len(sorted_interactions)):
			wr.writerow([sorted_interactions[i][0], sorted_interactions[i][1], sorted_interactions[i][2], sorted_interactions[i][3],])

	list_deals = []
	for i in vaults:
		for k in i.deals:
			list_deals.append([k['liquidationid'], i.vaultid, k['kickedon'], k['blockNumber'], k['keeper'], k['deallot'], k['dealbid'], k['discount'],])
	sorted_deals = sorted(list_deals, key=lambda x: x[2])
	with open(DEALS_FILENAME, 'w') as myfile3:
		wr = csv.writer(myfile3)
		wr.writerow(["liquidationid", "vaultid", "kickedon", "dealedon", "keeper", "deallot", "dealbid", "discount"],)
		for i in range(0, len(sorted_deals)):
			wr.writerow([sorted_deals[i][0], sorted_deals[i][1], sorted_deals[i][2], sorted_deals[i][3], sorted_deals[i][4], sorted_deals[i][5], sorted_deals[i][6], sorted_deals[i][7],])

	list_eth_prices = []
	for i in weth_prices:
		temple = [i['blockNumber'], i['value']]
		list_eth_prices.append(temple)
	with open (ETH_PRICE_CSV, 'w') as myfile4:
		wr = csv.writer(myfile4)
		wr.writerow(["blockNumber", "price"])
		for i in range(0, len(list_eth_prices)):
			wr.writerow([list_eth_prices[i][0], list_eth_prices[i][1],])

	list_bat_prices = []
	for i in bat_prices:
		temple = [i['blockNumber'], i['value']]
		list_bat_prices.append(temple)
	with open (BAT_PRICE_CSV, 'w') as myfile5:
		wr = csv.writer(myfile5)
		wr.writerow(["blockNumber", "price"])
		for i in range(0, len(list_bat_prices)):
			wr.writerow([list_bat_prices[i][0], list_bat_prices[i][1],])

def print_keepers():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	keepers = []
	for i in vaults:
		for k in i.kicks:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.tends:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.dents:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
		for k in i.deals:
			if(k['keeper'] not in keepers):
				keepers.append(k['keeper'])
	print(keepers)

def print_kicks_each_block():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	kicks = []
	start_block = web3.eth.blockNumber
	for i in vaults:
		for k in i.kicks:
			kicks.append(k)
			print(k)
	print(kicks)

def print_kicks_no_db():
	previous_bn = web3.eth.blockNumber
	current_bn = web3.eth.blockNumber
	while(True):
		current_bn = web3.eth.blockNumber
		if (previous_bn != current_bn):
			previous_bn = current_bn
			newkick_pre = []
			newkick = []
			i = current_bn
			print("getting kicks, tends, dents, deals for block {0}".format(i))

			# newcup_pre = []
			# newcup_filter = web3.eth.filter({"address":vaultmanager0x, "fromBlock":i, "toBlock":i , "topics":NEW_VAULT_TOPIC})
			# newcup_pre = newcup_filter.get_all_entries()
			# for j in range(0, len(newcup_pre)):
				
			# 	print(web3.toInt(newcup_pre[j]['topics'][3]))
				
			newwethAkickv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i, "topics":KICK_TOPIC})
			newwethAtendv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i, "topics":TEND_TOPIC})
			newwethAdentv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i, "topics":DENT_TOPIC})
			newwethAdealv0_filter = web3.eth.filter({"address":ethAflip0xv0, "fromBlock":i, "toBlock":i, "topics":DEAL_TOPIC})
			
	
			
			newwethAkickv0_pre = newwethAkickv0_filter.get_all_entries()
			newwethAtendv0_pre = newwethAtendv0_filter.get_all_entries()
			newwethAdentv0_pre = newwethAdentv0_filter.get_all_entries()
			newwethAdealv0_pre = newwethAdealv0_filter.get_all_entries()
			

			# WETH kicks
			for j in range(0, len(newwethAkickv0_pre)):
				liquidation_id = web3.toInt(hexstr=newwethAkickv0_pre[j]['data'][2:66].lstrip('0'))
				urnn = web3.toChecksumAddress(web3.toHex(newwethAkickv0_pre[j]['topics'][1][12:]))
				rec = web3.eth.getTransactionReceipt(newwethAkickv0_pre[j]['transactionHash'])
				keeper = web3.toChecksumAddress(rec['from'])
				print('new kick: {0}'.format(web3.toHex(newwethAkickv0_pre[j]['transactionHash'])))
				
			
						
			# WETH tends
			for j in range(0, len(newwethAtendv0_pre)):
				liquidation_id = web3.toInt(hexstr=newwethAtendv0_pre[j]['data'][190:202].lstrip('0'))
				lot = web3.toInt(hexstr=newwethAtendv0_pre[j]['data'][230:266].lstrip('0'))
				bid = web3.toInt(hexstr=newwethAtendv0_pre[j]['data'][269:330].lstrip('0'))
				keeper = web3.toChecksumAddress(web3.toHex(newwethAtendv0_pre[j]['topics'][1][12:]))
				print('new tend: {0}'.format(web3.toHex(newwethAtendv0_pre[j]['transactionHash'])))

			# WETH dents
			for j in range(0, len(newwethAdentv0_pre)):
				liquidation_id = web3.toInt(hexstr=newwethAdentv0_pre[j]['data'][190:202].lstrip('0'))
				lot = web3.toInt(hexstr=newwethAdentv0_pre[j]['data'][230:266].lstrip('0'))
				bid = web3.toInt(hexstr=newwethAdentv0_pre[j]['data'][269:330].lstrip('0'))
				keeper = web3.toChecksumAddress(web3.toHex(newwethAdentv0_pre[j]['topics'][1][12:]))
				print('new dent: {0}'.format(web3.toHex(newwethAdentv0_pre[j]['transactionHash'])))
			# WETH deals
			for j in range(0, len(newwethAdealv0_pre)):
				liquidation_id = web3.toInt(hexstr=web3.toHex(newwethAdealv0_pre[j]['topics'][2]))
				keeper = web3.toChecksumAddress(web3.toHex(newwethAdealv0_pre[j]['topics'][1][12:]))
				print('new deal: {0}'.format(web3.toHex(newwethAdealv0_pre[j]['transactionHash'])))
def update_actual_owners():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	actual_owners = get_pickle(ACTUAL_OWNERS_OBJ_FILENAME)
	pull_owners(vaults, actual_owners)

# pulls everything fressh
def get_actual_owners():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	actual_owners = []
	#dummy address
	actual_owners.append('0x0000000000000000000000000000000000000002')
	pull_owners(vaults, actual_owners)

def pull_owners(vaults, actual_owners):
	# find the latest actual owner so we don't have to repull them all
	latest_vault = len(vaults)
	latest_owner = len(actual_owners)
	for i in range(latest_owner, latest_vault):
		actual_owner = get_actual_owner(vaults[i])
		actual_owners.append(actual_owner)

	filehandler = open(ACTUAL_OWNERS_OBJ_FILENAME, 'wb')
	pickle.dump(actual_owners, filehandler)

def get_all_owner_strategy():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	actual_owners = get_pickle(ACTUAL_OWNERS_OBJ_FILENAME)
	strats = []
	ilk_prices = get_ilk_prices()
	
	# make objs, set the vault ids and owners
	for i in vaults:
		strat = Strat()
		strat.vaultid = i.vaultid
		print(strat.vaultid)
		strat.ilk_type = i.ilk_type
		strat.vault_owner = i.owners[len(i.owners) - 1]
		strat.actual_owner = actual_owners[strat.vaultid]
		if(i.ilk_type == ''):
			i.ilk_type = 'XXXX'
		strat.current_debt, strat.current_collateral = get_dnc(i.vaultid, QUICK_DICT_PATCH[i.ilk_type], i.ilk_type)
		strat.current_ratio = 0
		if (strat.current_debt > 0.00001):
			ilk_price = ilk_prices[i.ilk_type]
			strat.current_ratio = strat.current_collateral * ilk_price / strat.current_debt

		# do they have any x token balance
		if(len(i.actions) > 1):
			strat.check_list()
			strat.check_brrr()
		strats.append(strat)
		
	filehandler = open(STRAT_OBJ_FILENAME, 'wb')
	pickle.dump(strats, filehandler)

def get_interesting_owner_strategy():
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	actual_owners = get_pickle(ACTUAL_OWNERS_OBJ_FILENAME)
	strats = []
	interesting_ids = get_vaults_i_care_about()
	ilk_prices = get_ilk_prices()
	# make objs, set the vault ids and owners
	for i in vaults:
		if(i.vaultid in interesting_ids):
			strat = Strat()
			strat.vaultid = i.vaultid
			print(strat.vaultid)
			strat.ilk_type = i.ilk_type
			strat.vault_owner = i.owners[len(i.owners) - 1]
			strat.actual_owner = actual_owners[strat.vaultid]
			if(i.ilk_type == ''):
				i.ilk_type = 'XXXX'
			strat.current_debt, strat.current_collateral = get_dnc(i.vaultid, QUICK_DICT_PATCH[i.ilk_type], i.ilk_type)
			# if((i.ilk_type == 'USDCA') or (i.ilk_type == 'USDCB') or (i.ilk_type == 'USDTA')):
			# 	strat.current_collateral = strat.current_collateral / USDC_SCALE
			# 	strat.current_debt = strat.current_debt / ETH_SCALE
			# elif(i.ilk_type == 'WBTCA'):
			# 	strat.current_collateral = strat.current_collateral / WBTC_SCALE
			# 	strat.current_debt = strat.current_debt / ETH_SCALE
			# else:
			# 	strat.current_collateral = strat.current_collateral / ETH_SCALE
			# 	strat.current_debt = strat.current_debt / ETH_SCALE

			

			strat.current_ratio = 0
			if (strat.current_debt > 0.00001):
				ilk_price = ilk_prices[i.ilk_type]
				strat.current_ratio = strat.current_collateral * ilk_price / strat.current_debt
				print(strat.current_ratio)



			# do they have any actions
			if(len(i.actions) > 1):
				strat.check_list()
				strat.check_brrr()
			strats.append(strat)
		
	filehandler = open(STRAT_INTERESTING_OBJ_FILENAME, 'wb')
	pickle.dump(strats, filehandler)
		
def get_ilk_prices():
	ilk_prices = {}
	usdc = web3.eth.contract(address=usdc0x, abi=ethdaiunilpabi)
	weth = web3.eth.contract(address=weth0x, abi=ethdaiunilpabi)
	bat = web3.eth.contract(address=bat0x, abi=ethdaiunilpabi)
	wbtc = web3.eth.contract(address=wbtc0x, abi=ethdaiunilpabi)
	zrx = web3.eth.contract(address=zrx0x, abi=ethdaiunilpabi)
	knc = web3.eth.contract(address=knc0x, abi=ethdaiunilpabi)
	mana = web3.eth.contract(address=mana0x, abi=ethdaiunilpabi)
	# uni usdc pool price feed
	usdc_bal = usdc.functions.balanceOf('0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc').call() / USDC_SCALE
	weth_bal = weth.functions.balanceOf('0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc').call() / ETH_SCALE
	ethusd_price = usdc_bal / weth_bal
	ilk_prices['ETHA'] = ethusd_price

	bat_bal = bat.functions.balanceOf('0xB6909B960DbbE7392D405429eB2b3649752b4838').call() / ETH_SCALE
	weth_bal = weth.functions.balanceOf('0xB6909B960DbbE7392D405429eB2b3649752b4838').call() / ETH_SCALE
	bateth_price = weth_bal / bat_bal
	ilk_prices['BATA'] = bateth_price * ethusd_price

	wbtc_bal = wbtc.functions.balanceOf('0xBb2b8038a1640196FbE3e38816F3e67Cba72D940').call() / WBTC_SCALE
	weth_bal = weth.functions.balanceOf('0xBb2b8038a1640196FbE3e38816F3e67Cba72D940').call() / ETH_SCALE
	wbtceth_price = weth_bal / wbtc_bal
	ilk_prices['WBTCA'] = wbtceth_price * ethusd_price

	zrx_bal = zrx.functions.balanceOf('0xc6F348dd3B91a56D117ec0071C1e9b83C0996De4').call() / ETH_SCALE
	weth_bal = weth.functions.balanceOf('0xc6F348dd3B91a56D117ec0071C1e9b83C0996De4').call() / ETH_SCALE
	zrxeth_price = weth_bal / zrx_bal
	ilk_prices['ZRXA'] = zrxeth_price * ethusd_price

	knc_bal = knc.functions.balanceOf('0xf49C43Ae0fAf37217bDcB00DF478cF793eDd6687').call() / ETH_SCALE
	weth_bal = weth.functions.balanceOf('0xf49C43Ae0fAf37217bDcB00DF478cF793eDd6687').call() / ETH_SCALE
	knceth_price = weth_bal / knc_bal
	ilk_prices['KNCA'] = knceth_price * ethusd_price

	mana_bal = mana.functions.balanceOf('0x11b1f53204d03E5529F09EB3091939e4Fd8c9CF3').call() / ETH_SCALE
	weth_bal = weth.functions.balanceOf('0x11b1f53204d03E5529F09EB3091939e4Fd8c9CF3').call() / ETH_SCALE
	manaeth_price = weth_bal / mana_bal
	ilk_prices['MANAA'] = manaeth_price * ethusd_price

	ilk_prices['USDCA'] = 1
	ilk_prices['USDCB'] = 1
	ilk_prices['TUSDA'] = 1
	ilk_prices['USDTA'] = 1
	ilk_prices['PAXA'] = 1
	ilk_prices['XXXX'] = 1

	print(ilk_prices)
	return ilk_prices





def get_dnc(v_id, ilk, ilk_type):
	urn = web3.toChecksumAddress(vault_manager.functions.urns(v_id).call())
	ilk = web3.toBytes(hexstr=ilk)
	rate = vat.functions.ilks(ilk).call()[1] / ETH27_SCALE
	dnc = vat.functions.urns(ilk, urn).call()
	
	art = dnc[1]
	ink = dnc[0]
	# if((ilk_type == 'USDCA') or (ilk_type == 'USDCB') or (ilk_type == 'USDTA')):
	# 	ink = dnc[0] / USDC_SCALE
	# elif(ilk_type == 'WBTCA'):
	# 	ink = dnc[0] / WBTC_SCALE
	# else:
	art = (dnc[1] / ETH_SCALE) * rate
	ink = dnc[0] / ETH_SCALE

	
	return art, ink
	
def get_actual_owner(vv):

	actual_own = vv.owners[len(vv.owners) - 1]
	own = actual_own

	# first see if it is a dsproxy
	try:
		dsprox = web3.eth.contract(address=own, abi=dsproxyabi)
		if(dsprox.functions.cache().call() == dsproxycache0x):
			actual_own = dsprox.functions.owner().call()
			return actual_own

	except:
		print('owner not a dsproxy')

	# then see if it is a normal address or a contract
	normie_address = web3.eth.getCode('0xB6260B06c5b6e32c1bA903FBa67dfCE499d42a87')
	gode = web3.eth.getCode(own)
	if(gode == normie_address):
		print('normal address')
		actual_own = own
		return actual_own

	# then we'll try insta userwallet
	try:
		userwalletprox = web3.eth.contract(address=own, abi=userwalletabi)
		if(userwalletprox.functions.registry().call() == instaregistry0x):
			actual_own = userwalletprox.functions.owner().call()
			return actual_own

	except:
		print('owner not a insta userwallet proxy')

	# then we'll try insta userwallet
	try:
		randomprox = web3.eth.contract(address=own, abi=userwalletabi)
		actual_own = randomprox.functions.owner().call()
		return actual_own

	except:
		print('owner not a random proxy with owner function')


	# # and this one is instaaccount instaindex
	# try:
	# 	instaprox = web3.eth.contract(address=own, abi=instaaccountabi1)
	# 	if(instaprox.functions.instaIndex().call() == instaindex0x):

			
	# except:
	# 	print('owner not an instaproxy')
	
	bb = web3.eth.getBlock(vv.block_created)
	for i in bb['transactions']:
		#print(web3.toHex(i))
		tran = web3.eth.getTransaction(i)
		if(tran['to'] == own):
			actual_own = tran['from']
			print("found another actual owner{0}".format(actual_own))
			return actual_own
			break

	print("actual owner not found, setting to proxy address {0}".format(own))
	return actual_own


def output_farming_csv(strat_file):
	vaults = get_pickle(VAULT_OBJ_FILENAME)
	strats = get_pickle(strat_file)
	urn_to_id_dict = get_pickle(URN_TO_ID_DICT_FILENAME)
	actual_owners = get_pickle(ACTUAL_OWNERS_OBJ_FILENAME)

	list_vaults = []
	#"{0:.8f}".format(ff)
	for i in strats:
		strat_string = ''
		for k in i.strategy:
			strat_string = strat_string + ' ' + k
		list_vaults.append([i.vaultid, i.ilk_type, i.actual_owner, "{0:.2f}".format(i.current_debt), "{0:.5f}".format(i.current_ratio), strat_string])
	sorted_interactions = sorted(list_vaults, key=lambda x: x[0])
	with open(FARMING_CSV_FILENAME, 'w') as myfile2:
		wr = csv.writer(myfile2)
		wr.writerow(["vaultid", "ilk", "owner", "debt", "ratio", "activity"],)
		for i in range(0, len(sorted_interactions)):
			wr.writerow([sorted_interactions[i][0], sorted_interactions[i][1], sorted_interactions[i][2], sorted_interactions[i][3], sorted_interactions[i][4], sorted_interactions[i][5],])



def get_vaults_i_care_about():
	vvs = []
	with open(VAULTS_I_CARE_ABOUT_CSV, 'r') as myfile44:
		rr = csv.reader(myfile44)
		for row in rr:
			vvs.append(int(row[0]))
		
	vvsorted = sorted(vvs)
	return vvsorted



def main():
	# arg parsing
	parser = argparse.ArgumentParser(description='gets the data for the liquidation plot')
	parser.add_argument('--getvaultid', action='store_true', dest='getvaultid', help='gets all the cdp ids and their interactions')
	parser.add_argument('--updatevaultid', action='store_true', dest='updatevaultid', help='updates all the cdp ids and their interactions')

	parser.add_argument('--printvaultid', action='store_true', dest='printvaultid', help='prints all the cdp ids their interactions')
	#parser.add_argument('--getmoney', action='store_true', dest='getmoney', help='gets all the money puts in giant .csv and .obj')
	parser.add_argument('--getprices', action='store_true', dest='getprices', help='gets the price feed prices')

	parser.add_argument('--reducevaults', action='store_true', dest='reducevaults', help='removes everything except for the liquidated')
	parser.add_argument('--findliquidationpurchaseprice', action='store_true', dest='findliquidationpurchaseprice', help='find the amount the keeper paid, the amount bought, and the amount given back')
	parser.add_argument('--outputauctioncsv', action='store_true', dest='outputauctioncsv', help='outputs all auctions stuff to csv')
	parser.add_argument('--getactualowners', action='store_true', dest='getactualowners', help='gets the actual owners obj')
	parser.add_argument('--updateactualowners', action='store_true', dest='updateactualowners', help='updates the actual owners obj')	
	parser.add_argument('--getallownerstrategy', action='store_true', dest='getallownerstrategy', help='gets the all the owner strategies. Takes forever')
	parser.add_argument('--getinterestingownerstrategy', action='store_true', dest='getinterestingownerstrategy', help='gets the interesting owner strategies from vaultsIcareabout.csv')


	parser.add_argument('--outputfarmingcsv', action='store_true', dest='outputfarmingcsv', help='writes the farming strategies correlations to csv')
	parser.add_argument('--printkeepers', action='store_true', dest='printkeepers', help='quick look at all the different keepers')
	parser.add_argument('--printkicks', action='store_true', dest='printkicks', help='quick look at all the different kicks')
	parser.add_argument('--printkicksnodb', action='store_true', dest='printkicksnodb', help='live look at kicks and tends')

	#parser.add_argument('--daemon', action='store_true', dest='daemon', help='runs the daemon')
	global argss
	argss = parser.parse_args()

	if argss.getvaultid:
		get_vault_id()
		sys.exit(0)
	if argss.updatevaultid:
		#update these every time
		# or else
		# do in steps of 100
		# or else
		# starting block, ending block, writing objs 
		update_vault_id(9000000, 10947000 , True, STEP_SIZE)
		sys.exit(0)	
	if argss.printvaultid:
		vault_idds = get_filled_vault_id()
		for s in vault_idds:
			s.display_vault()
		sys.exit(0)
	# if argss.getmoney:
	# 	get_money()
	# 	sys.exit(0)
	if argss.getprices:
		get_eth_prices()
		sys.exit(0)
	if argss.getactualowners:
		get_actual_owners()
		sys.exit(0)
	if argss.updateactualowners:
		update_actual_owners()
		sys.exit(0)
	if argss.getallownerstrategy:
		get_all_owner_strategy()
		sys.exit(0)
	if argss.getinterestingownerstrategy:
		get_interesting_owner_strategy()
		sys.exit(0)
	if argss.outputfarmingcsv:
		strat_file = STRAT_INTERESTING_OBJ_FILENAME
		#strat_file = STRAT_OBJ_FILENAME
		output_farming_csv(strat_file)
		sys.exit(0)
	# if argss.findpopular:
	# 	find_popular_addresses()
	# 	sys.exit(0)
	# if argss.outputcdpcsv:
	# 	output_cdp_csv()
	# 	sys.exit(0)
	# if argss.outputtapcsv:
	# 	output_tap_csv()
	# 	sys.exit(0)
	# if argss.outputpethratiocsv:
	# 	output_peth_ratio_csv()
	# 	sys.exit(0)
	if argss.reducevaults:
		reduce_vaults()
		sys.exit(0)
	if argss.findliquidationpurchaseprice:
		find_liquidation_purchase_price()
		sys.exit(0)
	if argss.outputauctioncsvs:
		output_auction_csvs()
		sys.exit(0)
	if argss.printkeepers:
		print_keepers()
		sys.exit(0)
	if argss.printkicks:
		print_kicks_each_block()
		sys.exit(0)
	if argss.printkicksnodb:
		print_kicks_no_db()
		sys.exit(0)
	if argss.printauctionslive:
		print_auctions_live()
		sys.exit(0)
	if argss.printwinnerslive:
		print_winners_live()
		sys.exit(0)
	if argss.printlongforwisdom:
		print_lfw()
		sys.exit(0)


	print("Run 'getflip.py --help'")
if __name__ == "__main__":
	main()





