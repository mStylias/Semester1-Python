import instaloader

# Φόρτωση στιγμιότυπου
print("Σύνδεση με το instagram...")
L = instaloader.Instaloader()
print("Επιτυχία!")
# Υπάρχει ένα bug στα windows που μετά το input το πρόγραμμα σταματάει. Για να διορθωθεί πρέπει
# να δiaγραφεί το win-unicode-console με την εντολή: pip3 uninstall win-unicode-console
print("Για την προβολή ιδιωτικών προφίλ απαιτείται σύνδεση με κάποιο λογαριασμό instagram που να ακολουθεί το συγκεκριμένο προφίλ")
while True:
    login = input("Θέλετε να συνδεθείτε? (y/n) \n")
    if login == "y" or login == "n":
        break
    else:
        print("Λάθος εισαγωγή στοιχείων. Προσπαθήστε ξανά")

if login == "y":
    while True:
        username = input("Πληκτρολογήστε το όνομα χρήστη του λογαριασμού σας \n")
        password = input("Πληκτρολογήστε τον κωδικό \n")
        try:
            L.login(username, password)
            print("Επιτυχής σύνδεση!")
            break
        except:
            print("Λάθος όνομα χρήστη ή κωδικός. Προσπαθήστε ξανά")

while True:
    targetProfile = input("Πληκτρολογήστε το όνομα του στόχου \n")
    try:
        profile = instaloader.Profile.from_username(L.context, targetProfile) #Αποθήκευση του προφίλ
        break
    except:
        print("Το προφίλ είτε δεν υπάρχει είτε δεν είναι προσβάσιμο. Προσπαθήστε ξανά")
        
print("Γίνεται αναζήτηση, παρακαλώ περιμένετε...")
counter = 0 #Για να σταματήσει στα 100 posts (γραμμή 41)
owner = [] #H λίστα με τα ονόματα
for post in profile.get_posts(): #Όλα τα post
    counter += 1
    if counter > 100:
        break
    for comment in post.get_comments(): #Τα σχόλια του κάθε post
        owner.append(comment.owner.username) #Εισαγωγή ονόματος σχολιαστή στη λίστα
owner.sort() #Ταξινόμηση της λίστας ώστε να βρεθεί ο χρήστης με τα περισσότερα σχόλια
c = 1 #Μετρητής
maxc = [] #Λίστα με όλα τα c 
#Χρησιμοποιείται λίστα στην περίπτωση που 2 ή περισσότεροι χρήστες 
#έχουν κάνει τον ίδιο αριθμό σχολίων και αυτός είναι ο μέγιστος

#Βρίσκει πόσες φορές εμφανίζεται το κάθε όνομα
for i in range(1, len(owner)): 
    if owner[i] == owner[i-1]:
        c += 1
    else:
        c = 1
    maxc.append(c) #Παράλληλη λίστα που περιέχει όλα τα c
try:
    maxComment = max(maxc) #Εύρεση μεγαλύτερου στοιχείου της λίστας
    print("Οι παρακάτω χρήστες έχουν κάνει τα περισσότερα σχόλια στο προφίλ του/της", targetProfile + ". Έκαναν", maxComment, "σχόλια ο καθένας")
    for i in range(len(maxc)):
        if maxComment == maxc[i]:
            print(owner[i])
except:
    print("Το συγκεκριμένο προφίλ δεν έχει κανένα σχόλιο")
