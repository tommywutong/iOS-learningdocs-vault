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
doc_path: '/documentation/cryptokit/mlkem1024/publickey/init(rawrepresentation:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem1024/publickey/init(rawrepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem1024/publickey/init%28rawrepresentation%3A%29.json'
content_hash: 'sha256:7a53b7be5436064c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [MLKEM1024](../../mlkem1024.md) · [PublicKey](../publickey.md)

# init(rawRepresentation:)

<sub>Initializer</sub>

Initializes a public key from a raw representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<D>(rawRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `rawRepresentation` — Data that represents the public key.
