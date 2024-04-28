import mysql.connector

# Connection to the Database
conn = mysql.connector.connect(
    host="localhost",        
    user="root",
    password="shivusql",
    database="recipe" 
)

# Function to add a new recipe
def add_recipe():
    dishname = input("Enter the name of the dish: ")
    ingredients = input("Enter ingriedients: ")
    procedures = input("Enter the procedure for the recipe: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (dish_name, ingredients, procedures) VALUES (%s, %s, %s)", (dishname, ingredients, procedures))
    conn.commit()
    print("Recipe added successfully!")

# Function to search for existing recipes by title
def search_recipe():
    title = input("Enter the title of the recipe to search for: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE dish_name LIKE %s", ("%" + title + "%",))
    recipes = cursor.fetchall()
    if recipes:
        print("Found Recipe:")
        for recipe in recipes:
            print(f"Title: {recipe[1]}")
            print(f"INGREDIENTS: {recipe[2]}")
            print(f"Procedures: {recipe[3]}")
            print()
    else:
        print("No recipes found with that title.")

# Display menu options
def display_menu():
    print("Choose an option:")
    print("1. Add a new recipe")
    print("2. Search for existing recipes")
    print("3.Exit")
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        add_recipe()
        return True  
    elif choice == "2":
        search_recipe()
        return True  
    elif choice == "3":
        return False
    else:
        print("Invalid choice!")
        return True  

# Usage: Call the display_menu() function in a loop
while True:
    if not display_menu():
        break 
