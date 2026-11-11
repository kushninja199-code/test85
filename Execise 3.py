# make kbc with the help of list ?
# ans:
# kbc
print("lets start kon benega crorepati")
print("There are only 5 questions")
questions=[["Who is the author of the epic Indian poem \' Meghaduta \' ?","Valmiki", "Tulsidas","kalidasa","Banabhatta",3],["Who was the first woman to successfully climb K2, the world's second-highest mountain peak?","Junko Tabei","Wanda Rutkiewicz","Tamae Watanabe","Bachendri Pal",2],["Which Mughal ruler's court was home to the poet Zahir Dehlvi, who wrote the personal account of the 1857 revolt titled 'Dastan-e-Ghadar'?","Akbar","Shah Jahan","Aurangzeb","Bahadur Shah Zafar",4],["Which of these personalities was the first to receive the Bharat Ratna posthumously?","Lal Bahadur Shastri","B. K. Kamaraj","Vinoba Bhave","B. R. Ambedkar",1],["In which specific year did the British East India Company officially annex the kingdom of Awadh under the Doctrine of Lapse","1848","1854","1856","1857",3]]
print("level1 3 questions")
levels=[50000,1000000,2000000,5000000,10000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"question is for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"1.{question[1]}           2.{question[2]}")
    print(f"3.{question[3]}          4.{question[4]}")
    reply=int(input("so what is the answer (1-4): "))
    if(reply==question[-1]):
        print(f"correct answer, you won rs. {levels[i]}")
        if i==2:
            print("if you lose next 2 questions you will get 2000000")
            print("level2")
            money=2000000
        if i==4:
            money=10000000
    else:
        print(f"wrong answer!,correct answer is {question[-1]}")
        break
print(f"your take home money is {money}")