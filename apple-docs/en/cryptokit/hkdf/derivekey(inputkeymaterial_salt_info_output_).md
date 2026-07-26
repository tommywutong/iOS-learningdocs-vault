---
title: 'deriveKey(inputKeyMaterial:salt:info:output:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:salt:info:output:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:salt:info:output:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/derivekey%28inputkeymaterial%3Asalt%3Ainfo%3Aoutput%3A%29.json'
content_hash: 'sha256:70494db84c3a4c28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# deriveKey(inputKeyMaterial:salt:info:output:)

<sub>Type Method</sub>

Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func deriveKey(inputKeyMaterial: SymmetricKey, salt: RawSpan? = nil, info: RawSpan? = nil, output outputKey: inout OutputRawSpan)
```

## Parameters

- `inputKeyMaterial` — The main key or passcode the derivation function uses to derive a key.

- `salt` — The salt to use for key derivation.

- `info` — The shared information to use for key derivation.

- `outputKey` — An output span that will be populated with the derived symmetric key.
