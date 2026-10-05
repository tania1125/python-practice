from art import logo
print(logo)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar(original_text, shift_amount, encode_or_decode):

        output_text = ""
        
        if encode_or_decode == 'decode':
            shift_amount *= -1

        for i in original_text:
            if i not in alphabet:
                  output_text += i
            else:
                new_index = (alphabet.index(i) + shift_amount) % 26
                output_text += alphabet[new_index]
        
        print(f"Here is the {encode_or_decode} result: {output_text}")

should_continue = True

while should_continue:
     
    Instruction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount= shift, encode_or_decode= Instruction)

    restrat = input("Type 'Yes' if you want to go again, Otherwise, type 'No'.\n").lower()
    if restrat == "no":
         should_continue = False