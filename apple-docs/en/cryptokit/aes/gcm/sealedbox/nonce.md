---
title: nonce
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/gcm/sealedbox/nonce
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/nonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/sealedbox/nonce.json'
content_hash: 'sha256:6fa18957b76d60a4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [SealedBox](../sealedbox.md)

# nonce

<sub>Instance Property</sub>

The nonce used to encrypt the data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nonce: AES.GCM.Nonce { get }
```

## See Also

### Inspecting the component elements

- [ciphertext](ciphertext.md) — The encrypted data.
- [tag](tag.md) — An authentication tag.
