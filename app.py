from aiohttp import web
import spacy
import logging

log = logging.getLogger(__name__)

nlp = spacy.load('en', disable=['ner'])

def main():
    async def wordTokenize(request):
        body = await request.json()

        doc = nlp(body['text'])

        tokens = [{'text': token.text, 'lemma': token.lemma_, 'pos': token.tag_, 'stopword': token.is_stop} for token in doc]
        
        return web.json_response({'tokens': tokens})

    async def sentenceTokenize(request):
        body = await request.json()

        doc = nlp(body['text'])

        sentences = [{'text': sentence.text} for sentence in doc.sents]

        return web.json_response({'sentences': sentences})

    app = web.Application(client_max_size=1024**12)
    app.router.add_post('/tokenizers/words', wordTokenize)
    app.router.add_post('/tokenizers/sentences', sentenceTokenize)

    web.run_app(app, host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()