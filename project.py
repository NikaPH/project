#1
'''ნინისთან ცხოვრობს ოთხი ძაღლი (ჯეკა, ტობი, ციცქნა, მოკა) და ერთი კატა (ციცი).
თქვენი ამოცანაა დაწეროთ ფუნქცია, რომელიც გამოთვლის ცხოველების ასაკს.
ფუნქციას არგუმენტად უნდა გადასცეთ თითოეული ცხოველისთვის შესაბამისი
„ადამიანური ასაკი“ და დააბრუნოს რეალურად რამდენი წლისაა ცხოველი.
საბოლოოდ უნდა დაიბეჭდოს რამდენი წლისაა თითოეული ცხოველი.
გაითვალისწინეთ: ძაღლის შემთხვევაში, პირველი „ადამიანური წელი“ შეადგენს ძაღლის 15
წელს, მეორე წელი არის 9 წლის ექვივალენტი, ხოლო ყველა მომდევნო წელი − +5 წელი.
რაც შეეხება კატას, საწყისი ორი წელი იდენტურია, რაც ძაღლთან, ხოლო მესამე წლიდან +4
წელი.
მაგალითად, თუ ციცი სამი ადამიანური წლისაა, მისი ასაკი, 15+9+4, ანუ 28 გამოდის.'''



# def calculate_animal_age(name, human_age):
#     if name.lower() == 'cici':
#         # Cat age calculation
#         if human_age == 1:
#             cat_age = 15
#         elif human_age == 2:
#             cat_age = 15 + 9
#         else:
#             cat_age = 15 + 9 + (human_age - 2) * 4

#         print(f"{name.capitalize()}'s age: {cat_age}")

#     elif name.lower() == 'jeka' or "tobi" or 'cicqna' or 'moka':
#         # Dog age calculation
#         if human_age == 1:
#             dog_age = 15
#         elif human_age == 2:
#             dog_age = 15 + 9
#         else:
#             dog_age = 15 + 9 + (human_age - 2) * 5

#         print(f"{name.capitalize()}'s age: {dog_age}")

#     else:
#         print(f"Unknown animal: {name}")

# # Example usage:
# calculate_animal_age(input('name: '), int(input('what\'s the actual age? ')))   # Calculate cat's age for 3 human years


#2
'''გაქვთ ჩემპიონთა ლიგის გამარჯვებულების სია. თქვენი ამოცანაა დაწეროთ ფუნქცია,
რომელსაც გადასცემთ აღნიშნულ სიას და დამატებით ერთ არგუმენტს (season, team ან
country). თუ არგუმენტად გადაეცემა სეზონი, ამ შემთხვევაში უნდა დაიბეჭდოს არჩეული
სეზონის გამარჯვებული. თუ გადავცემთ გუნდს - დაიბეჭდოს მოცემულ პერიოდში
რამდენჯერ გაიმარჯვა ამ გუნდმა, ხოლო ქვეყნის შემთხვევაში - რამდენჯერ გახდა ამ ქყვეყნის
წარმომადგენელი ჩემპიონი.
მაგალითად, თუ მეორე არგუმენტად გადავცემთ სეზონს 2002-03, უნდა დაბეჭდოს AC Milan.
თუ გადავცემთ გუნდს, მილანს, დაბეჭდოს 2. თუ გადავცემთ ქვეყანას იტალიას, დაბეჭდოს 3.
leagueWinners = [
{'season':'1999-00', 'team':'Real Madrid', 'country':'Spain'},
{'season':'2000-01', 'team':'Bayern Munich', 'country':'Germany'},
{'season':'2001-02', 'team': 'Real Madrid', 'country':' Spain'},
{'season':'2002-03', 'team':'AC Milan', 'country':'Italy'},
{'season':'2003-04', 'team':'Porto', 'country':'Portugal'},
{'season':'2004-05', 'team':'Liverpool', 'country':'England'},
{'season':'2005-06', 'team':'Barcelona', 'country':'Spain'},
{'season':'2006-07', 'team':'AC Milan', 'country':'Italy'},
{'season':'2007-08', 'team':'Manchester United', 'country':'England'},
{'season':'2008-09', 'team':'Barcelona', 'country':'Spain'},
{'season':'2009-10', 'team':'Inter Milan', 'country':'Italy'}]'''




def champions_league_info(league_winners, question):
    if not question:
        print("Please provide a search query.")
        return

    # Search by season
    for winner in league_winners:
        if len(question) == 7 and '-' in question and winner['season'] == question:
            print(f"Season {question} winner: {winner['team']}")
            return

    # Search by team
    team_wins = sum(1 for entry in league_winners if entry['team'].lower() == question.lower())
    if team_wins > 0:
        print(f"The team '{question}' won the Champions League {team_wins} times.")
        return

    # Search by country
    country_wins = sum(1 for entry in league_winners if entry['country'].lower() == question.lower())
    if country_wins > 0:
        print(f"The country '{question}' has representatives who won the Champions League {country_wins} times.")
        return

    print(f"No information found for '{question}'.")

# Example usage:
leagueWinners = [
    {'season': '1999-00', 'team': 'Real Madrid', 'country': 'Spain'},
    {'season': '2000-01', 'team': 'Bayern Munich', 'country': 'Germany'},
    {'season': '2001-02', 'team': 'Real Madrid', 'country': 'Spain'},
    {'season': '2002-03', 'team': 'AC Milan', 'country': 'Italy'},
    {'season': '2003-04', 'team': 'Porto', 'country': 'Portugal'},
    {'season': '2004-05', 'team': 'Liverpool', 'country': 'England'},
    {'season': '2005-06', 'team': 'Barcelona', 'country': 'Spain'},
    {'season': '2006-07', 'team': 'AC Milan', 'country': 'Italy'},
    {'season': '2007-08', 'team': 'Manchester United', 'country': 'England'},
    {'season': '2008-09', 'team': 'Barcelona', 'country': 'Spain'},
    {'season': '2009-10', 'team': 'Inter Milan', 'country': 'Italy'}
]

# Example queries:
champions_league_info(leagueWinners, input('Search: '))  

