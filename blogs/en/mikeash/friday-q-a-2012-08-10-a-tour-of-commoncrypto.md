---
title: 'Friday Q&A 2012-08-10: A Tour of CommonCrypto'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b5c3c8f7e51b0450'
translated: false
---

> 原文：[Friday Q&A 2012-08-10: A Tour of CommonCrypto](https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)　·　mikeash.com Friday Q&A

Posted at 2012-08-10 13:21 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-08-24: Things You Never Wanted To Know About C](https://www.mikeash.com/pyblog/friday-qa-2012-08-24-things-you-never-wanted-to-know-about-c.html)  
Previous article: [Friday Q&A 2012-07-27: Let's Build Tagged Pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)  
Tags: [cryptography](https://www.mikeash.com/pyblog/?tag=cryptography) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa)

Friday Q&A 2012-08-10: A Tour of CommonCrypto

by [Mike Ash](https://www.mikeash.com/)

**Hashes**  
Facilities for computing cryptographic hashes, also known as digests, are located in `CommonDigest.h`. There are a large number of different hashes provided, each with its own functions, ranging from the commonplace like SHA-1 to unusual ones like MD2.

As a quick recap, a cryptographic hash function is a function that maps an arbitrarily large piece of data into a small piece of data, such that `x = y` always means that `f(x) = f(y)`, and `f(x) = f(y)` implies `x = y` to high probability. In other words, if two pieces of data have the same cryptographic hash, you can be highly confident that they have the same contents. They are also _preimage resistant_, meaning that if you only have `f(x)`, it's infeasible to recover `x`.

Each hash in `CommonDigest.h` has a state structure and three functions for manipulating it. The `Init` function initializes the state structure. The `Update` function feeds data into the hash computation. The `Final` function then computes the hash of the data that was provided. All of these hashes are streaming hashes, so you can feed data in one piece at a time, and then compute a hash of the entire data without ever needing to have everything in memory at once.

Let's look at an example of how to compute the SHA-1 hash of a few different pieces of data, in this case a hypothetical username and machine identifier. We'll presume they've already been transformed into `NSData` instances. For strings, you'd probably want to convert them to `NSData` using an encoding like UTF-8, possibly after applying a Unicode normalization with something like `NSString`'s `decomposedStringWithCanonicalMapping` method. Here are the hypothetical `NSData` variables:

```
    NSData *username = ...;
    NSData *machineIdentifier = ...;
```

Next, we create and initialize the state structure for `SHA-1`:

```
    CC_SHA1_CTX context;
    CC_SHA1_Init(&context);
```

Then we feed the data into the context using the `Update` function:

```
    CC_SHA1_Update(&context, [username bytes], [username length]);
    CC_SHA1_Update(&context, [machineIdentifier bytes], [machineIdentifier length]);
```

Finally, we compute the hash using the `Final` function. We have to allocate storage for the hash ourselves, but there's a convenient macro that tells us how long it is. `NSMutableData` makes for an ideal target for the hash data:

```
    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CC_SHA1_Final([hash mutableBytes], &context);
```

The hash is now in the `hash` variable. Note that this is the raw hash, not a human-readable version. If you need it in a format like hexadecimal, you'll have to perform that conversion yourself afterwards.

As a convenience, there's also a function provided that wraps up the `Init`, `Update`, `Final` sequence into a single call, when you need to compute the hash of a single chunk of data. You'd use it like this:

```
    NSData *toHash = ...;
    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CC_SHA1([toHash bytes], [toHash length], [hash mutableBytes]);
```

All of the other hashes have the same context structure and four functions, with the hash's name where `SHA1` is in these functions. See the `CommonDigest.h` header for the full list of what's available.

Note that, for legacy reasons, all of these functions return a code that indicates success or failure. However, these functions cannot fail, and that return value is safe to ignore.

**HMACs**  
HMAC stands for Hash-based Message Authentication Code. An HMAC combines a cryptographic hash with a secret key to provide _authentication_. Using an HMAC, you can authenticate a piece of data as having come from someone else in possession of the secret key. CommonCrypto provides HMAC functions in `CommonHMAC.h`.

The HMAC functions are similar to the hash functions, except instead of a separate set of functions for each hash, there's a single set of functions that takes a parameter to indicate which hash function to use. The list of available hash functions is listed in an enumeration at the top of the header file.

Here's a quick example of computing an HMAC of a piece of data using the `Init`, `Update`, `Final` sequence, using SHA-1 as the hash function:

```
    NSData *key = ...;
    NSData *data = ...;

    CCHmacContext context;
    CCHmacInit(&context, kCCHmacAlgSHA1, [key bytes], [key length]);
    CCHmacUpdate(&context, [data bytes], [data length]);

    NSMutableData *hash = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CCHmacFinal(&context, [hash mutableBytes]);
```

Just like the hash functions, there's a single `CCHmac` function which does the entire sequence at once for a single chunk of data.

**Key Derivation Functions**  
A key derivation function is another derivative of a cryptographic hash. A key derivation function takes a password and a salt and computes a key from them, which is basically random-looking data derived from the password and salt. CommonCrypto provides key derivation functions in `CommonKeyDerivation.h`.

This can be used to generate encryption keys from a password, for example to securely password-protect a file. It can also be used to securely authenticate users without allowing an attacker to extract their password from your authentication database if it's compromised.

A good key derivation function supports _key stretching_, where the function is artifically hardened to take more time to compute. An authenticated user only has to compute the function once, so it's acceptable for it to take a substantial amount of time. An attacker is guessing many passwords, so taking a large amount of time for each guess makes the process extremely slow. For example, a key derivation function that takes one second to compute is fine for authentication, but requiring one second per guess makes it infeasible for an attacker to guess the password.

CommonCrypto provides a single key-derivation function, PBKDF2, which supports key stretching by allowing the caller to specify a number of rounds. The key derivation function is computed with the `CCKeyDerivationPBKDF` function. To help with deciding how many rounds to use, the `CCCalibratePBKDF` can be used to figure out how many rounds are needed to make the function take a certain amount of time.

Here's an example of deriving a key from a password using PBKDF2 based on SHA-1:

```
    NSData *password = ...;
    NSData *salt = ...;

    // Figure out how many rounds needed for 1000ms computation time
    uint rounds = CCCalibratePBKDF(kCCPBKDF2,
                                   [password length],
                                   [salt length],
                                   kCCPRFHmacAlgSHA1,
                                   CC_SHA1_DIGEST_LENGTH),
                                   1000);

    // Derive the key
    NSMutableData *derivedKey = [NSMutableData dataWithLength: CC_SHA1_DIGEST_LENGTH];
    CCKeyDerivationPBKDF(kCCPBKDF2,
                         [password bytes],
                         [password length],
                         [salt bytes],
                         [salt length],
                         kCCPRFHmacAlgSHA1,
                         rounds,
                         [derivedKey mutableBytes],
                         [derivedKey length]);
```

The initial computation can use calibrated rounds like this, but for verification, the number of rounds must equal the number used in the initial computation. Accordingly, you'd need to store the number of rounds originally used as well as the salt and the derived key, if you use a dynamic number of rounds.

**Symmetric Encryption**  
CommonCrypto provides a bewildering array of encryption algorithms and modes, and I'm not going to cover all of them. If you need to be compatible with an existing cryptosystem, that system should specify exaclty what algorithm and mode it uses. If you have a choice of algorithms, you probably want to use [AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) in [CBC](http://en.wikipedia.org/wiki/CBC_mode_of_operation#Cipher-block_chaining_.28CBC.29) mode with [PKCS7](http://en.wikipedia.org/wiki/Padding_(cryptography)#Padding_methods) padding. Note that, due to the padding, the output data may be slightly larger than the input.

The encryption functionality is located in `CommonCryptor.h`. It follows the same init/update/final pattern as the others, except that, the init function is called `Create` for whatever reason.

Unlike the other functionality, encryption is provided through something resembling actual objects called cryptors, rather than context structures. This means that, unlike the context structs used in the other CommonCrypto functions, you have to explicitly release a cryptor once you're done using it.

Create a cryptor using the `CCCryptorCreate` function. It takes a bunch of parameters:

- The operation to perform, either encryption or decryption.
- The encryption algorithm to use.
- Options, such as padding.
- The encryption key and length.
- The initialization vector.

Most of this should be pretty clear, but the initialization vector may be unfamiliar to you. It's insecure to use the same encryption key on more than one piece of data. The initialization vector is a random, non-private chunk of data that's basically used to randomize the enryption algorithm so that you can reuse the same key safely. When encrypting, you generate the initialization vector, then transmit it along with the encrypted data. When decrypting, you use the key, initialization vector, and encrypted data to recover the original data.

The only other tricky bit is getting the data out. All of the other functionality we've seen from CommonCrypto provides a fixed-sized output from variable-length input. The `Update` function simply takes data in, and then the `Final` function emits the result. Symmetric encryption generates data as you feed it in, so the `Update` function also produces data. Since the amount of data is not necessarily fixed, the `Update` function will tell the caller how much data it actually wrote, and a `CCCryptorGetOutputLength` function exists to figure out how large of a buffer should be provided.

Here's a quick example of encrypting some data using AES. Note that these functions can return errors, and real code must check for them rather than continuing forward blindly. This code omits error checking for brevity:

```
    NSData *data;
    NSData *key;
    NSData *initializationVector;

    CCCryptorRef cryptor;
    CCCryptorCreate(kCCEncrypt,
                    kCCAlgorithmAES128,
                    kCCOptionPKCS7Padding,
                    [key bytes],
                    [key length],
                    [initializationVector bytes],
                    &cryptor);

    size_t length = CCCryptorGetOutputLength(cryptor, [data length], true);
    NSMutableData *encryptedData = [NSMutableData dataWithLength: length];
    size_t updateLength;
    CCCryptorUpdate(cryptor,
                    [data bytes],
                    [data length],
                    [encryptedData mutableBytes],
                    [encryptedData length],
                    &updateLength);

    // Final may emit data, put it on the end
    char *finalDataPointer = (char *)[encryptedData mutableBytes] + updateLength;
    size_t remainingLength = [encryptedData length] - updateLength;
    size_t finalLength;
    CCCryptorFinal(cryptor,
                   finalDataPointer,
                   remainingLength,
                   &finalLength);

    // The amount of data emitted may have been less than
    // GetOutputLength said, so truncate
    [encryptedData setLength: updateLength + finalLength];

    CCCryptorRelease(cryptor);
```

If you're streaming data, or have multiple pieces of data to encrypt, you can call `CCCryptorUpdate` multiple times, calling `CCCryptorFinal` once at the end to finalize the output. You can stream the data produced by `CCCryptorUpdate` out to another destination, or simply accumulate it all into a buffer.

For cases where your input data is a single contiguous chunk and you want to accumulate the output data in memory, the `CCCrypt` function is a shortcut function which combines the functionality of `CCCryptorCreate`, `CCCryptorUpdate`, `CCCryptorFinal`, and `CCCryptorRelease` as used above.

**Conclusion**  
CommonCrypto is a convenient library provided with Mac OS X and iOS that provides a range of cryptographic primitives. It provides cryptographic hashes, message-authentication codes and key-derivation functions based on those hashes, and symmetric encryption. It's not a fully-featured cryptography library like [OpenSSL](http://www.openssl.org/), as it's missing more complex features such as public key cryptography and common protocols like [TLS](http://en.wikipedia.org/wiki/Transport_Layer_Security). However, if your needs fit within its capabilities, CommonCrypto is easy to use and requires no third-party code.

Cryptography is hard. This article is not intended as an introduction to cryptography in general or how to use it. If you plan to implement cryptography in a situation where a breach or failure could cause damage, please be sure to read up on the subject before diving in.

That's it for today. Come back next time for another cryptic Friday Q&A. Friday Q&A is driven by reader suggestions, so please keep [sending in your ideas](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
