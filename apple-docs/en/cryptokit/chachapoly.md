---
title: ChaChaPoly
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/chachapoly
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly.json'
content_hash: 'sha256:d6c89c0c6e4457fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# ChaChaPoly

<sub>Enumeration</sub>

An implementation of the ChaCha20-Poly1305 cipher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ChaChaPoly
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Storing the output

- [SealedBox](chachapoly/sealedbox.md) — A secure container for your data that you access using a cipher.

### Getting a nonce

- [Nonce](chachapoly/nonce.md) — A value used once during a cryptographic operation and then discarded.

### Securing the plaintext message

- [seal(_:using:nonce:)](<chachapoly/seal(__using_nonce_).md>) — Secures the given plaintext message with encryption and an authentication tag.
- [seal(_:using:nonce:authenticating:)](<chachapoly/seal(__using_nonce_authenticating_).md>) — Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.

### Decrypting and verifying the message

- [open(_:using:)](<chachapoly/open(__using_).md>) — Decrypts the message and verifies its authenticity.
- [open(_:using:authenticating:)](<chachapoly/open(__using_authenticating_).md>) — Decrypts the message and verifies the authenticity of both the encrypted message and additional data.

### Type Methods

- [open(inPlace:using:nonce:authenticating:tag:)](<chachapoly/open(inplace_using_nonce_authenticating_tag_).md>) — Decrypts the message and verifies the authenticity of both the encrypted message and additional data. _(beta)_
- [seal(inPlace:using:nonce:authenticating:tag:)](<chachapoly/seal(inplace_using_nonce_authenticating_tag_).md>) — Secures the given plaintext message in place with encryption and an authentication tag. _(beta)_

## See Also

### Ciphers

- [AES](aes.md) — A container for Advanced Encryption Standard (AES) ciphers.
