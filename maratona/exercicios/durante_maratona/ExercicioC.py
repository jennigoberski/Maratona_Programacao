"""
Since the Infinite Improbability Drive, many do not question about life on other planets, and deepen in the most unlikely questions,
as, for example, is that beings from other planets using the same characters we write to? And if this is true, they will use the same
vowels like us? With this in mind, many scientists have designed various types of alien alphabets, using our alphabet letters, and the
digits 0 to 9, with their respective vowels. On this basis, they are asking for help to identify vowels in alien alphabets and make counts about.
Write a program that, given a sequence of vowels in a given alien alphabet, to count, in a text written with the same alphabet, how many alien
vowels the text has.
Input There will be several test cases. Each test case is formed by two lines. The first line informs a word formed by all letters of a
particular alien planet. The second line contains a phrase made ​​up of letters of the same alphabet. The entry ends with end of file.

Output For each test case, print the amount of corresponding alien vowels.

Input Sample:
aeiou
o rato roeu a roupa do rei de roma

Output Sample:
16
.....

Input Sample:
4310
t3st3 p4r4 c0d1f1c4r

Output Sample:
8
....

Input Sample:
kwy
the quick brown fox jumps over the lazy dog

Output Sample:
3
....
"""

while(1):
  letras = input()
  if letras == '':
    break
  frase = input()
  contagem = 0
  pattern = []
  for letra in letras:
    contagem = contagem+  frase.count(letra)
  print(contagem)