---
title: AES.GCM
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/gcm
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm.json'
content_hash: 'sha256:e23556700268747c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [AES](../aes.md)

# AES.GCM

<sub>Enumeration</sub>

The Advanced Encryption Standard (AES) Galois Counter Mode (GCM) cipher suite.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum GCM
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Storing the output

- [SealedBox](gcm/sealedbox.md) — A secure container for your data that you can access using a cipher.

### Getting a nonce

- [Nonce](gcm/nonce.md) — A value used once during a cryptographic operation and then discarded.

### Securing the plaintext message

- [seal(_:using:nonce:)](<gcm/seal(__using_nonce_).md>) — Secures the given plaintext message with encryption and an authentication tag.
- [seal(_:using:nonce:authenticating:)](<gcm/seal(__using_nonce_authenticating_).md>) — Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.

### Decrypting and verifying the message

- [open(_:using:)](<gcm/open(__using_).md>) — Decrypts the message and verifies its authenticity.
- [open(_:using:authenticating:)](<gcm/open(__using_authenticating_).md>) — Decrypts the message and verifies the authenticity of both the encrypted message and additional data.

### Type Methods

- [open(inPlace:using:nonce:authenticating:tag:)](<gcm/open(inplace_using_nonce_authenticating_tag_).md>) — Decrypts the message and verifies its authenticity. _(beta)_
- [seal(inPlace:using:nonce:authenticating:tag:)](<gcm/seal(inplace_using_nonce_authenticating_tag_).md>) — Secures the given plaintext message with encryption and an optional authentication tag. _(beta)_
