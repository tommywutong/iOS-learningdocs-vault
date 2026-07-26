---
title: rawRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa87/publickey/rawrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa87/publickey/rawrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa87/publickey/rawrepresentation.json'
content_hash: 'sha256:6530e6979a8f7c54'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA87](../../mldsa87.md) · [PublicKey](../publickey.md)

# rawRepresentation

<sub>Instance Property</sub>

A serialized representation of the public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawRepresentation: Data { get }
```

## Discussion

This property provides a representation of the public key in the FIPS 204 standard serialization format.
