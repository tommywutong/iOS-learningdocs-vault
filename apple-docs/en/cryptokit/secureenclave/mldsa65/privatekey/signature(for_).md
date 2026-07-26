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
doc_path: '/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature(for:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature%28for%3A%29.json'
content_hash: 'sha256:eb406e8d25465894'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# signature(for:)

<sub>Instance Method</sub>

Generates a MLDSA65 signature

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D>(for data: D) throws -> Data where D : DataProtocol
```

## Parameters

- `data` — The data to sign

## Return Value

The MLDSA65 signature

## Discussion

> [!danger] Throws
> If there is a failure producing the signature
