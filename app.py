from flask import Flask ,render_template,request
import pandas as pd
from collections import Counter
import re
import textdistance
app = Flask(__name__)

words = []
with open('autocorrect book.txt','r',encoding='utf-8') as f:
    data = f.read()
    data = data.lower()
    words = re.findall(r'\w+',data)
    words += words

v = set(words)
word_freq_dict = Counter(words)
total = sum(word_freq_dict.values())
prob = {}
for k in word_freq_dict.keys():
    prob[k] = word_freq_dict[k] / total

@app.route("/")

def home():
    return render_template("index.html" , suggestions=None)

@app.route('/suggest',methods=['POST'])

def suggest():
    keyword = request.form['keyword'].lower()
    if keyword:
        similarites = [1-textdistance.Jaccard(qval=2).distance(v,keyword) for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(prob,orient='index').reset_index()
        df.columns = ['Word','Prob']
        df['Similarity'] = similarites
        suggestions = df.sort_values(['Similarity','Prob'],ascending=False)[['Word','Similarity']]
        suggestions_list = suggestions.to_dict('records')
        return render_template('index.html',suggestions = suggestions_list)

if __name__ == "__main__":
    app.run(debug=True)