---
title: 'extract(inputKeyMaterial:salt:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:)-7qmzj'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:)-7qmzj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/extract%28inputkeymaterial%3Asalt%3A%29-7qmzj.json'
content_hash: 'sha256:0d5980e1f854070f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# extract(inputKeyMaterial:salt:)

<sub>Type Method</sub>

Creates cryptographically strong key material from a main key or passcode that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func extract(inputKeyMaterial: SymmetricKey, salt: RawSpan?) -> HashedAuthenticationCode<H>
```

## Parameters

- `inputKeyMaterial` — The main key or passcode the derivation function uses to derive a key.

- `salt` — The salt to use for key derivation.

## Return Value

A pseudorandom, cryptographically strong key in the form of a hashed authentication code.

## Discussion

Generate a derived symmetric key from the cryptographically strong key material this function creates by calling [expand(pseudoRandomKey:info:outputByteCount:)](<expand(pseudorandomkey_info_outputbytecount_).md>).
