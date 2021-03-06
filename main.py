import re

string = "De Clippeleer Jessika	B, L, T, V	Alternatieve (pseudo)granen voor de productie van innovatieve bieren	   	viewDegroote Jeroen, Michiels Joris	B, L, T, V	Automatische pneumatische voedersystemen voor precisievoedering van landbouwdier...	   	viewWerbrouck Stefaan	B, L, T, V	Bacteriën als blinde passagiers in planten	   	viewBriers Yves	B, L, T, V	Bacteriofaag-geïnspireerde alternatieven voor antibiotica	   	viewWerbrouck Stefaan	B, L, T, V	Bedrieglijk zoete planten	   	viewDewitte Kevin	B, L, T, V	De productie van eiwithoudende gewassen met het oog op het produceren van evenwi...	   	viewEeckhout Mia	B, L, T, V	De vleesalternatieven uitgespit.	   	viewMouazen Abdulmounem	B, L, T, V	Detectie van alternaria in aardappel door kunstmatige intelligentie	   	viewFievez Veerle	B, L, T, V	Eenvoudige druppelgrootte-metingen op melk als barometer voor de metabole status...	   	viewAudenaert Kris	B, L, T, V	Het bevorderen van de plantengroei door Serendipita isolaten: richting een prakt...	   	viewDe Clippeleer Jessika	B, L, T, V	Hop als bittere smaakmaker in bier: meten is weten	   	viewBriers Yves	B, L, T, V	Identificatie en analyse van bacteriofaagstaartvezels	   	viewEeckhout Mia	B, L, T, V	In kaart brengen van het effect van product en procesparameters bij hamermolen v...	   	viewRuyssen Tony	B, L, T, V	In situ productie van GOS-prebiotica	   	viewDe Leyn Ingrid	B, L, T, V	Invloed van de bewerking van tarwebloemdeeg op de bakwaardigheid van enkele tarw...	   	viewJacxsens Liesbeth	B, L, T, V	Last mile concept : hoe hygiëne te waarborgen ?	   	viewFievez Veerle	B, L, T, V	Melk kan de koe een spiegel voorhouden, maar hoe krijgen we deze spiegel in de s...	   	viewLachat Carl, Schouteten Joachim	B, L, T, V	Nutriscore in UGent resto	   	viewSonck Bart	B, L, T, V	Onderzoek naar de relatie tussen dier-, voeder- en productieparameters en methaa...	   	viewBriers Yves	B, L, T, V	Ontwikkelen van educatief kaartspel voor het aanleren van kloneringsstrategieën	   	viewBriers Yves	B, L, T, V	Ontwikkelen van educatief kaartspel voor het aanleren van proteïne-opzuiverings...	   	viewBaeten Lander, Mertens Jan	B, L, T, V	Opstellen van indicatoren voor het UGent-Biodiversiteitsplan	   	viewDe Gelder Leen	B, L, T, V	Opvolging van denitrificatie via de redoxpotentiaal: openen van de black box	   	viewJacxsens Liesbeth, Van Bockstaele Filip	B, L, T, V	Productinnovatie en novel food wetgeving : een spanningsveld ?	   	viewDewettinck Koen, Messens Kathy	B, L, T, V	Rol van organische zuren in de zure flavour van cacao	   	viewSonck Bart, Tuyttens Frank, Vandaele Leen	B, L, T, V	Studie van mogelijke praktische maatregelen ter preventie van hittestress bij me...	   	viewDe Gelder Leen	B, L, T, V	Sturen van het microbieel rotingsproces van hennep voor textieltoepassingen	   	viewDegroote Jeroen, Michiels Joris	B, L, T, V	Voederopnamegedrag van jonge biggen, onderzoek aan de hand van cameraobservatie ...	   	view"
regex = "(.*?)B, L, T, V	(.*?)   	view"
subj_list = re.findall(regex,string)

jesse, lau, lenn, pieter =  [0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,0],[0,0,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,0],[0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,1,0,0,0]

for j in range(28):
    if jesse[j] + lau[j] + lenn[j] + pieter[j] >= 3:
        with open("test.txt","a+") as f:
            f.write(" - ".join(subj_list[j])+"\n")


proj = []
with open("test.txt","r+") as k:
    for line in k:
        proj.append(line.strip('\n'))

pj,pl,pla,pp = [4,3,2,0,1],[4,3,2,0,1],[4,3,2,0,1],[4,1,3,0,2] #higher means better
new = [(pj[t]+pl[t]+pla[t]+pp[t]) for t in range(len(pj))]



