---
title: HPKE.AEAD.exportOnly
framework: Apple CryptoKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/aead/exportonly
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/aead/exportonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/aead/exportonly.json'
content_hash: 'sha256:cbd291034a7fe2f1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [AEAD](../aead.md)

# HPKE.AEAD.exportOnly

<sub>Case</sub>

An export-only mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case exportOnly
```

## Discussion

In export-only mode, HPKE negotiates key derivation, but you can’t use it to encrypt or decrypt data.
