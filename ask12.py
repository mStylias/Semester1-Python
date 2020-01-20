#Βιβλιοθήκες
from datetime import datetime, date

#Ελεγχος ορθότητας
def validate(date):
    try:
        global UserDate
        UserDate = datetime.strptime(date, '%d/%m/%Y')
        return True
    except:
        print("Λανθασμένη ημερομηνία, πρέπει να έχει τη μορφή: ΗΗ/ΜΜ/ΕΕΕΕ")
        return False

while True:
    if validate(input("Πληκτρολογήστε μία ημερομηνία σε μορφή ΗΗ/ΜΜ/ΕΕΕΕ \n")):
        break

#Μέρες του δοθέντος μήνα
Uyear = UserDate.year
Umonth = UserDate.month
Uday = UserDate.day
if Umonth == 12: #Γιατί ο 12ος μήνας θα γινόταν 13 και θα κράσαρε στη γραμμή 25
    days = 31 #Ο Δεκέμβριος έχει πάντα 31 μέρες
else:
    days = (date(Uyear,Umonth+1,Uday) - date(Uyear,Umonth,Uday)).days
print("Ο συγκεκριμένος μήνας έχει", days, "μέρες.")

#Διαφορά της δοθείσας ημερομηνίας από σήμερα
today = datetime.now()
diff = abs(today-UserDate)
diffHours = int(diff.days*24 + diff.seconds//3600)
if UserDate>today:
    diffSeconds = (diffHours-(23-today.hour))*60*60 + (diff.seconds) #23-today.hour επειδή αν πχ τώρα 8 το πρωί απομένουν 24-9=15 ή 23-8=15 ώρες για το τέλος της ημέρας 
else:
    diffSeconds = (diffHours-today.hour)*60*60 + diff.seconds #παίρνει τα δευτερόλεπτα από τις ώρες που είναι γνωστές, αφαιρεί τις τρέχουσες ωρες και προσθέτει τα τρέχοντα δευτερόλεπτα
print("Οι δύο ημερομηνίες απέχουν", diff.days, "μέρες", diffHours, "ώρες ή", diffSeconds, "δευτερόλεπτα.")