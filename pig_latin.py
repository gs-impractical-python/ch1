"""
Pig Latin generator
"""


class PigLatin:
  def __init__(self, words):
    self._words_split = self._split(words)
    self._translated = self._translate(self._words_split)

  @property
  def words_split(self):
    return self._words_split

  @words_split.setter
  def words_split(self, words):
    self._words_split = self._split(words)

  def _split(self, words):
    return words.split()

  def _translate(self, words_split):
    translated = []
    for word in words_split:
      if word[0].lower() in "aeiou":
        translated.append(word + "way")
      else:
        pl_word = word[1:] + word[0].lower() + "ay"
        translated.append(pl_word)
    return " ".join(translated)


def main():
  """Do the thing"""
  while True:
    text = input("Enter string: ")
    translate = PigLatin(text)
    print(translate._translated)
    try_again = input("Want to try again?: ")
    if "n" in try_again.lower():
      break


if __name__ == '__main__':
  main()
