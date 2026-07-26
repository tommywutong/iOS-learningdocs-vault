---
title: HMAC
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hmac
source_url: 'https://developer.apple.com/documentation/cryptokit/hmac'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hmac.json'
content_hash: 'sha256:2bcb14676c3c1a0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HMAC

<sub>Structure</sub>

A hash-based message authentication algorithm.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HMAC<H> where H : HashFunction
```

## Overview

Use hash-based message authentication to create a code with a value that’s dependent on both a block of data and a symmetric cryptographic key. Another party with access to the data and the same secret key can compute the code again and compare it to the original to detect whether the data changed. This serves a purpose similar to digital signing and verification, but depends on a shared symmetric key instead of public-key cryptography.

As with digital signing, the data isn’t hidden by this process. When you need to encrypt the data as well as authenticate it, use a cipher like [AES](aes.md) or [ChaChaPoly](chachapoly.md) to put the data into a sealed box (an instance of [SealedBox](aes/gcm/sealedbox.md) or [SealedBox](chachapoly/sealedbox.md)).

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting a key

- [Key](hmac/key.md) — An alias for the symmetric key type used to compute or verify a message authentication code.
- [SymmetricKey](symmetrickey.md) — A symmetric cryptographic key.

### Working with codes

- [MAC](hmac/mac.md) — An alias for a hash-based message authentication code.
- [HashedAuthenticationCode](hashedauthenticationcode.md) — A hash-based message authentication code.
- [MessageAuthenticationCode](messageauthenticationcode.md) — A type that represents a message authentication code.

### Creating an authentication code iteratively

- [init(key:)](<hmac/init(key_).md>) — Creates a message authentication code generator.
- [update(data:)](<hmac/update(data_).md>) — Updates the message authentication code computation with a block of data.
- [finalize()](<hmac/finalize().md>) — Finalizes the message authentication computation and returns the computed code.

### Checking an authentication code

- [isValidAuthenticationCode(_:authenticating:using:)](<hmac/isvalidauthenticationcode(__authenticating_using_)-8ezmw.md>) — Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.
- [isValidAuthenticationCode(_:authenticating:using:)](<hmac/isvalidauthenticationcode(__authenticating_using_)-5jbc8.md>) — Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.
- [isValidAuthenticationCode(_:authenticating:using:)](<hmac/isvalidauthenticationcode(__authenticating_using_)-5ilt9.md>) — Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.

### Instance Methods

- [update(bytes:)](<hmac/update(bytes_).md>) _(beta)_

### Type Methods

- [authenticationCode(for:using:)](<hmac/authenticationcode(for_using_)-737ab.md>) — Computes a message authentication code for the given data.
- [authenticationCode(for:using:)](<hmac/authenticationcode(for_using_)-heea.md>) — Computes a message authentication code for the given data. _(beta)_

## See Also

### Message authentication codes

- [SymmetricKey](symmetrickey.md) — A symmetric cryptographic key.
- [SymmetricKeySize](symmetrickeysize.md) — The sizes that a symmetric cryptographic key can take.
