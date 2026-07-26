---
title: 'isValidSignature(_:for:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/curve25519/signing/publickey/isvalidsignature(_:for:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey/isvalidsignature(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing/publickey/isvalidsignature%28_%3Afor%3A%29.json'
content_hash: 'sha256:6acc6c3a9943f655'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [Curve25519](../../../curve25519.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# isValidSignature(_:for:)

<sub>Instance Method</sub>

Verifies an EdDSA signature over Curve25519.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidSignature<S, D>(_ signature: S, for data: D) -> Bool where S : DataProtocol, D : DataProtocol
```

## Parameters

- `signature` — The signature to check against the given data.

- `data` — The data covered by the signature.

## Return Value

A Boolean value that’s `true` when the signature is valid for the given data.
