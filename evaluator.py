import re
from sentence_transformers import SentenceTransformer, util

embed_model = SentenceTransformer('all-MiniLM-L6-v2')


class AnswerEvaluator:
    def __init__(self):
        self.model = embed_model

    def sem_score(self, ua, ra):
        if not ua.strip():
            return 0.0
        eu = self.model.encode(ua, convert_to_tensor=True)
        er = self.model.encode(ra, convert_to_tensor=True)
        return max(0.0, util.cos_sim(eu, er).item())

    def kw_score(self, ua, ra):
        stop = {'the','a','an','is','are','was','were','to','of','and',
                'in','it','that','this','with','for','on','at','by','from'}

        ref = set(w.lower() for w in re.findall(r'\b\w+\b', ra)
                  if w.lower() not in stop and len(w) > 3)

        usr = set(w.lower() for w in re.findall(r'\b\w+\b', ua))

        return len(ref & usr) / len(ref) if ref else 0.5

    def evaluate(self, ua, ra):
        sem = self.sem_score(ua, ra)
        kw = self.kw_score(ua, ra)

        score = round((sem * 0.65 + kw * 0.35) * 10, 2)

        if score >= 8: grade = 'Excellent'
        elif score >= 6: grade = 'Good'
        elif score >= 4: grade = 'Partial'
        else: grade = 'Needs Improvement'

        return {
            'score': score,
            'grade': grade,
            'semantic_similarity': round(sem*100, 1),
            'keyword_overlap': round(kw*100, 1),
            'reference_answer': ra
        }
