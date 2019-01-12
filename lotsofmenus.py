from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Mata Kimbala", email="mata.kimbala@gmail.com")
session.add(User1)
session.commit()

User2 = User(name="Isaac Redford", email="iredford@gmail.com")
session.add(User2)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Cheesy French Fries",
                     description="Sprinkled with cheese, onions, and bacon",
                     price="$4.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Burger",
                     description="Juicy grilled chicken patty on a house made \
                     bun with tomato, mayo and lettuce",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chocolate Cake",
                     description="Baked fresh daily and icing made by hand",
                     price="$5.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Sal's Sirloin Burger",
                     description="Made with 90% lean beef on a house made bun \
                     and topped with onion rings",
                     price="$10.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Root Beer",
                     description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese",
                     price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Veggie Burger",
                     description="Made with fresh veggies and cajun spices",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chicken Stir Fry",
                     description="With your choice of noodles vegetables \
                     and sauces.Ask server for details.",
                     price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing \
                     that has been prepared since the Imperial Era.",
                     price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Spicy Tuna Roll",
                     description="Seared rare ahi, avocado, edamame, \
                     cucumber with wasabi soy sauce.",
                     price="$15.00", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Nepali Momo ",
                     description="Steamed dumplings made with vegetables, \
                     spices and meat. ",
                     price="$12.00", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Beef Noodle Soup",
                     description="A Chinese soup made of stewed or \
                     braised beef, beef broth, vegetables and noodles.",
                     price="$6.99", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Ramen",
                     description="Japanese noodle soup dish. It consists \
                     of thin wheat noodles served in a meat- or \
                     fish-based broth, often flavored with soy sauce or miso. \
                     Toppings include sliced pork, dried seaweed, kamaboko, \
                     or green onions.",
                     price="$8.99", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant3 = Restaurant(user_id=1, name="Panda Garden")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Pho",
                     description="Vietnamese noodle soup consisting of broth, \
                     linguine-shaped rice noodles called banh pho, \
                     a few herbs, and meat.",
                     price="$7.99", course="Entree", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chinese Dumplings",
                     description="A common Chinese dumpling which generally \
                     consists of minced meat and finely chopped vegetables \
                     wrapped into a piece of dough skin. The skin can be \
                     either thin and elastic or thicker.",
                     price="$9.99", course="Appetizer", restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Gyoza",
                     description="Light seasoning of Japanese gyoza with \
                     salt and soy sauce, and in a thin gyoza wrapper.",
                     price="$10.99", course="Entree", restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Stinky Tofu",
                     description="Taiwanese dish, deep fried fermented tofu \
                     served with pickled cabbage.",
                     price="$8.99", course="Entree", restaurant=restaurant3)

session.add(menuItem4)
session.commit()


# Menu for Thyme for that
restaurant4 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Tres Leches Cake",
                     description="Rich, luscious sponge cake soaked in sweet \
                     milk and topped with vanilla bean whipped cream and \
                     strawberries.",
                     price="$8.99", course="Dessert", restaurant=restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Mushroom risotto",
                     description="Portabello mushrooms in a creamy risotto.",
                     price="$6.99", course="Entree", restaurant=restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine \
                     tea jelly, grass jelly, caramel, cream, and freshly \
                     made mochi.",
                     price="$7.99", course="Dessert", restaurant=restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Cauliflower Manchurian",
                     description="Golden fried cauliflower florets in a midly \
                     spiced soya,garlic sauce cooked with fresh cilantro, \
                     celery, chilies,ginger & green onions.",
                     price="$4.99", course="Appetizer", restaurant=restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Aloo Gobi Burrito",
                     description="Vegan goodness. Burrito filled with rice, \
                     garbanzo beans, curry sauce, potatoes (aloo), fried \
                     cauliflower (gobi) and chutney.",
                     price="$7.99", course="Entree", restaurant=restaurant4)

session.add(menuItem5)
session.commit()


# Menu for Tony's Bistro
restaurant5 = Restaurant(user_id=1, name="Tony\'s Bistro ")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Shellfish Tower",
                     description="Lobster, shrimp, sea snails, crawfish, \
                     stacked into a delicious tower.",
                     price="$10.99", course="Entree", restaurant=restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken and Rice",
                     description="Boiled chicken with white rice and \
                     white gravy.",
                     price="$9.99", course="Entree", restaurant=restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Momma Mia's Spaghetti",
                     description="Spaghetti with house made tomato basil \
                     sauce and sprinkled with mild Italian sausage.",
                     price="$6.99", course="Entree", restaurant=restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Easy Mint Chocolate Chip Ice Cream",
                     description="Made with the freshest ingredients \
                     including milk, cream, sugar, salt, vanilla extract \
                     and peppermint extract. Served in a bowl for two.",
                     price="$7.95", course="Dessert",
                     restaurant=restaurant5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Tonkatsu Ramen",
                     description="Ramen noodles served in a delicious \
                     pork-based broth with a soft-boiled egg.",
                     price="$7.99", course="Entree", restaurant=restaurant5)

session.add(menuItem5)
session.commit()


# Menu for Vishnu's Fine Indian Cuisine
restaurant6 = Restaurant(user_id=1, name="Vishnu\'s Fine Indian Cuisine")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chicken65",
                     description="A deep fried chicken with authentic \
                     Indian species.",
                     price="$8.99", course="Appetizer", restaurant=restaurant6)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chicken Tikka Masala",
                     description="Chicken tikka masala is a dish of \
                     chunks of roasted marinated chicken in a spiced \
                     curry sauce.",
                     price="$7.99", course="Entree", restaurant=restaurant6)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Lamb Curry",
                     description="Slow cooked lamb meat in a pool of \
                     tomatoes, onions and garam marsala spice.",
                     price="$9.99", course="Entree", restaurant=restaurant6)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Mango Lassi",
                     description="Mango Lassi is a delicious blend \
                     of mangoes and yogurt with a touch of cardamom.",
                     price="$4.99", course="Beverage", restaurant=restaurant6)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Gulab Jamun",
                     description="Gulab jamun are a milk-solid-based \
                     sweet from the Indian subcontinent, popular in India, \
                     Nepal, Pakistan, and Bangladesh, as well as Myanmar.",
                     price="$6.99", course="Dessert", restaurant=restaurant6)

session.add(menuItem5)
session.commit()


# Menu for Mercado's Mexican Restaurant
restaurant7 = Restaurant(user_id=2, name="Mercado\'s Mexican Restaurant")

session.add(restaurant7)
session.commit()


menuItem1 = MenuItem(user_id=2, name="Super Burrito Al Pastor",
                     description="Marinated pork served on tortillas, and \
                     served with rice and beans.",
                     price="$8.99", course="Entree", restaurant=restaurant7)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=2, name="Chilaquiles",
                     description="a dish of fried tortilla strips typically \
                     topped with a spicy tomato sauce and cheese.",
                     price="$9.99", course="Entree", restaurant=restaurant7)

session.add(menuItem2)
session.commit()

print("added menu items!")
