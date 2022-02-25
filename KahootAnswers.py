import requests, json, os

_clear = lambda: os.system('cls')

def _getQuizInfo(_id):
    try:
        _response = requests.get(f"https://api.gradyn.com/kahoot/{_id}")
        if 'INVALID_DATA' not in _response.text:
            return _response.text
        else:
            return "Nah"
    except:
        return "Nah"

def _getAnswer(_question):
    try:
        _correctAnswer = ""
        _type = _question["type"]
        _noOfAnswers = len(_question["choices"])
        _answerNo = 0
        for _answerNo in range(_noOfAnswers):
            _choice = _question["choices"][_answerNo]
            if _question["choices"][_answerNo]["correct"] == True:
                _correctAnswer = _question["choices"][_answerNo]["answer"]
            _answerNo += 1
        return _correctAnswer
    except:
        return "Nah"

def _main():
    print("""         __  __            __ 
   _  __/ / / /___  ____  / /_
  | |/_/ /_/ / __ \/ __ \/ __/
 _>  </ __  / /_/ / /_/ / /_  
/_/|_/_/ /_/\____/\____/\__/  
                              
""")
    print("[Main] Made By Roni | V1.1")
    _quizId = input("[Main] Quiz-ID: ")
    try:
        _quizInfoText = _getQuizInfo(_quizId)
        if _quizInfoText != "Nah":
            print("\n[Main] Getting answers...\n")
            _quizInfoJSON = json.loads(_quizInfoText)
            _title = _quizInfoJSON["title"]
            _desc = _quizInfoJSON["description"]
            print(f"[Info] Title: {_title}\n[Info] Description: {_desc}")
            _noOfQuestions = len(_quizInfoJSON["questions"])
            _questionNo = 0; _fix = 0
            for _questionNo in range(_noOfQuestions):
                _fix += 1
                print(f'[{_fix}] {_getAnswer(_quizInfoJSON["questions"][_questionNo])}')
                _questionNo += 1
        else:
            input(f"[Error] Invalid ID, press enter to restart.")
            _clear(); _main()
    except:
        _clear(); _main()

_main()
