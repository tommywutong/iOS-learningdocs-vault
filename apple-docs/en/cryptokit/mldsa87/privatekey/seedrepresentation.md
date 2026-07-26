---
title: seedRepresentation
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mldsa87/privatekey/seedrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/seedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa87/privatekey/seedrepresentation.json'
content_hash: 'sha256:6587e61ae892d30b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA87](../../mldsa87.md) · [PrivateKey](../privatekey.md)

# seedRepresentation

<sub>Instance Property</sub>

The seed representation of the private key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var seedRepresentation: Data { get }
```

## Discussion

The seed representation is 32 bytes long, and is the parameter for the `ML-DSA.KeyGen_internal` algorithm (Algorithm 16) of FIPS 204.

## See Also

### Inspecting a private key’s properties

- [integrityCheckedRepresentation](integritycheckedrepresentation.md) — The integrity-checked data representation of the private key.
- [publicKey](publickey.md) — The associated public key.
