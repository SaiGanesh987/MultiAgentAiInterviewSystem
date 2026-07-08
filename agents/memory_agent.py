class MemoryAgent:

    def __init__(self):

        self.history = []

        self.weak_topics = []

        self.strong_topics = []


    def add_result(self, topic, question, answer, score, feedback):

        self.history.append({

            "topic": topic,

            "question": question,

            "answer": answer,

            "score": score,

            "feedback": feedback

        })

        if score < 5:

            self.weak_topics.append(topic)

        else:

            self.strong_topics.append(topic)


    def get_history(self):

        return self.history


    def get_summary(self):

        return {

            "strong_topics": list(set(self.strong_topics)),

            "weak_topics": list(set(self.weak_topics))

        }