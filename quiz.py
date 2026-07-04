#build a quiz where each question is evaluted by a function , nd scores are tracked and reported at the end.
def ask_question(question, correct_answer):
    answer = input(question + " ").strip().lower()
    if answer == correct_answer.lower():
        print("correct")
        return 1
    else:
        print(f"wrong! answer: {correct_answer}")
        return 0 
def display_result(score, total):
    percent = (score/total)*100
    print(f"/your score: {score}/{total} ({percent:.1f}%)")
    if percent >= 80:
        print("excellent!")
    elif percent >= 50:
        print("good effort!")
    else:
        print("keep studying ")

score=0
score=ask_question("capital of india?", "new delhi")
score=ask_question("2**8=?","256")
score=ask_question("python is inter preted? (yes/no)","yes")
display_result(score,3)