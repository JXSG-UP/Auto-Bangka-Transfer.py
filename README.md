# Auto-Bangka-Transfer.py

A simple Python tool that converts text to binary using UTF-8 encoding and represents binary digits as 'Bangka' (邦咔). This tool allows easy encoding and decoding of messages using custom characters. 

Inspired by `Alice Tendo` from *Blue Archive*.

> [!NOTE]
> `The reason for developing this software`
> 
>  In UTC Wednesday, February 5, 2025, Someone in our anime club’s group chat suddenly started sending random, playful words like `呱呱`. I found it amusing and decided to join in. Since I’m a fan of *Blue Archive*, I thought it would be fun to create a program inspired by the character `Alice Tendo`. So, I wrote [this program](https://github.com/JXSG-UP/Auto-Bangka-Transfer.py) to convert text into a binary sequence using `'Bangka'` `(邦咔)`.

## Features
- Convert text into a binary string, represented as 'Bangka' (邦咔).
- Decode 'Bangka' (邦咔) binary back to readable text.
- Automatically copies encoded result to the clipboard.

## Requirements

> [!IMPORTANT]  
> Before using the script, you'll need to ensure that your system has Python 3 installed. You will also need the following Python libraries:

> `pyperclip`: This library is used to copy the encoded text to your clipboard.

To install `pyperclip`, run the following command:

```bash
pip install pyperclip
```

## Usage

1. **Clone or download the repository**:
   - You can download the Python script from the repository or clone it using Git.

   ```bash
   git clone https://github.com/JXSG-UP/Auto-Bangka-Transfer.py.git
   ```

2. **Run the script**:
   - Open a terminal or command prompt and navigate to the directory where the script is located.
   - Execute the script by running:

   ```bash
   python Auto-Bangka-Transfer.py
   ```

3. **Choose the mode**:
   The script will prompt you to select a mode:
   - `1`: Convert text to 'Bangka' binary.
   - `2`: Convert 'Bangka' binary back to text.
   - `0`: Exit the program.

4. **Mode 1: Convert text to 'Bangka' binary**:
   - When you choose this option, you'll be asked to input the text you'd like to convert.
   - The script will convert the text into binary, represent it as 'Bangka' (邦咔), and automatically copy the result to your clipboard.

5. **Mode 2: Convert 'Bangka' binary to text**:
   - When you choose this option, you'll need to input the 'Bangka' binary (with each 8-bit group separated by spaces).
   - The script will convert the binary back to readable text.

## Example

### Convert text to 'Bangka' binary:

1. Select mode `1`.
2. Input text (e.g., `Hello`).
3. The script will output the binary representation using 'Bangka' (邦咔) and copy the result to the clipboard.

```
邦邦咔咔邦邦邦咔 邦邦咔咔邦邦邦咔 邦邦咔咔邦咔邦邦 邦邦咔咔邦咔邦咔
```

### Convert 'Bangka' binary to text:

1. Select mode `2`.
2. Input the 'Bangka' binary (with spaces between each 8-bit group).
3. The script will output the original text.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
