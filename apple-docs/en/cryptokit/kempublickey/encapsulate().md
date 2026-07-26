---
title: encapsulate()
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kempublickey/encapsulate()
source_url: 'https://developer.apple.com/documentation/cryptokit/kempublickey/encapsulate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kempublickey/encapsulate%28%29.json'
content_hash: 'sha256:5ff70e7ea178e115'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEMPublicKey](../kempublickey.md)

# encapsulate()

<sub>Instance Method</sub>

Generates and encapsulates a shared secret.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encapsulate() throws -> KEM.EncapsulationResult
```

## Return Value

The shared secret, and its encapsulated version.

## Discussion

Share the encapsulated secret with the person who has the [KEMPrivateKey](../kemprivatekey.md). They use [decapsulate(_:)](<../kemprivatekey/decapsulate(__).md>) to recover the shared secret.
