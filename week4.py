import json
import difflib
with open('c:/Users/ADMIN/Documents/plpmodules/python/week_4/data.json') as json_file:
     data = json.load(json_file)

#print(type(data))
#print(data.keys())
#removing 
def format_string(json_data):
    for key, value in json_data.items():
        if isinstance(value, list) and len(value) > 0:
            cleaned_value = value[0]
            json_data[key] = cleaned_value

    return json_data

cleaned_data = format_string(data)

def searchWord(word):
          
    if word in cleaned_data:
        print(f"{word.title()} is in the dictionary and it means {cleaned_data[word].lower()}")
    else:
        similar_words = difflib.get_close_matches(word,cleaned_data.keys())
        similar_words = [words for words in similar_words if len(words)>1]
        if similar_words:
            suggestions = ", ".join(similar_words)
            choice = input(f"Did you mean {suggestions}? Enter correct word from list, if the word is not there type No: ")
            if choice.lower() == "no":
                return (f"{word.title()} is not in the dictionary.")
            elif choice.lower() in cleaned_data:
                return f"{choice.title()} means {cleaned_data[choice].lower()}"                
        else:
            print(f"{word.title()} is not in the dictionary.")  


word = input("What word are you looking for: ").lower()
result = searchWord(word)
print(result)