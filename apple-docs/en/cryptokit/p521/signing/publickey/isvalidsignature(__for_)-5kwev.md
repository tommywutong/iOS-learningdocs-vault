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
doc_path: '/documentation/cryptokit/p521/signing/publickey/isvalidsignature(_:for:)-5kwev'
source_url: 'https://developer.apple.com/documentation/cryptokit/p521/signing/publickey/isvalidsignature(_:for:)-5kwev'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/p521/signing/publickey/isvalidsignature%28_%3Afor%3A%29-5kwev.json'
content_hash: 'sha256:ad78612e3dfcd1a4'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [P521](../../../p521.md) · [Signing](../../signing.md) · [PublicKey](../publickey.md)

# isValidSignature(_:for:)

<sub>Instance Method</sub>

Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-521 elliptic curve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidSignature<D>(_ signature: P521.Signing.ECDSASignature, for data: D) -> Bool where D : DataProtocol
```

## Parameters

- `signature` — The signature to verify.

- `data` — The signed data.

## Return Value

A Boolean value that’s `true` if the signature is valid for the given data; otherwise, `false`.

## See Also

### Verifying a signature

- [isValidSignature(_:for:)](<isvalidsignature(__for_)-dhjh.md>) — Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-521 elliptic curve.
- [ECDSASignature](../ecdsasignature.md) — A P-521 elliptic curve digital signature algorithm (ECDSA) signature.
