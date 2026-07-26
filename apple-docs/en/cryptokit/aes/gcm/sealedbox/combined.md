---
title: combined
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/gcm/sealedbox/combined
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/combined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/sealedbox/combined.json'
content_hash: 'sha256:de766d616ccca4a4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [SealedBox](../sealedbox.md)

# combined

<sub>Instance Property</sub>

A combined element composed of the nonce, encrypted data, and authentication tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var combined: Data? { get }
```

## Discussion

The combined representation is only available when the [Nonce](../nonce.md) size is the default size of 12 bytes. The data layout of the combined representation is nonce, ciphertext, then tag.
