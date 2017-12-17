import json
import codecs

def getJLPTTag(tag):
	return {
        "JLPT_5": "jlpt5",
        "JLPT_4": "jlpt4",
        "JLPT_3": "jlpt3",
        "JLPT_2": "jlpt2",
		"JLPT_1": "jlpt1",
    }.get(tag, None)

kanjiJSON = json.load(open('Core_2000_Japanese_Vocabulary.json'))
newData = {"kanji": []}

for note in kanjiJSON['notes']:
	newData["kanji"].append({	
								"character": note["fields"][1].encode('utf-8'),
						 		"kunyomi": note["fields"][2].encode('utf-8'),
						 		"meanings": [note["fields"][3].encode('utf-8')],
						 		"sentencekanji": [note["fields"][4].encode('utf-8')],
						 		"sentencekana": [note["fields"][5].encode('utf-8')],
						 		"tags": [] if getJLPTTag(note["tags"][1]) == None else [getJLPTTag(note["tags"][1])]
							})

with open('core_vocab.json', 'wb') as file:
    json.dump(newData, file, ensure_ascii=False)






