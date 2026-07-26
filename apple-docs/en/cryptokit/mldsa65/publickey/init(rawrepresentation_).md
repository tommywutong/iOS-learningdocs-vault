---
title: 'init(rawRepresentation:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/mldsa65/publickey/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mldsa65/publickey/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mldsa65/publickey/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:0388557be062b7e6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLDSA65](../../mldsa65.md) · [PublicKey](../publickey.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Parses a public key from a serialized representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(rawRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `rawRepresentation` — The public key, in the FIPS 204 standard serialization format.

## Return Value

The deserialized public key.
