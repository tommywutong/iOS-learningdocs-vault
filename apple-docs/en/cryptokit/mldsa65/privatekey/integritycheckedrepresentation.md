---
title: integrityCheckedRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa65/privatekey/integritycheckedrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/integritycheckedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/privatekey/integritycheckedrepresentation.json'
content_hash: 'sha256:361fa44cc1e7be20'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# integrityCheckedRepresentation

<sub>Instance Property</sub>

The integrity-checked data representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var integrityCheckedRepresentation: Data { get }
```

## Discussion

This representation is 64 bytes long, and contains the seed and a hash of the public key.

## See Also

### Inspecting a private key’s properties

- [publicKey](publickey.md) — The associated public key.
- [seedRepresentation](seedrepresentation.md) — The seed representation of the private key.
