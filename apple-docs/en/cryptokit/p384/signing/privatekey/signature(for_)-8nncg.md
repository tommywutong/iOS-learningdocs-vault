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
doc_path: '/documentation/cryptokit/p384/signing/privatekey/signature(for:)-8nncg'
source_url: 'https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/signature(for:)-8nncg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p384/signing/privatekey/signature%28for%3A%29-8nncg.json'
content_hash: 'sha256:56446d80bb2f1873'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P384](../../../p384.md) · [Signing](../../signing.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-384 elliptic curve, using SHA-384 as the hash function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for data: D) throws -> P384.Signing.ECDSASignature where D : DataProtocol
```

## Parameters

- `data` — The data to sign.

## Return Value

The signature corresponding to the data. The signing algorithm employs randomization to generate a different signature on every call, even for the same data and key.

## See Also

### Creating a signature

- [signature(for:)](<signature(for_)-wrsj.md>) — Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-384 elliptic curve.
- [ECDSASignature](../ecdsasignature.md) — A P-384 elliptic curve digital signature algorithm (ECDSA) signature.
