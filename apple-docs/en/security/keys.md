---
title: Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keys
source_url: 'https://developer.apple.com/documentation/security/keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keys.json'
content_hash: 'sha256:0d4fb9fd95b94ed0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)

# Keys

<sub>API Collection</sub>

Generate, store, and use cryptographic keys.

## Overview

Cryptographic keys are strings of bytes that you combine with other data in specialized mathematical operations to enhance security. At the lowest level, this usually means participating in either encryption and decryption or digital signing and verification. You can use these basic operations directly, such as when you encrypt data before sending it through an insecure channel. You also use them implicitly, such as when you verify the digital signature on a certificate as a byproduct of a trust evaluation.

Keys vary based on the operations they support. For example, you use public and private key pairs to perform asymmetric encryption, whereas you use symmetric keys to conduct symmetric encryption. Similarly, one key might work for a 1024-bit RSA algorithm, while another might be suitable for a 256-bit elliptic curve algorithm. Use the functions in this section when you need to handle cryptographic keys.

## Topics

### Essentials

- [Getting an Existing Key](getting-an-existing-key.md) — Learn how to obtain an existing cryptographic key.
- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md) — Store and access cryptographic keys in the keychain.
- [SecKey](seckey.md) — An object that represents a cryptographic key.
- [SecKeyGetTypeID](<seckeygettypeid().md>) — Returns the unique identifier of the opaque type to which a key object belongs.

### Key Generation

- [Generating New Cryptographic Keys](generating-new-cryptographic-keys.md) — Create both asymmetric and symmetric cryptographic keys.
- [Protecting keys with the Secure Enclave](protecting-keys-with-the-secure-enclave.md) — Create an extra layer of security for your private keys.
- [SecKeyCreateRandomKey](<seckeycreaterandomkey(____).md>) — Generates a new public-private key pair.
- [SecKeyCopyPublicKey](<seckeycopypublickey(__).md>) — Gets the public key associated with the given private key.
- [Key Generation Attributes](key-generation-attributes.md) — Use attribute dictionary keys during cryptographic key generation.

### Examining Keys

- [SecKeyIsAlgorithmSupported](<seckeyisalgorithmsupported(______).md>) — Returns a Boolean indicating whether a key is suitable for an operation using a certain algorithm.
- [SecKeyGetBlockSize](<seckeygetblocksize(__).md>) — Gets the block length associated with a cryptographic key.
- [SecKeyCopyAttributes](<seckeycopyattributes(__).md>) — Gets the attributes of a given key.
- [SecKeyAlgorithm](seckeyalgorithm.md) — The algorithms that cryptographic keys enable.
- [SecKeyOperationType](seckeyoperationtype.md) — The types of operations that you can use a cryptographic key to perform.

### Import and Export

- [Storing Keys as Data](storing-keys-as-data.md) — Create an external representation of a key for transmission.
- [SecKeyCopyExternalRepresentation](<seckeycopyexternalrepresentation(____).md>) — Returns an external representation of the given key suitable for the key’s type.
- [SecKeyCreateWithData](<seckeycreatewithdata(______).md>) — Restores a key from an external representation of that key.

### Key Exchange

- [SecKeyCopyKeyExchangeResult](<seckeycopykeyexchangeresult(__________).md>) — Performs the Diffie-Hellman style of key exchange with optional key-derivation steps.
- [SecKeyKeyExchangeParameter](seckeykeyexchangeparameter.md) — The dictionary keys used to specify Diffie-Hellman key exchange parameters.

### Encryption

- [Using Keys for Encryption](using-keys-for-encryption.md) — Perform asymmetric and symmetric encryption and decryption using cryptographic keys.
- [SecKeyCreateEncryptedData](<seckeycreateencrypteddata(________).md>) — Encrypts a block of data using a public key and specified algorithm.
- [SecKeyCreateDecryptedData](<seckeycreatedecrypteddata(________).md>) — Decrypts a block of data using a private key and specified algorithm.

### Digital Signatures

- [Signing and Verifying](signing-and-verifying.md) — Create and evaluate digital signatures to establish the validity of code or data.
- [SecKeyCreateSignature](<seckeycreatesignature(________).md>) — Creates the cryptographic signature for a block of data using a private key and specified algorithm.
- [SecKeyVerifySignature](<seckeyverifysignature(__________).md>) — Verifies the cryptographic signature of a block of data using a public key and specified algorithm.

### Legacy iOS Key Operations

- [SecKeyGeneratePair](<seckeygeneratepair(______).md>) — Creates an asymmetric key pair. _(deprecated)_
- [SecKeyEncrypt](<seckeyencrypt(____________).md>) — Encrypts a block of plaintext. _(deprecated)_
- [SecKeyDecrypt](<seckeydecrypt(____________).md>) — Decrypts a block of ciphertext. _(deprecated)_
- [SecKeyRawSign](<seckeyrawsign(____________).md>) — Generates a digital signature for a block of data. _(deprecated)_
- [SecKeyRawVerify](<seckeyrawverify(____________).md>) — Verifies a digital signature. _(deprecated)_
- [SecPadding](secpadding.md) — The types of padding to use when you create or verify a digital signature. _(deprecated)_

### Legacy macOS Key Operations

- [SecKeyGeneratePairAsync](<seckeygeneratepairasync(______).md>) — Generates a public/private key pair. _(deprecated)_
- [SecKeyGenerateSymmetric](<seckeygeneratesymmetric(____).md>) — Generates a random symmetric key. _(deprecated)_
- [SecKeyCreateFromData](<seckeycreatefromdata(______).md>) — Constructs a SecKeyRef object for a symmetric key. _(deprecated)_
- [SecKeyDeriveFromPassword](<seckeyderivefrompassword(______).md>) — Returns a key object in which the key data is derived from a password. _(deprecated)_
- [SecKeyWrapSymmetric](<seckeywrapsymmetric(________).md>) — Wraps a symmetric key with another key. _(deprecated)_
- [SecKeyUnwrapSymmetric](<seckeyunwrapsymmetric(________).md>) — Unwraps a wrapped symmetric key. _(deprecated)_
- [SecKeySizes](seckeysizes.md) — The supported sizes for keys of various common types. _(deprecated)_
- [SecKeyUsage](seckeyusage.md) — The flags that indicate key usage in the `KeyUsage` extension of a certificate.
- [SecPublicKeyHash](secpublickeyhash.md) — A container for a 20-byte public key hash.
- [SecKeyGeneratePairBlock](seckeygeneratepairblock.md) — A block called with the results of a call to [SecKeyGeneratePairAsync](<seckeygeneratepairasync(______).md>).
- [SecCredentialType](seccredentialtype.md) — The credential type to be returned by [SecKeyGetCredentials](seckeygetcredentials.md). _(deprecated)_
