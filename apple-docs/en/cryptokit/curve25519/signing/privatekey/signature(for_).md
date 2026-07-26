---
title: 'signature(for:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/curve25519/signing/privatekey/signature(for:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey/signature(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/curve25519/signing/privatekey/signature%28for%3A%29.json'
content_hash: 'sha256:5fe7e247286ebe20'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [Curve25519](../../../curve25519.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates an EdDSA signature over Curve25519.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

## Parameters

- `data` — The data to sign.

## Return Value

The signature for the data. Although not required by [RFC 8032](https://tools.ietf.org/html/rfc8032), which describes the Edwards-Curve Digital Signature Algorithm (EdDSA), the CryptoKit implementation of the algorithm employs randomization to generate a different signature on every call, even for the same data and key, to guard against side-channel attacks.
