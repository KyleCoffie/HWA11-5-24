from text_utils import reverse_string as r_str, capitalize_string as c_str

def main():
    text = input("Enter the text you wish to play with:")
    choice = input("Select a text utility: capitalize or reversed ")
    if choice == 'capitalize':
        print (f"{text} in call caps is: {c_str(text)}")
        
    elif choice == 'reversed':
        print (f"{text} in reverse is: {r_str(text)}")
        
    
        
if __name__ == "__main__":
    main()