---
title: Apple CryptoKit
framework: Apple CryptoKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 15.0+, macOS 10.15+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit
source_url: 'https://developer.apple.com/documentation/cryptokit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit.json'
content_hash: 'sha256:4a821129cdd6f6cb'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Apple CryptoKit

<sub>Framework</sub>

Perform cryptographic operations securely and efficiently.

## Overview

Use Apple CryptoKit to perform common cryptographic operations:

- Compute and compare cryptographically secure digests.
- Use public-key cryptography to create and evaluate digital signatures, and to perform key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave.
- Generate symmetric keys, and use them in operations like message authentication and encryption.

Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.

## Topics

### Essentials

- [Complying with Encryption Export Regulations](security/complying-with-encryption-export-regulations.md) — Declare the use of encryption in your app to streamline the app submission process.
- [Performing Common Cryptographic Operations](cryptokit/performing-common-cryptographic-operations.md) — Use CryptoKit to carry out operations like hashing, key generation, and encryption.
- [Storing CryptoKit Keys in the Keychain](cryptokit/storing-cryptokit-keys-in-the-keychain.md) — Convert between strongly typed cryptographic keys and native keychain types.
- [Enhancing your app’s privacy and security with quantum-secure workflows](cryptokit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows.md) — Use quantum-secure cryptography to protect your app from quantum attacks.

### Cryptographically secure hashes

- [HashFunction](cryptokit/hashfunction.md) — A type that performs cryptographically secure hashing.
- [SHA512](cryptokit/sha512.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.
- [SHA384](cryptokit/sha384.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- [SHA256](cryptokit/sha256.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.

### Message authentication codes

- [HMAC](cryptokit/hmac.md) — A hash-based message authentication algorithm.
- [SymmetricKey](cryptokit/symmetrickey.md) — A symmetric cryptographic key.
- [SymmetricKeySize](cryptokit/symmetrickeysize.md) — The sizes that a symmetric cryptographic key can take.

### Ciphers

- [AES](cryptokit/aes.md) — A container for Advanced Encryption Standard (AES) ciphers.
- [ChaChaPoly](cryptokit/chachapoly.md) — An implementation of the ChaCha20-Poly1305 cipher.

### Public key cryptography

- [Curve25519](cryptokit/curve25519.md) — An elliptic curve that enables X25519 key agreement and Ed25519 signatures.
- [P521](cryptokit/p521.md) — An elliptic curve that enables NIST P-521 signatures and key agreement.
- [P384](cryptokit/p384.md) — An elliptic curve that enables NIST P-384 signatures and key agreement.
- [P256](cryptokit/p256.md) — An elliptic curve that enables NIST P-256 signatures and key agreement.
- [SharedSecret](cryptokit/sharedsecret.md) — A key agreement result from which you can derive a symmetric cryptographic key.
- [SecureEnclave](cryptokit/secureenclave.md) — A representation of a device’s hardware-based key manager.
- [HPKE](cryptokit/hpke.md) — A container for hybrid public key encryption (HPKE) operations.

### Key derivation functions

- [HKDF](cryptokit/hkdf.md) — A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).

### Key encapsulation mechanisms (KEM)

- [KEM](cryptokit/kem.md) — A key encapsulation mechanism.
- [MLKEM768](cryptokit/mlkem768.md) — The Module-Lattice key encapsulation mechanism (KEM).
- [MLKEM1024](cryptokit/mlkem1024.md) — The Module-Lattice key encapsulation mechanism (KEM).
- [XWingMLKEM768X25519](cryptokit/xwingmlkem768x25519.md) — The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06

### KEM keys

- [KEMPrivateKey](cryptokit/kemprivatekey.md) — The private key for a key encapsulation mechanism.
- [KEMPublicKey](cryptokit/kempublickey.md) — The public key for a key encapsulation mechanism.

### Errors

- [CryptoKitError](cryptokit/cryptokiterror.md) — General cryptography errors used by CryptoKit.
- [CryptoKitASN1Error](cryptokit/cryptokitasn1error.md) — Errors from decoding ASN.1 content.

### Legacy algorithms

- [Insecure](cryptokit/insecure.md) — A container for older, cryptographically insecure algorithms.

### Protocols

- [DiffieHellmanKeyAgreement](cryptokit/diffiehellmankeyagreement.md) — A Diffie-Hellman Key Agreement Key
- [HPKEDiffieHellmanPrivateKey](cryptokit/hpkediffiehellmanprivatekey.md) — A type that represents the private key in a Diffie-Hellman key exchange.
- [HPKEDiffieHellmanPrivateKeyGeneration](cryptokit/hpkediffiehellmanprivatekeygeneration.md) — A type that represents the generation of private keys in a Diffie-Hellman key exchange.
- [HPKEDiffieHellmanPublicKey](cryptokit/hpkediffiehellmanpublickey.md) — A type that represents the public key in a Diffie-Hellman key exchange.
- [HPKEKEMPrivateKey](cryptokit/hpkekemprivatekey.md) — A type that represents the private key in HPKE.
- [HPKEKEMPrivateKeyGeneration](cryptokit/hpkekemprivatekeygeneration.md) — A type that represents the generation of private keys in HPKE
- [HPKEKEMPublicKey](cryptokit/hpkekempublickey.md) — A type that represents the public key in HPKE
- [HPKEPublicKeySerialization](cryptokit/hpkepublickeyserialization.md) — A type that [HPKE](cryptokit/hpke.md) uses to encode the public key.
- [KEMOneTimePrivateKey](cryptokit/kemonetimeprivatekey.md) — A one-time private key for a key encapsulation mechanism, which can only decapsulate once but it does so faster. _(beta)_

### Structures

- [CorecryptoCurveType](cryptokit/corecryptocurvetype.md)
- [SHA3_256](cryptokit/sha3_256.md) — An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 256-bit digest.
- [SHA3_256Digest](cryptokit/sha3_256digest.md) — The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 256-bit digest.
- [SHA3_384](cryptokit/sha3_384.md) — An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 384-bit digest.
- [SHA3_384Digest](cryptokit/sha3_384digest.md) — The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 384-bit digest.
- [SHA3_512](cryptokit/sha3_512.md) — An implementation of Secure Hashing Algorithm 3 (SHA-3) hashing with a 512-bit digest.
- [SHA3_512Digest](cryptokit/sha3_512digest.md) — The output of a Secure Hashing Algorithm 3 (SHA-2) hash with a 512-bit digest.

### Type Aliases

- [CryptoKitMetaError](cryptokit/cryptokitmetaerror.md)
- [SHA2_256](cryptokit/sha2_256.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 256-bit digest.
- [SHA2_384](cryptokit/sha2_384.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 384-bit digest.
- [SHA2_512](cryptokit/sha2_512.md) — An implementation of Secure Hashing Algorithm 2 (SHA-2) hashing with a 512-bit digest.

### Enumerations

- [MLDSA65](cryptokit/mldsa65.md) — The MLDSA65 Digital Signature Algorithm
- [MLDSA87](cryptokit/mldsa87.md) — The MLDSA87 Digital Signature Algorithm
