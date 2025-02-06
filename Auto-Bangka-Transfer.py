import pyperclip

def text_to_bangka(text):
    """
    Converts text to a custom binary format using '邦' and '咔' for '0' and '1'.
    """
    # Encode text to UTF-8 bytes
    byte_data = text.encode('utf-8')
    
    # Convert bytes to binary string
    binary_str = ' '.join(format(byte, '08b') for byte in byte_data)
    
    # Replace binary '0' with '邦' and '1' with '咔'
    bangka = binary_str.replace('0', '邦').replace('1', '咔')
    
    # Copy result to clipboard
    pyperclip.copy(bangka)
    
    return bangka

def bangka_to_text(bangka):
    """
    Converts custom binary back to text.
    """
    try:
        # Convert '邦' and '咔' back to binary '0' and '1'
        binary_str = bangka.replace('邦', '0').replace('咔', '1')
        
        # Split into 8-bit binary groups
        binary_groups = binary_str.split(' ')
        
        # Convert binary to byte data
        byte_data = bytes(int(group, 2) for group in binary_groups)
        
        # Decode byte data to text
        text = byte_data.decode('utf-8', errors='replace')
        return text
    except Exception as e:
        # Handle conversion errors
        return f"Conversion error: {str(e)}"

def main():
    """
    Main interface for user interaction to convert text and binary.
    """
    while True:
        print("Choose a mode:")
        print("1. Text to custom binary")
        print("2. Custom binary to text")
        print("0. Exit\n")
        
        mode = input("Enter mode number (1, 2, or 0): ")

        if mode == '1':
            input_text = input("Enter text: ")
            result = text_to_bangka(input_text)
            print("Converted result:", result)
            print("Result copied to clipboard!\n")
        elif mode == '2':
            input_bangka = input("Enter custom binary: ")
            result = bangka_to_text(input_bangka)
            print("Converted result:\n", result)
        elif mode == '0':
            print("Exiting program.\n")
            break
        else:
            print("Invalid mode!\n")

if __name__ == "__main__":
    main()
