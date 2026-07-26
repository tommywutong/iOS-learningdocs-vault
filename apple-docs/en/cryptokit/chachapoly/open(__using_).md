---
title: 'open(_:using:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/chachapoly/open(_:using:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/chachapoly/open(_:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/chachapoly/open%28_%3Ausing%3A%29.json'
content_hash: 'sha256:ccd5cc6666eabe2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [ChaChaPoly](../chachapoly.md)

# open(_:using:)

<sub>Type Method</sub>

Decrypts the message and verifies its authenticity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func open(_ sealedBox: ChaChaPoly.SealedBox, using key: SymmetricKey) throws -> Data
```

## Parameters

- `sealedBox` — The sealed box to open.

- `key` — The cryptographic key that was used to seal the message.

## Return Value

The original plaintext message that was sealed in the box, as long as the correct key is used and authentication succeeds. The call throws an error if decryption or authentication fail.

## See Also

### Decrypting and verifying the message

- [open(_:using:authenticating:)](<open(__using_authenticating_).md>) — Decrypts the message and verifies the authenticity of both the encrypted message and additional data.
