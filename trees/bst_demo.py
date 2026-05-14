from bst import bst, insert, delete, update, inorder, preorder, postorder 
def get_menu(choice: int):
    menu = {
        1: insert,
        2: delete,
        3: update,
        4: inorder,
        5: preorder,
        6: postorder,
        7: end
    }
    return menu[choice]

def end():
    print("Closing menu")

def run_menu():
    while True:
        print('''
              1: Insert
              2: Delete
              3: Update
              4: Inorder
              5: Preorder
              6: Postorder
              7: Exit
              ''')
        input_choice = int(input("Enter your choice: "))
        if input_choice == 1:
            input_value = int(input("Enter value: "))
            get_menu(input_choice)(bst, input_value)
        if input_choice in [4, 5, 6]:
            get_menu(input_choice)(bst.head)
        if input_choice == 7:
            get_menu(input_choice)()
            break

run_menu()