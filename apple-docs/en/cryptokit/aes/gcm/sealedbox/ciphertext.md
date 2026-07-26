---
title: ciphertext
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/gcm/sealedbox/ciphertext
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/ciphertext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/sealedbox/ciphertext.json'
content_hash: 'sha256:d92cf2b4eb3981ad'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [SealedBox](../sealedbox.md)

# ciphertext

<sub>Instance Property</sub>

The encrypted data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ciphertext: Data { get }
```

## Discussion

The length of the ciphertext of a sealed box is the same as the length of the plaintext you encrypt.

## See Also

### Inspecting the component elements

- [nonce](nonce.md) — The nonce used to encrypt the data.
- [tag](tag.md) — An authentication tag.
