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
doc_path: /documentation/cryptokit/mlkem768/privatekey/seedrepresentation
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/seedrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768/privatekey/seedrepresentation.json'
content_hash: 'sha256:cead243510465e91'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM768](../../mlkem768.md) · [PrivateKey](../privatekey.md)

# seedRepresentation

<sub>Instance Property</sub>

The private key’s seed representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var seedRepresentation: Data { get }
```

## Discussion

The seed is `d||z`, as specified in the algorithm `ML-KEM.KeyGen_internal(d,z)` (Algorithm 16) of FIPS 203.

## See Also

### Inspecting a private key’s properties

- [integrityCheckedRepresentation](integritycheckedrepresentation.md) — An integrity-checked representation of the private key.
- [publicKey](publickey.md) — The corresponding public key.
