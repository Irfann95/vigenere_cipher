<h1>Vigenere Cypher Program</h1>

<p>The Vigenère cipher is therefore a special case of a polyalphabetic substitution. First described by Giovan Battista Bellaso in 1553, the cipher is easy to understand and implement, but it resisted all attempts to break it until 1863, three centuries later.<p>

This program uses a similar idea by mapping characters in the key to characters in the alphabet and then using these mappings to encrypt or decrypt the message. However, there are some differences from the traditional Vigenère cipher:

In the traditional Vigenère cipher, the key is repeated to match the length of the plaintext message. This program also repeats the key but ensures it's exactly 25 characters long by cutting or repeating it as needed.

The encryption and decryption functions in this program use slightly different algorithms than the classic Vigenère cipher. For example, in the "addvarriables" function, it uses modulo arithmetic to wrap around the alphabet, which is a bit different from the Vigenère cipher's standard addition.

The program uses a fixed alphabet (26 lowercase letters) rather than allowing for variable alphabets as seen in some Vigenère cipher implementations.

In essence, it employs the Vigenère cipher concept of using a key to shift characters, but it adapts the method for its specific purposes, which may not precisely match the traditional Vigenère cipher algorithm.
