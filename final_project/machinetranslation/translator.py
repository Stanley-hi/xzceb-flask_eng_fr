"""Module has two functions that translates English and French"""


from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """translates english to french"""
    text = 'Hello'
    french_text = MyMemoryTranslator(source='english', target='french').translate(text)
    return french_text

def french_to_english(french_text):
    """translates french to english"""
    text = "Bonjour"
    english_text = MyMemoryTranslator(source='french', target='english').translate(text)
    return english_text
