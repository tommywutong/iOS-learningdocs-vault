---
title: 'signature(for:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mldsa87/privatekey/signature(for:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/signature(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa87/privatekey/signature%28for%3A%29.json'
content_hash: 'sha256:ee97af917542bc6d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA87](../../mldsa87.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates a MLDSA87 signature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

## Parameters

- `data` — The data to sign.

## Return Value

The MLDSA87 signature. This method throws if CryptoKit encounters an error producing the signature.

## See Also

### Signing data

- [signature(for:context:)](<signature(for_context_).md>) — Generates a MLDSA87 signature, with context.
