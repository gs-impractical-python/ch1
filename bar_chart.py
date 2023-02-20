"""
Creates a dictionary bar chart of letters used in a sentence.
"""
import json


def create_chart(sentence):
  chart = {}
  for s in sentence:
    if s in chart:
      chart[s].append(s)
    elif s != " ":
      chart[s] = [s]
  return chart


def main():
  while True:
    sentence = input("Enter sentence: ")
    chart = create_chart(sentence)
    print(json.dumps(chart, indent=2))
    try_again = input("Want to try again?: ")
    if "n" in try_again.lower():
      break



if __name__ == '__main__':
  main()
