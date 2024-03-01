import batiment
import infras
import pandas as pd

df = pd.read_excel('c:/Users/kawta/Downloads/reseau_en_arbre.xlsx').drop_duplicates()


def prepare_data(df):
    df = df[df['infra_type'] != 'infra_intacte']
    
    infra_subdfs = df.groupby(by="infra_id")
    liste_infra = []
    
    for infra_id, infra_subdf in infra_subdfs:
        longueur = infra_subdf['longueur'].iloc[0]
        nb_maisons = infra_subdf['nb_maisons'].sum()
        infra_type = infra_subdf['infra_type'].iloc[0]
        infra = infras.Infra(infra_id, longueur, infra_type, nb_maisons)
        difficulte = infra.obtenir_difficulte_infra()
        infra_subdf['difficulté'] = difficulte
        liste_infra.append(infra)


    batiment_subdfs = df.groupby(by="id_batiment")
    liste_batiment = []
    
    for id_batiment, batiment_subdf in batiment_subdfs:
        infra_ids_batiment = batiment_subdf['infra_id'].tolist()
        infra_batiment = [infra for infra in liste_infra if infra.infra_id in infra_ids_batiment]
        
        batiment_instance = batiment.Batiment(id_batiment, infra_batiment)
        total_difficulty_batiment = batiment_instance.obtenir_difficulte_batiment()
        batiment_subdf['difficulté'] = total_difficulty_batiment
        liste_batiment.append(batiment_instance)
    

    return liste_infra, liste_batiment



def planification(liste_infra, liste_batiment):
    liste_batiments_classes = []

    while liste_batiment:
        simple_batiment = min(liste_batiment)
        liste_batiments_classes.append(simple_batiment)

        for infra in simple_batiment.liste_infras:
            infra.reparer_infra()

        liste_batiment.remove(simple_batiment)

    return liste_batiments_classes


liste_infra, liste_batiment = prepare_data(df)
liste_batiments_classes = planification(liste_infra, liste_batiment)

results = []

for index, batiment_classe in enumerate(liste_batiments_classes):
    results.append({"priorite": index,"id_batiment": batiment_classe.id_batiment, "difficulty": batiment_classe.obtenir_difficulte_batiment()})

df_results = pd.DataFrame(results)

df_results.to_csv('results.csv', index=False)

print("Les résultats ont été écrits dans le fichier 'results.csv'.")

