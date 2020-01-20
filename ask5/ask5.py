words = open("article.txt", encoding="utf8").read().split()
textLength = len(words)
for i in range(textLength):
    wordLength =  len(words[i]) #Παίρνει το μήκος της κάθε λέξης
    if wordLength > 3:
        word = list(words[i]) #Δημιουργεία λίστας με τα γράμματα της λέξης
        j = 0
        l = len(word)
        punOnStart = False #Σημείο στίξης στην αρχή της λέξης
        punOnEnd = False #Σημείο στίξης στο τέλος της λέξης
        while j<l: #Για να μπουν τα σημεία στίξης στο σωστό σημείο
            if word[j]=="," or word[j]=="." or word[j]=="”" or word[j]=="“" or word[j]=="’":
                if j == 0:
                    punOnStart = True #Υποδεικνύει ότι υπάρχει σημείο στίξης στην αρχή της λέξης
                elif j==l-1:
                    punOnEnd = True #Υποδεικνύει ότι υπάρχει σημείο στίξης στο τέλος της λέξης
                else: #Αλλιώς υπάρχει ενδιάμεσα σημείο στίξης οπότε αφαιρείται
                    word.pop(j) 
                    l -= 1 #Μείωση του μήκους της λίστας επειδή αφαιρέθηκε ένα στοιχείο
                    j -= 1 #Για να μην σταματήσει να ψάχνει πριν τσεκάρει όλα γράμματα
            j += 1
        #Μετάθεση γραμμάτων σύμφωνα με την άσκηση
        if punOnStart and not punOnEnd: #Aν υπάρχει σημείο στίξης στην αρχή, αλλά όχι στο τέλος
            firstLetter = word[1]
            word.pop(1)
            word.extend([firstLetter, "ay"])
        elif not punOnStart and punOnEnd: #Αν υπάρχει στο τέλος αλλά όχι στην αρχή
            firstLetter = word[0]
            word.pop(0)
            word.insert(-1, firstLetter + "ay")
        elif punOnStart and punOnEnd: #Αν υπάρχει και στην αρχή και στο τέλος
            firstLetter = word[1]
            word.pop(1)
            word.insert(-1, firstLetter + "ay")
        else: #Αν δεν υπάρχει καθόλου
            firstLetter = word[0]
            word.pop(0)
            word.extend([firstLetter, "ay"])
        empty = ""
        words[i] = empty.join(word) # Ενοποίηση των γραμμάτων και εισαγωγή της τροποποιημένης λέξης πίσω στη λίστα των λέξεων
#Εκτύπωση της λίστας
for i in range(len(words)):
    print(words[i])