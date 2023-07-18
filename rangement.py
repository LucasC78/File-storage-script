def rangement_fichier():
  import os 
  import shutil

  #On indique le chemin du dossier à trier
  chemin = "D:/pc/pc/dossier_a_trier"

  # On liste tous les fichiers qui se trouvent dans le dossier
  liste_elements = os.listdir(chemin)

  for element in liste_elements:
    nom, extension = os.path.splitext(element)
    if extension == "":
      pass
    else:
      extension = extension[1:]
    # Déplacer les fichiers dans le bon dossier
    if os.path.exists(chemin+"/"+extension): # /dossier_a_trier/mp3
      ### à compléter
      shutil.move(chemin+"/"+element, chemin+"/"+extension+"/"+element)
    else:
      os.makedirs(chemin+"/"+extension) # Le dossier est créé
      shutil.move(chemin+"/"+element, chemin+"/"+extension+"/"+element)
      
rangement_fichier()