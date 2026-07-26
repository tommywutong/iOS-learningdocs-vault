---
title: 'signature(for:context:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature(for:context:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature(for:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/secureenclave/mldsa65/privatekey/signature%28for%3Acontext%3A%29.json'
content_hash: 'sha256:279e984348cf5d86'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [SecureEnclave](../../../secureenclave.md) · [MLDSA65](../../mldsa65.md) · [PrivateKey](../privatekey.md)

# signature(for:context:)

<sub>Instance Method</sub>

Generates a MLDSA65 signature, with context

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func signature<D, C>(for data: D, context: C) throws -> Data where D : DataProtocol, C : DataProtocol
```

## Parameters

- `data` — The data to sign

- `context` — Context for the signature

## Return Value

The MLDSA65 signature

## Discussion

> [!danger] Throws
> If there is a failure producing the signature
