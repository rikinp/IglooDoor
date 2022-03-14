from flask import Flask,request, jsonify
import json
app = Flask(__name__)

@app.route('/unsafepasswords/<string:keyword>', methods=['GET'])
def index(keyword):

    easyGuessKeywords = ["12345678","123456789","abcdefgh","qwerty","password","asdfghjk"]
    easyGuessKeywords.append(keyword + "@123")
    easyGuessKeywords.append(keyword + "@99")
    easyGuessKeywords.append("123@" + keyword)
    easyGuessKeywords.append("99@" + keyword)

    return jsonify(easyGuessKeywords)

if __name__ == '__main__':
    app.run(port=80, debug=True)

