# projet_nsi_git

On a mis a jour le main.py je n'ai pas réussi avec l'aide de Ambroise de connecter le replit au github du coup j'ai copié collé le code dans le main.py car la semaine d'avant nous n'avons pas mis à jour celui-ci et nous avons mis dans le tableau avec les choses à faire un résumé de chaque séances. https://github.com/venuxiio/projet_nsi_git/projects/1

Jade RICHEZ, Perrine BRON

jeu en vue contre plongée (exemple pokémon)

tapper sur internet pour trouver des idées: 2D games ideas pixel

bibliothèque py.game (python)

description un peu plus détaillée du jeu:

- un personnage se déplace dans un labyrinthe, il a trois vies

- il se retrouve face à une petite maison fermée à clé et ne peut plus avancer

- s'il a la clé il peut entrer sinon il doit aller chercher la clé

- une fois dans la maison il doit faire un jeu ou répondre à une énigme pour ouvrir la porte de sortie de la maison qui lui permet de poursuivre son chemin dans le labyrinthe

- s'il échoue il perd une vie et doit recommencer le jeu ou l'énigme de la maison où il se trouve

- au cours du jeu il peut devenir une fois " passe muraille" et sortir de la maison sans faire le jeu

- il y aurait 4 maisons (2 mini-jeux: mémory et puzzle; 2 énigmes)

______________________________________________________________________________________________________

- pour le moment commencer par mettre une seule petite maison avec un mini jeu dedans pour tester
______________________________________________________________________________________________________

https://github.com/venuxiio/projet_nsi_git/projects/1
chronologie:

- définir le labyrinthe 
- définir sa taille et la taille du zoom
- définir le personnage et sa taille 
- dessiner le labyrinthe et le personnage 
- tester
  - afficher une image avec pygame
  - afficher plusieurs images
  - déplacer une image 
  - le zoom
  - succession d'image


References:


![8d8b062d26bba8fe1bd7a7b76983ac7e](https://user-images.githubusercontent.com/95481660/148552243-fee52830-9433-40b3-838f-67121b02853e.gif)

![image](https://user-images.githubusercontent.com/95481694/145578967-6b2150a0-a88c-4151-9629-f9c089327240.png) ; ![image](https://user-images.githubusercontent.com/95481694/!
145579029-c0f4663f-897a-4eca-a8bb-c9506566b5ae.png)


![image](https://user-images.githubusercontent.com/95481694/145579738-15fb2a74-dddd-4c99-8c1e-bc3dc83667f2.png)

![WEuPTrJ](https://user-images.githubusercontent.com/95481660/146652467-96af5589-a964-4cbc-90c8-5040eda7c303.gif)


Idee du labyrinthe :

![image](https://user-images.githubusercontent.com/95481660/145583625-6f7a5aa6-5061-4b80-a770-b2a0c381d68c.png)

![image](https://user-images.githubusercontent.com/95481660/145786144-4e16f51e-8a48-4ebd-8952-1f184bff4e7f.png)
exemple du logiciel Tiled qui permet de creer des maps
______________________________________________________________________________________________________
banane

![Banana](https://user-images.githubusercontent.com/95481694/149673509-7744600c-aa33-4051-ba73-8164defbb176.png)

Labyrinthe

dimentions: largeur 1600 et hauteur: 1600

![carte](https://user-images.githubusercontent.com/95481660/166211011-093efc05-5b1b-4238-b5d8-af00ca0c6809.png)

______________________________________________________________________________________________________
Idee de l'interieur de la maison

![image](https://user-images.githubusercontent.com/95481660/146652571-97f67b3b-8d09-480f-99ad-19896161a9be.png)


______________________________________________________________________________________________________

Regles du jeu global:
Bonjour et bienvenue dans Escape Adventures! Je vais vous expliquer les règles du jeu. Tout d'abord votre objectif principal c'est de sortir du labyrinthe. Mais attention dans ce labyrinthe (non rassurez vous vous êtes seuls il n'y a pas d'ennemis) mais il y a des petites maisons dans lesquels il y a des épreuves. Vous le verrez il y a trois petites maisons mais ne vous précipitez pas dessus vous avez besoins de quelque chose pour les ouvrir! Fouillez bien tout les petits chemins ! Je vous souhaite bonne chance!
______________________________________________________________________________________________________

Règle du memory :
Maintenant que vous avez reussi a entré dans la maison, vous devez jouer a un jeu de memory afin de passer de l'autre côté de la maisonn et poursuivre votre chemin. Les règles du jeu sont simples: vous devez retourner les cartes afin de trouver toutes les paires. 

______________________________________________________________________________________________________

Règle du qcm Barthélémy:
Bonjour a tous et bienvenue dans mon qcm! Je vais tout de suite vous expliquer les règle de mon mini jeu! Vous allez vous retrouver face à un qcm qui va porter sur des questions de cours mais vous devez faire comme dans questions pour un champion! En effet vous devez répondre juste à 4 questions à la suite. Attention si vous faites faux vous retomberez à 0 et vous devrez tout recommencer!

______________________________________________________________________________________________________

Règle du jeu des boules qui éclatent :
Bravo! Vous avez réussi à accéder à la dernière maison, maitenant il vous reste plus qu'un jeu. Un jeu jsplus le nom mais les règles sont simples: vous devez éclater toutes les boules pour gagner et sortir. Pour éclater les boules vous aurais une planche mobile avec une boule noire. Bonne chance!

______________________________________________________________________________________________________

liens:

tuto pygame : https://www.youtube.com/watch?v=ooITOxbYVTo

lien pytmx : https://www.pygame.org/project-Tiled+TMX+Loader-2036-.html

lien pyscroll : https://github.com/bitcraft/pyscroll

lien pyganim : https://pyganim.readthedocs.io/en/latest/basics.html

dessiner en pixel: https://pixelover.io/

lien pour telecharger des tiles: https://itch.io/game-assets/tag-tileset

lien pour voir pour le memory: https://stackoverflow.com/questions/14636320/card-matching-game-on-python

lien pour créer une page d'accueil: https://www.geeksforgeeks.org/creating-start-menu-in-pygame/
https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Do3VHJ7g7M08&psig=AOvVaw1xsLlno4gO-b0RvSiFzDTq&ust=1652531349593000&source=images&cd=vfe&ved=0CAoQjhxqFwoTCKjmxZK93PcCFQAAAAAdAAAAABAE

lien pour créer un compteur ?: https://stackoverflow.com/questions/55327065/python-pygame-how-do-i-add-a-time-counter-for-my-game
______________________________________________________________________________________________________
logiciels :

Jpixel qui permet de creer des animations en pixel

lien pour telecharger:https://emad.itch.io/jpixel

Tiles pour creer des maps

lien pour telecharger:https://thorbjorn.itch.io/tiled

Bosca ceoil pour creer des musiques et https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjXvuyquNz3AhVQ5IUKHWjrC04QwqsBegQIHhAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DpcdB2s2y4Qc&usg=AOvVaw2vLhAh7yt0f2h3Pa0k5huM

lien pour telecharger:https://terrycavanagh.itch.io/bosca-ceoil

lien piskel : https://www.piskelapp.com/

________________________________________________________________________________________________________

replit:
https://replit.com/@venuxiio/Escape-Adventure#main.py
https://replit.com/@venuxiio/exemple?from=notifications#main.py
