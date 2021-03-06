#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import re

words = {
	'a':'あ',
	'akesi':'獣',
	'ala':'無',
	'alasa':'探',
	'ale':'全',
	'ali':'全',
	'anpa':'下',
	'ante':'变',
	'anu':'ぬ',
	'awen':'待',
	'e':'え',
	'en':'ん',
	'esun':'市',
	'ijo':'物',
	'ike':'悪',
	'ilo':'具',
	'insa':'内',
	'jaki':'汚',
	'jan':'人',
	'jelo':'黄',
	'jo':'有',
	'kala':'魚',
	'kalama':'音',
	'kama':'来',
	'kasi':'木',
	'ken':'能',
	'kepeken':'使',
	'kili':'果',
	'kin':'又',
	'kipisi':'切',
	'kiwen':'石',
	'ko':'粉',
	'kon':'空',
	'kule':'色',
	'kulupu':'群',
	'kute':'聞',
	'la':'ら',
	'lape':'眠',
	'laso':'青',
	'lawa':'首',
	'len':'布',
	'lete':'冷',
	'li':'り',
	'lili':'小',
	'linja':'糸',
	'lipu':'葉',
	'loje':'赤',
	'lon':'在',
	'luka':'手',
	'lukin':'見',
	'lupa':'穴',
	'ma':'土',
	'mama':'母',
	'mani':'貝',
	'meli':'女',
	'mi':'私',
	'mije':'男',
	'moku':'食',
	'moli':'死',
	'monsi':'後',
	'mu':'む',
	'mun':'月',
	'musi':'楽',
	'mute':'多',
	'namako':'冗',
	'nanpa':'番',
	'nasa':'狂',
	'nasin':'道',
	'nena':'丘',
	'ni':'此',
	'nimi':'称',
	'noka':'足',
	'o':'お',
	'oko':'目',
	'olin':'愛',
	'ona':'彼',
	'open':'開',
	'pakala':'打',
	'pali':'作',
	'palisa':'棒',
	'pan':'米',
	'pana':'授',
	'pata':'氏',
	'pi':'ぴ',
	'pilin':'心',
	'pimeja':'黒',
	'pini':'終',
	'pipi':'虫',
	'poka':'側',
	'poki':'箱',
	'pona':'良',
	'sama':'同',
	'seli':'火',
	'selo':'皮',
	'seme':'何',
	'sewi':'上',
	'sijelo':'体',
	'sike':'丸',
	'sin':'新',
	'sina':'君',
	'sinpin':'前',
	'sitelen':'画',
	'sona':'知',
	'soweli':'猫',
	'suli':'大',
	'suno':'日',
	'supa':'面',
	'suwi':'甜',
	'tan':'因',
	'taso':'許',
	'tawa':'去',
	'telo':'水',
	'tenpo':'时',
	'toki':'言',
	'tomo':'家',
	'tu':'二',
	'unpa':'盛',
	'uta':'口',
	'utala':'戦',
	'walo':'白',
	'wan':'一',
	'waso':'鳥',
	'wawa':'力',
	'weka':'遥',
	'wile':'要'
	}

puncts = {
	' ':'',
	'¡':'',
	'¿':''
	}

cmdargs = sys.argv

with open(cmdargs[1], 'r') as intext, open('kanji_'+cmdargs[1], 'w') as outtext:
	for line in intext:
		for src, target in words.iteritems():
			line = re.sub('\\b'+src+'\\b', target, line)
		for src, target in puncts.iteritems():
			line = line.replace(src, target)
		outtext.write(line)
