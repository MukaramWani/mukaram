#Q1
dict1 = {
    "name":"Mukaram",
    "class":10,
    "roll no.":23,
    "section":"red",
    "phone no.":1234567890
}
print(dict1)

#Q2
#As appennd is not  a function inn ppython, Thus, used .updatefubction
dict1.update ({
                        "parentage":"abcc"
                        })
print(dict1)

#Q3
dict2 = {}
dict2.update ({"language": "python"})
print (dict2)

#Q4
for i in dict1.keys ():
                   print(i)


#Q5
dict10 = {
                "name":"muukaram",
                "class":"10",
                "sec":"red",
                "roll no.":"23",
                "parentage":"abc",
                "phone no.":"9999999999",
                "city":"srinagar",
                "school":"gvei",
                "language":"python",
                "class2":"ai"
                }
for t in dict10.values():
        print(t)
        
#Q6
dictq6 = {
                "name":"muukaram",
                "class":"10",
                "sec":"red",
                "roll no.":"23",
                "parentage":"abc",
                "phone no.":"9999999999",
                "city":"srinagar",
                "school":"gvei",
                "language":"python",
                "class2":"ai"
                }
dictq6.popitem()
print(dictq6)

#Q7
dictq7 = {
                "books":["english","science","maths"],
                "cars":["suvs","sports","trucks"]
                }
                
print(dictq7)