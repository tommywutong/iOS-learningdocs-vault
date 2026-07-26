---
title: 'seal(_:using:nonce:authenticating:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/seal(_:using:nonce:authenticating:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/seal(_:using:nonce:authenticating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/seal%28_%3Ausing%3Anonce%3Aauthenticating%3A%29.json'
content_hash: 'sha256:8289f205af4b762d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [GCM](../gcm.md)

# seal(_:using:nonce:authenticating:)

<sub>Type Method</sub>

Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func seal<Plaintext, AuthenticatedData>(_ message: Plaintext, using key: SymmetricKey, nonce: AES.GCM.Nonce? = nil, authenticating authenticatedData: AuthenticatedData) throws -> AES.GCM.SealedBox where Plaintext : DataProtocol, AuthenticatedData : DataProtocol
```

## Parameters

- `message` — The plaintext data to seal.

- `key` — A cryptographic key used to seal the message.

- `nonce` — The nonce the sealing process requires. If you don’t provide a nonce, the method generates a random one by invoking [init()](<nonce/init().md>).

- `authenticatedData` — Additional data to be authenticated.

## Return Value

The sealed message.

## See Also

### Securing the plaintext message

- [seal(_:using:nonce:)](<seal(__using_nonce_).md>) — Secures the given plaintext message with encryption and an authentication tag.
