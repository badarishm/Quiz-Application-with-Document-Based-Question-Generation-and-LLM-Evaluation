import pandas as pd
from document_ingestion import DocumentIngester
from question_generator import QuestionGenerator
from evaluator import AnswerEvaluator

ingester = DocumentIngester()
qgen = QuestionGenerator()
evaluator = AnswerEvaluator()


class QuizSession:
    def __init__(self):
        self.reset()

    def reset(self):
        self.quiz_items = []
        self.current_index = 0
        self.results = []

    def load_document(self, fp, num_questions=5):
        text = ingester.extract(fp)
        chunks = ingester.chunk_text(text)

        self.quiz_items = qgen.generate_quiz(chunks, num_questions)

    def current_question(self):
        return self.quiz_items[self.current_index]

    def submit_answer(self, ua):
        item = self.current_question()

        result = evaluator.evaluate(ua, item['reference_answer'])
        result.update({
            'question': item['question'],
            'user_answer': ua
        })

        self.results.append(result)
        self.current_index += 1

        return result

    def export_results(self):
        return pd.DataFrame(self.results)
