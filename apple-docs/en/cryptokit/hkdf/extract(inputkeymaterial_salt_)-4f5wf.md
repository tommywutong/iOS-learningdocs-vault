---
title: 'extract(inputKeyMaterial:salt:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:)-4f5wf'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/extract(inputkeymaterial:salt:)-4f5wf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/extract%28inputkeymaterial%3Asalt%3A%29-4f5wf.json'
content_hash: 'sha256:59b4101c6537cdc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# extract(inputKeyMaterial:salt:)

<sub>Type Method</sub>

Creates cryptographically strong key material from a main key or passcode that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func extract<Salt>(inputKeyMaterial: SymmetricKey, salt: Salt?) -> HashedAuthenticationCode<H> where Salt : DataProtocol
```

## Parameters

- `inputKeyMaterial` — The main key or passcode the derivation function uses to derive a key.

- `salt` — The salt to use for key derivation.

## Return Value

A pseudorandom, cryptographically strong key in the form of a hashed authentication code.

## Discussion

Generate a derived symmetric key from the cryptographically strong key material this function creates by calling [expand(pseudoRandomKey:info:outputByteCount:)](<expand(pseudorandomkey_info_outputbytecount_).md>).
