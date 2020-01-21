def get_formatted_name(first, last, middle=""):
    "generate a neatly formatted full name"
    if middle:
        full_name=first + " " + middle + " " + last
    else:
        full_name=first + " " + last
    return full_name.title()


class AnonSurvey():
    "\"collect anonymous answers to a survey questions\""

    def __init__(self,question):
        "\"Store a question, and prepare to store responses\""
        self.question=question
        self.responses=[]
    
    def show_question(self):
        "\"show the suervey question.\""
        print(self.question)

    def store_response(self, new_response):
        "\"Store a single response to the survey\""
        self.responses.append(new_response)

    def show_results(self):
        "\"Show all the responses that have been given\""
        print("Survey results:")
        for response in responses:
            print('- ' + response)


