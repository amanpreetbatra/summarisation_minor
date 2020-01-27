import json
from develop.summain import data_to_send
def data():
    x = dict()
    x = data_to_send()
    dat = [  { "key":"textrank",
                     "values":[  # textrank
            {'axis': "Cosine Similarity", 'tech': 'textrank','value': x['ent']['textrank'][0]},
            {'axis': "Unit Overlap", 'tech': 'textrank','value': x['ent']['textrank'][1]},
            {'axis': "Precision",'tech': 'textrank', 'value': x['ent']['textrank'][2]},
            {'axis': "Recall",'tech': 'textrank', 'value': x['ent']['textrank'][3]},
            {'axis': "F Score",'tech': 'textrank', 'value': x['ent']['textrank'][4]}]},

             {"key": "luhn",
              "values":[ # luhn
              {'axis': "Cosine Similarity",'tech': 'luhn', 'value':x['ent']['luhn'][0]},
              {'axis': "Unit Overlap", 'tech': 'luhn','value':x['ent']['luhn'][1]},
              {'axis': "Precision", 'tech': 'luhn','value':x['ent']['luhn'][2]},
              {'axis': "Recall", 'tech': 'luhn','value':x['ent']['luhn'][3]},
              {'axis': "F Score", 'tech': 'luhn','value':x['ent']['luhn'][4]}]},
             {"key": "lsa",
              "values":[  #lsa
        {'axis': "Cosine Similarity",'tech': 'lsa', 'value':x['ent']['lsa'][0]},
        {'axis': "Unit Overlap", 'tech': 'lsa','value': x['ent']['lsa'][1]},
        {'axis': "Precision",'tech': 'lsa', 'value': x['ent']['lsa'][2]},
        {'axis': "Recall",'tech': 'lsa', 'value': x['ent']['lsa'][3]},
        {'axis': "F Score",'tech': 'lsa', 'value': x['ent']['lsa'][4]}]},
             {"key": "klsum",
              "values":[  # klsum
            {'axis': "Cosine Similarity",'tech': 'klsum', 'value': x['ent']['klsum'][0]},
            {'axis': "Unit Overlap",'tech': 'klsum', 'value': x['ent']['klsum'][1]},
            {'axis': "Precision",'tech': 'klsum', 'value': x['ent']['klsum'][2]},
            {'axis': "Recall",'tech': 'klsum', 'value': x['ent']['klsum'][3]},
            {'axis': "F Score",'tech': 'klsum', 'value': x['ent']['klsum'][4]}]},

             {"key": "lexrank",
              "values":
                  [  # lexrank
            {'axis': "Cosine Similarity",'tech': 'lexrank', 'value': x['ent']['lexrank'][0] },
            {'axis': "Unit Overlap", 'tech': 'lexrank','value': x['ent']['lexrank'][1]},
            {'axis': "Precision",'tech': 'lexrank', 'value': x['ent']['lexrank'][2]},
            {'axis': "Recall",'tech': 'lexrank', 'value': x['ent']['lexrank'][3]},
            {'axis': "F Score", 'tech': 'lexrank','value': x['ent']['lexrank'][4]}]}
    ]

    return json.dumps(dat)

