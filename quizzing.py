import requests
import json
import pprint
import random
import html


url = ("https://opentdb.com/api.php?amount=1")

end_game = ""

while end_game != "quit":
    r = requests.get(url)
    if(r.status_code != 200):
        end_game = input(
            "Sorry there was a problem retriving the question . Press enter to try again or type 'quit' to quit the game")
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data["results"][0]["question"]
        answers = data["results"][0]["incorrect_answers"]

        print(answers)
        correct_answer = data["results"][0]["correct_answer"]
        answers.append(correct_answer)
        random.shuffle(answers)

        print(question + "\n")

        for answer in answers:
            print(str(answer_number) + " - " + html.unescape(answer))
            answer_number += 1

        user_answer = input("\nType the number of the correct answer")

        user_answer = answers[int(user_answer)-1]

    if user_answer == correct_answer:
        print("\nCongrats! you answered correctly, the correct answer was :" +
              html.usncape(correct_answer))
        score_correct += 1

    else:
        print("Sorry , " + html.unscape(user_answer) +
              "is not the correct answer")
        score_correct += 1
    print("\n###########################")
    print("Correct answers : " + str(score_correct))
    print("Correct answers : " + str(score_incorrect))
    print("\n###########################")

    end_game = input("\nPress Enter to play again or press Quit to quit")

print("\nThanks for playing")
