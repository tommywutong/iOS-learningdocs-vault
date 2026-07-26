---
title: 'isValidSignature(_:for:context:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mldsa87/publickey/isvalidsignature(_:for:context:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa87/publickey/isvalidsignature(_:for:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa87/publickey/isvalidsignature%28_%3Afor%3Acontext%3A%29.json'
content_hash: 'sha256:c20addba89452ce0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA87](../../mldsa87.md) · [PublicKey](../publickey.md)

# isValidSignature(_:for:context:)

<sub>Instance Method</sub>

Verifies a MLDSA87 signature, in a specific context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isValidSignature<S, D, C>(_ signature: S, for data: D, context: C) -> Bool where S : DataProtocol, D : DataProtocol, C : DataProtocol
```

## Parameters

- `signature` — The MLDSA87 signature to verify.

- `data` — The signed data.

- `context` — Context for the signature.

## Return Value

`true` if the signature is valid in the specified context, `false` otherwise.
