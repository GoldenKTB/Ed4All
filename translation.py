from transformers import pipeline

def english(translate_to, input):
    en_fi = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")
    en_es = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")
    en_de = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
    en_zh = pipeline("translation_en_to_zh", model="Helsinki-NLP/opus-mt-en-zh")

    match translate_to:
        case "finnish":
            fi_res = en_fi(input)
            return fi_res[0]['translation_text']

        case "spanish":
            es_res = en_es(input)
            return es_res[0]['translation_text']

        case "german":
            de_res = en_de(input)
            return de_res[0]['translation_text']
        
        case "mandarin":
            zh_res = en_zh(input)
            return zh_res[0]['translation_text']

def finnish(translate_to, input):
    fi_en = pipeline("translation_fi_to_en", model="Helsinki-NLP/opus-mt-fi-en")
    fi_es = pipeline("translation_fi_to_es", model="Helsinki-NLP/opus-mt-fi-es")
    fi_de = pipeline("translation_fi_to_de", model="Helsinki-NLP/opus-mt-fi-de")
    fi_zh = pipeline("translation_fi_to_zh", model="Helsinki-NLP/opus-mt-fi-ZH")

    match translate_to:
        case "english":
            en_res = fi_en(input)
            return en_res[0]['translation_text']

        case "spanish":
            es_res = fi_es(input)
            return es_res[0]['translation_text']

        case "german":
            de_res = fi_de(input)
            return de_res[0]['translation_text']
        
        case "mandarin":
            zh_res = fi_zh(input)
            return zh_res[0]['translation_text']


def spanish(translate_to, input):
    es_fi = pipeline("translation_es_to_fi", model="Helsinki-NLP/opus-mt-es-fi")
    es_en = pipeline("translation_es_to_en", model="Helsinki-NLP/opus-mt-es-en")
    es_de = pipeline("translation_es_to_de", model="Helsinki-NLP/opus-mt-es-de")
    es_zh = pipeline("translation_es_to_zh", model="Helsinki-NLP/opus-tatoeba-es-zh")

    match translate_to:
        case "finnish":
            fi_res = es_fi(input)
            return fi_res[0]['translation_text']

        case "english":
            en_res = es_en(input)
            return en_res[0]['translation_text']

        case "german":
            de_res = es_de(input)
            return de_res[0]['translation_text']
        
        case "mandarin":
            zh_res = es_zh(input)
            return zh_res[0]['translation_text']

def german(translate_to, input):
    de_fi = pipeline("translation_de_to_fi", model="Helsinki-NLP/opus-mt-de-fi")
    de_es = pipeline("translation_de_to_es", model="Helsinki-NLP/opus-mt-de-es")
    de_en = pipeline("translation_de_to_en", model="Helsinki-NLP/opus-mt-de-en")
    de_zh = pipeline("translation_de_to_zh", model="Helsinki-NLP/opus-mt-de-ZH")

    match translate_to:
        case "finnish":
            fi_res = de_fi(input)
            return fi_res[0]['translation_text']

        case "spanish":
            es_res = de_es(input)
            return es_res[0]['translation_text']

        case "english":
            en_res = de_en(input)
            return en_res[0]['translation_text']
        
        case "mandarin":
            zh_res = de_zh(input)
            return zh_res[0]['translation_text']

def mandarin(translate_to, input):
    zh_en = pipeline("translation_zh_to_en", model="Helsinki-NLP/opus-mt-zh-en")
    zh_fi = pipeline("translation_zh_to_vi", model="Helsinki-NLP/opus-mt-zh-fi")
    zh_de = pipeline("translation_zh_to_de", model="Helsinki-NLP/opus-mt-zh-de")
    en_es = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")

    match translate_to:
        case "finnish":
            fi_res = zh_fi(input)
            return fi_res[0]['translation_text']

        case "spanish":
            en_before_res = zh_en(input)
            es_res = en_es(en_before_res[0]['translation_text'])
            return es_res[0]['translation_text']

        case "english":
            en_res = zh_en(input)
            return en_res[0]['translation_text']

        case "german":
            de_res = zh_de(input)
            return de_res[0]['translation_text']
