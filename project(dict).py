d1 = "conception", "turnover", "wagon", "fleet"
print(d1)
d2 = {"conception": "A conception of something is an idea that you've in your mind",
      "turnover": "Turnover is the value of goods or services sold during particular period of time",
      "wagon": "Wagon is a large container on wheels. which is pulled by train",
      "fleet": "A fleet is a group of ships"}
person = input("Search the above given words:")
print(d2.get(person))

