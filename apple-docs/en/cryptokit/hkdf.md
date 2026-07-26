---
title: HKDF
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hkdf
source_url: 'https://developer.apple.com/documentation/cryptokit/hkdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hkdf.json'
content_hash: 'sha256:6a0bff6575675e14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# HKDF

<sub>Structure</sub>

A standards-based implementation of an HMAC-based Key Derivation Function (HKDF).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HKDF<H> where H : HashFunction
```

## Overview

The key derivation functions allow you to derive one or more secrets of the size of your choice from a main key or passcode. The key derivation function is compliant with IETF RFC 5869. Use one of the `deriveKey` functions, such as [deriveKey(inputKeyMaterial:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_outputbytecount_).md>) or [deriveKey(inputKeyMaterial:salt:info:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_salt_info_outputbytecount_).md>), to derive a key from a main secret or passcode in a single function.

To derive a key with more fine-grained control, use `extract(inputKeyMaterial:salt:)` to create cryptographically strong key material in the form of a hashed authentication code, then call [expand(pseudoRandomKey:info:outputByteCount:)](<hkdf/expand(pseudorandomkey_info_outputbytecount_).md>) using that key material to generate a symmetric key of the length you specify.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Deriving a key

- [deriveKey(inputKeyMaterial:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation.
- [deriveKey(inputKeyMaterial:info:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_info_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information you specify.
- [deriveKey(inputKeyMaterial:salt:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_salt_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with salt that you specify.
- [deriveKey(inputKeyMaterial:salt:info:outputByteCount:)](<hkdf/derivekey(inputkeymaterial_salt_info_outputbytecount_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify.

### Controlling key derivation

- [expand(pseudoRandomKey:info:outputByteCount:)](<hkdf/expand(pseudorandomkey_info_outputbytecount_).md>) — Expands cryptographically strong key material into a derived symmetric key.

### Type Methods

- [deriveKey(inputKeyMaterial:salt:info:output:)](<hkdf/derivekey(inputkeymaterial_salt_info_output_).md>) — Derives a symmetric encryption key from a main key or passcode using HKDF key derivation with information and salt you specify. _(beta)_
- [expand(pseudoRandomKey:info:into:)](<hkdf/expand(pseudorandomkey_info_into_).md>) — Expands cryptographically strong key material into a derived symmetric key. _(beta)_
- [extract(inputKeyMaterial:salt:)](<hkdf/extract(inputkeymaterial_salt_)-4f5wf.md>) — Creates cryptographically strong key material from a main key or passcode that you specify.
- [extract(inputKeyMaterial:salt:)](<hkdf/extract(inputkeymaterial_salt_)-7qmzj.md>) — Creates cryptographically strong key material from a main key or passcode that you specify. _(beta)_
