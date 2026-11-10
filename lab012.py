#Document Analysis System
sentence = input("Enter a sentence: ")
words = sentence.split()
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_characters = 0

for char in sentence:

    if char.lower() in "aeiou":
        vowels += 1

    elif char.isalpha():
        consonants += 1

    elif char.isdigit():
        digits += 1

    elif char == " ":
        spaces += 1

    else:
        special_characters += 1

total_characters = len(sentence)

print("==========================================")
print("        DOCUMENT ANALYSIS REPORT")
print("==========================================")

print("Sentence:", sentence)
print("Total characters:", total_characters)

print("--- Character Breakdown ---")
print("Words:", len(words))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special_characters)

total_letters = vowels + consonants

if total_letters > 0:
    vowel_percentage = (vowels / total_letters) * 100
else:
    vowel_percentage = 0

print("--- Summary ---")
print("Total letters:", total_letters)
print("Vowel percentage:", round(vowel_percentage, 1), "%")

print("==========================================")
print("Analysis Complete!")
print("==========================================")