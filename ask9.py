#Έλεγχος ορθότητας
while True:
    n = input("Δώστε έναν ακέραιο αριθμό \n")
    try:
        n = int(n) #Μετατροπή από string σε int
        break
    except:
        print("Λάθος εισαγωγή, μπορείτε να δώσετε μόνο ακέραιο αριθμό")
#Πράξεις
while True:
    n = n*3+1
    add = str(n) #Μετατροπή σε string ώστε να υπάρχει πρόσβαση σε κάθε ψηφίο
    result = 0
    for i in range(len(add)):
        result += int(add[i]) #Μετατροπή ξανά σε int για να πάρει τιμή το result
    if result < 10:
        break
    else:
        n = result
print("Ο τελικός αριθμός είναι", result)