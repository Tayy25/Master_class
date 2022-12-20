import os.path


class Fichier:
    def __init__(self,file=open("fichier.txt","a+")):
        self.file = file
        self.file.close()

    def ekri_nan_fichier(self):
        self.file = open("fichier.txt", "a+")
        self.file.write(input("ekri non"))
        self.file.close()

    def efase_kotni(self):
        self.file = open("fichier.txt", "w")
        pass

    def efase_fichier(self):
        if os.path.exists("fichier.txt"):
            os.remove("fichier.txt")

    def afiche_fichier(self):
        self.file = open("fichier.txt", "r+")
        print(self.file.readline())
        self.file.close()

fichier1 = Fichier()
#fichier1.ekri_nan_fichier()
#fichier1.efase_kotni()
#fichier1.afiche_fichier()
fichier1.efase_fichier()