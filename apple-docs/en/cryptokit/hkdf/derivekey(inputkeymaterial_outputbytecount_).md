---
title: 'deriveKey(inputKeyMaterial:outputByteCount:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:outputbytecount:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf/derivekey(inputkeymaterial:outputbytecount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf/derivekey%28inputkeymaterial%3Aoutputbytecount%3A%29.json'
content_hash: 'sha256:d8d5c462d25b4a20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HKDF](../hkdf.md)

# deriveKey(inputKeyMaterial:outputByteCount:)

<sub>Type Method</sub>

Derives a symmetric encryption key from a main key or passcode using HKDF key derivation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func deriveKey(inputKeyMaterial: SymmetricKey, outputByteCount: Int) -> SymmetricKey
```

## Parameters

- `inputKeyMaterial` — The main key or passcode the derivation function uses to derive a key.

- `outputByteCount` — The length in bytes of the resulting symmetric key.

## Return Value

The derived symmetric key.

## See Also

### Deriving a key

- [deriveKey(inputKeyMaterial:info:outputByteCount:)](<derivekey(inputkeymaterial_info_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information you specify.
- [deriveKey(inputKeyMaterial:salt:outputByteCount:)](<derivekey(inputkeymaterial_salt_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with salt that you specify.
- [deriveKey(inputKeyMaterial:salt:info:outputByteCount:)](<derivekey(inputkeymaterial_salt_info_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.