def data1():
    x = dict()
    x = data_to_send()
    dat = [{"key": "textrank",
            "values": [  # textrank
                {'axis': "Cosine Similarity", 'tech': 'textrank', 'value': x['science']['textrank'][0]},
                {'axis': "Unit Overlap", 'tech': 'textrank', 'value': x['science']['textrank'][1]},
                {'axis': "Precision", 'tech': 'textrank', 'value': x['science']['textrank'][2]},
                {'axis': "Recall", 'tech': 'textrank', 'value': x['science']['textrank'][3]},
                {'axis': "F Score", 'tech': 'textrank', 'value': x['science']['textrank'][4]}]},

           {"key": "luhn",
            "values": [  # luhn
                {'axis': "Cosine Similarity", 'tech': 'luhn', 'value': x['science']['luhn'][0]},
                {'axis': "Unit Overlap", 'tech': 'luhn', 'value': x['science']['luhn'][1]},
                {'axis': "Precision", 'tech': 'luhn', 'value': x['science']['luhn'][2]},
                {'axis': "Recall", 'tech': 'luhn', 'value': x['science']['luhn'][3]},
                {'axis': "F Score", 'tech': 'luhn', 'value': x['science']['luhn'][4]}]},
           {"key": "lsa",
            "values": [  # lsa
                {'axis': "Cosine Similarity", 'tech': 'lsa', 'value': x['science']['lsa'][0]},
                {'axis': "Unit Overlap", 'tech': 'lsa', 'value': x['science']['lsa'][1]},
                {'axis': "Precision", 'tech': 'lsa', 'value': x['science']['lsa'][2]},
                {'axis': "Recall", 'tech': 'lsa', 'value': x['science']['lsa'][3]},
                {'axis': "F Score", 'tech': 'lsa', 'value': x['science']['lsa'][4]}]},
           {"key": "klsum",
            "values": [  # klsum
                {'axis': "Cosine Similarity", 'tech': 'klsum', 'value': x['science']['klsum'][0]},
                {'axis': "Unit Overlap", 'tech': 'klsum', 'value': x['science']['klsum'][1]},
                {'axis': "Precision", 'tech': 'klsum', 'value': x['science']['klsum'][2]},
                {'axis': "Recall", 'tech': 'klsum', 'value': x['science']['klsum'][3]},
                {'axis': "F Score", 'tech': 'klsum', 'value': x['science']['klsum'][4]}]},

           {"key": "lexrank",
            "values":
                [  # lexrank
                    {'axis': "Cosine Similarity", 'tech': 'lexrank', 'value': x['science']['lexrank'][0]},
                    {'axis': "Unit Overlap", 'tech': 'lexrank', 'value': x['science']['lexrank'][1]},
                    {'axis': "Precision", 'tech': 'lexrank', 'value': x['science']['lexrank'][2]},
                    {'axis': "Recall", 'tech': 'lexrank', 'value': x['science']['lexrank'][3]},
                    {'axis': "F Score", 'tech': 'lexrank', 'value': x['science']['lexrank'][4]}]}
           ]

    return json.dumps(dat)

def data2():
    x = dict()
    x = data_to_send()
    dat = [  { "key":"textrank",
                     "values":[  # textrank
            {'axis': "Cosine Similarity", 'tech': 'textrank','value': x['sports']['textrank'][0]/2.15},
            {'axis': "Unit Overlap", 'tech': 'textrank','value': x['sports']['textrank'][1]},
            {'axis': "Precision",'tech': 'textrank', 'value': x['sports']['textrank'][2]},
            {'axis': "Recall",'tech': 'textrank', 'value': x['sports']['textrank'][3]},
            {'axis': "F Score",'tech': 'textrank', 'value': x['sports']['textrank'][4]}]},

             {"key": "luhn",
              "values":[ # luhn
              {'axis': "Cosine Similarity",'tech': 'luhn', 'value':x['sports']['luhn'][0]/2.15},
              {'axis': "Unit Overlap", 'tech': 'luhn','value':x['sports']['luhn'][1]},
              {'axis': "Precision", 'tech': 'luhn','value':x['sports']['luhn'][2]},
              {'axis': "Recall", 'tech': 'luhn','value':x['sports']['luhn'][3]},
              {'axis': "F Score", 'tech': 'luhn','value':x['sports']['luhn'][4]}]},
             {"key": "lsa",
              "values":[  #lsa
        {'axis': "Cosine Similarity",'tech': 'lsa', 'value':x['sports']['lsa'][0]/2.15},
        {'axis': "Unit Overlap", 'tech': 'lsa','value': x['sports']['lsa'][1]},
        {'axis': "Precision",'tech': 'lsa', 'value': x['sports']['lsa'][2]},
        {'axis': "Recall",'tech': 'lsa', 'value': x['sports']['lsa'][3]},
        {'axis': "F Score",'tech': 'lsa', 'value': x['sports']['lsa'][4]}]},
             {"key": "klsum",
              "values":[  # klsum
            {'axis': "Cosine Similarity",'tech': 'klsum', 'value': x['sports']['klsum'][0]/2.15},
            {'axis': "Unit Overlap",'tech': 'klsum', 'value': x['sports']['klsum'][1]},
            {'axis': "Precision",'tech': 'klsum', 'value': x['sports']['klsum'][2]},
            {'axis': "Recall",'tech': 'klsum', 'value': x['sports']['klsum'][3]},
            {'axis': "F Score",'tech': 'klsum', 'value': x['sports']['klsum'][4]}]},

             {"key": "lexrank",
              "values":
                  [  # lexrank
            {'axis': "Cosine Similarity",'tech': 'lexrank', 'value': x['sports']['lexrank'][0] / 2.15},
            {'axis': "Unit Overlap", 'tech': 'lexrank','value': x['sports']['lexrank'][1]},
            {'axis': "Precision",'tech': 'lexrank', 'value': x['sports']['lexrank'][2]},
            {'axis': "Recall",'tech': 'lexrank', 'value': x['sports']['lexrank'][3]},
            {'axis': "F Score", 'tech': 'lexrank','value': x['sports']['lexrank'][4]}]}
    ]

    return json.dumps(dat)




