---
title: publicKey
framework: Apple CryptoKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem1024/privatekey/publickey
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/publickey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/privatekey/publickey.json'
content_hash: 'sha256:1188fa2063eefc11'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM1024](../../mlkem1024.md) · [PrivateKey](../privatekey.md)

# publicKey

<sub>Instance Property</sub>

The corresponding public key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var publicKey: MLKEM1024.PublicKey { get }
```

## See Also

### Inspecting a private key’s properties

- [integrityCheckedRepresentation](integritycheckedrepresentation.md) — An integrity-checked representation of the private key.
- [seedRepresentation](seedrepresentation.md) — The private key’s seed representation.
