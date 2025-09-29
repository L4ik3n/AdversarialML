import requests as r
import json 
class OLLAMA:
    def __init__(self, model, api_endpoint='http://0.0.0.0:11434/api/generate', **kwargs):
        self.model = model
        self.api_endpoint = api_endpoint
        self.session = r.Session()
        self.kwargs = {'temperature': 0.5, **kwargs}


    def queryModel(self, query, **kwargs):
        output =''
        payload = {'model': self.model, 'prompt': query, **self.kwargs, **kwargs}

        with self.session.post(self.api_endpoint, json=payload, stream=True) as re:
            if re.status_code ==200:
                for line in re.iter_lines():
                    if line:
                        j = json.loads(line.decode('utf-8'))
                        output += j.get('response', '')
                        if j.get('done', True):
                            break
            else:
                print(f'Error. Status code {re.status_code}')

        return[output.strip()]

    def __call__(self, query, **kwargs):
        return self.queryModel(query, **kwargs)

