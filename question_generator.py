import random
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(
    'mrm8488/t5-base-finetuned-question-generation-ap'
)
model = AutoModelForSeq2SeqLM.from_pretrained(
    'mrm8488/t5-base-finetuned-question-generation-ap'
)

def custom_qg_pipeline(inputs, max_length=128, num_beams=4):
    input_ids = tokenizer(inputs, return_tensors='pt',
                          padding=True, truncation=True).input_ids

    outputs = model.generate(
        input_ids, max_length=max_length,
        num_beams=num_beams, early_stopping=True
    )

    return [{'generated_text': tokenizer.decode(outputs[0], skip_special_tokens=True)}]


class QuestionGenerator:
    def __init__(self):
        self.qg = custom_qg_pipeline

    def gen_q(self, answer_text, context):
        inp = f'answer: {answer_text} context: {context}'
        try:
            r = self.qg(inp)[0]['generated_text']
            r = r.replace('question:', '').strip()
            if r and r[-1] not in '.?!':
                r += '?'
            return r
        except:
            return None

    def key_answer(self, chunk):
        sents = sent_tokenize(chunk)
        for s in sents:
            if len(s.split()) > 8:
                return s
        return sents[0] if sents else chunk[:200]

    def generate_quiz(self, chunks, n=5):
        n = min(n, len(chunks))
        quiz = []

        for i, chunk in enumerate(random.sample(chunks, n)):
            key_ans = self.key_answer(chunk)
            q = self.gen_q(key_ans, chunk)

            if q:
                quiz.append({
                    'id': i+1,
                    'question': q,
                    'context': chunk,
                    'reference_answer': key_ans
                })

        return quiz
