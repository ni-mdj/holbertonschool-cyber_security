# Ruby Scripting - 0x00 Hello World

## Description
Cette section se concentre sur l'introduction à la programmation en Ruby dans le contexte de la cybersécurité. Le projet 0x00 couvre les bases de Ruby avec une fonction simple "Hello, World!".

## Objectifs d'Apprentissage
- Comprendre la syntaxe de base de Ruby
- Écrire et exécuter des fonctions simples en Ruby
- Apprendre les conventions de dénomination Ruby
- Préparer les bases pour des scripts de sécurité plus avancés

## Prérequis
- Ruby installé sur votre système (version 2.7+)
- Éditeur de texte ou IDE (VS Code, RubyMine, etc.)
- Compréhension basique de la programmation

## Installation de Ruby

### macOS (avec Homebrew)
```bash
brew install ruby
```

### Linux (Debian/Ubuntu)
```bash
sudo apt-get install ruby-full
```

### Linux (CentOS/RHEL)
```bash
sudo yum install ruby
```

### Vérifier l'installation
```bash
ruby --version
```

## Fichiers du Projet

### 0-hello_world_function.rb
**Objectif**: Créer et exécuter une fonction simple en Ruby

**Concepts Couverts**:
- Définition de fonction (`def`/`end`)
- Affichage de texte (`puts`)
- Appel de fonction
- Syntaxe de base de Ruby

**Utilisation**:
```bash
ruby 0-hello_world_function.rb
```

**Sortie Attendue**:
```
Hello, World!
```

## Structure de Base d'un Script Ruby

```ruby
#!/usr/bin/env ruby

# Ceci est un commentaire

# Définir une fonction
def my_function
  puts "Ceci est ma fonction"
end

# Appeler la fonction
my_function
```

### Éléments Clés:
- **`#!/usr/bin/env ruby`**: Shebang pour exécuter le script directement
- **`def`**: Mot-clé pour définir une fonction
- **`puts`**: Affiche une chaîne de caractères avec une nouvelle ligne
- **`end`**: Termine la définition de fonction

## Conventions Ruby

### Nommage des Fonctions
- Utiliser des noms en minuscules avec des underscores: `hello_world`, `process_data`
- Les noms de fonctions décrivant une action sont préférés
- Éviter les noms sur une seule lettre (sauf pour les variables de boucle)

### Indentation
- Utiliser 2 espaces pour l'indentation (standard Ruby)
- Pas de tabulations

### Commentaires
```ruby
# Ceci est un commentaire sur une seule ligne

=begin
Ceci est un commentaire sur plusieurs lignes
Utile pour la documentation
=end
```

## Exécution du Script

### Méthode 1: Utiliser Ruby directement
```bash
ruby 0-hello_world_function.rb
```

### Méthode 2: Rendre le script exécutable
```bash
chmod +x 0-hello_world_function.rb
./0-hello_world_function.rb
```

## Concepts Ruby Fondamentaux

### Fonctions (Méthodes)
En Ruby, les fonctions sont aussi appelées "méthodes". Voici les variations:

```ruby
# Fonction simple
def greet
  puts "Bonjour!"
end

# Fonction avec paramètre
def greet(name)
  puts "Bonjour, #{name}!"
end

# Fonction avec valeur de retour implicite
def add(a, b)
  a + b
end

# Fonction avec return explicite
def multiply(a, b)
  return a * b
end
```

### Appel de Fonctions
```ruby
greet
greet("Alice")
result = add(5, 3)
```

### Variables
```ruby
# Variable locale
name = "Alice"

# String (chaîne de caractères)
message = "Hello"

# Entier
count = 42

# Booléen
is_active = true
```

## Exercices Suggérés

### Exercice 1: Fonction avec Paramètre
```ruby
def hello_person(name)
  puts "Hello, #{name}!"
end

hello_person("Bob")
```

### Exercice 2: Fonction avec Retour
```ruby
def double(number)
  number * 2
end

result = double(5)
puts result  # Affichera 10
```

### Exercice 3: Fonction avec Logique
```ruby
def is_even(number)
  if number % 2 == 0
    puts "#{number} est pair"
  else
    puts "#{number} est impair"
  end
end

is_even(4)
is_even(7)
```

## Ressources Utiles

- [Documentation Officielle Ruby](https://ruby-doc.org/)
- [Ruby Style Guide](https://rubystyle.guide/)
- [Try Ruby - Tutoriel Interactif](https://www.ruby-lang.org/fr/documentation/)
- [Ruby pour la Sécurité](https://ruby-doc.org/)

## Prochaines Étapes

Après avoir maîtrisé les bases:
1. Apprendre les structures de contrôle (if/else, boucles)
2. Travailler avec les tableaux et les hashes
3. Créer des classes et des modules
4. Découvrir les gems Ruby utiles pour la cybersécurité
5. Écrire des scripts d'automatisation de sécurité

## Dépannage

### Le script ne s'exécute pas
- Vérifier que Ruby est installé: `ruby --version`
- Vérifier que le fichier a la bonne extension `.rb`
- Assurez-vous que le chemin d'accès est correct

### Erreur: "command not found"
- Vérifier que Ruby est dans le PATH
- Exécuter `which ruby` pour localiser Ruby
- Réinstaller Ruby si nécessaire

### Erreur de syntaxe
- Vérifier l'indentation
- Assurez-vous que toutes les fonctions sont fermées avec `end`
- Utiliser un linter comme `rubocop`

## Informations du Dépôt
- **Dépôt GitHub**: holbertonschool-cyber_security
- **Répertoire**: `scripting_cyber/0x00-ruby_scripting`
- **Fichier**: `0-hello_world_function.rb`

---

**Dernière Mise à Jour**: 8 mai 2026

**Note**: Ruby est un langage élégant et puissant. Explorez-le et créez des scripts de sécurité robustes!
