from deep_translator import GoogleTranslator

def translateText(text):
   return GoogleTranslator(source='auto', target='english').translate(text=text)