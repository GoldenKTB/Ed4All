from transformers import pipeline

## Basic translation model.

translationPipeline = pipeline("translation_en_to_de")
print(translationPipeline("I love ice cream."))

