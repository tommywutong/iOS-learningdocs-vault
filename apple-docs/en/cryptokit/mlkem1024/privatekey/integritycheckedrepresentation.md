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
doc_path: /documentation/cryptokit/mlkem1024/privatekey/integritycheckedrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/integritycheckedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/privatekey/integritycheckedrepresentation.json'
content_hash: 'sha256:8a8ee36825e4c1af'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM1024](../../mlkem1024.md) · [PrivateKey](../privatekey.md)

# integrityCheckedRepresentation

<sub>Instance Property</sub>

An integrity-checked representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var integrityCheckedRepresentation: Data { get }
```

## Discussion

This representation includes the seed value, and a hash of the corresponding public key.

## See Also

### Inspecting a private key’s properties

- [publicKey](publickey.md) — The corresponding public key.
- [seedRepresentation](seedrepresentation.md) — The private key’s seed representation.
