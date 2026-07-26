---
title: Key Generation Attributes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/key-generation-attributes
source_url: 'https://developer.apple.com/documentation/security/key-generation-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/key-generation-attributes.json'
content_hash: 'sha256:4a3d1f11b967fb11'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Keys](keys.md)

# Key Generation Attributes

<sub>API Collection</sub>

Use attribute dictionary keys during cryptographic key generation.

## Overview

Use these dictionary keys in the `parameter` dictionary when you create new cryptographic keys with the [SecKeyCreateRandomKey](<seckeycreaterandomkey(____).md>) function. The type and size attributes are required, while all others are optional.

With the exception of [kSecAttrTokenID](ksecattrtokenid.md), you can specify the optional keys in either the top-level `parameter` dictionary or in one of the key-specific sub-dictionaries specified by the [kSecPrivateKeyAttrs](ksecprivatekeyattrs.md) and [kSecPublicKeyAttrs](ksecpublickeyattrs.md) attributes. In the latter case, the given attribute applies only to the private or public key, respectively.

Use these keys in exactly the same way for the `parameter` dictionary you supply to the legacy [SecKeyGeneratePair](<seckeygeneratepair(______).md>) function.

## Topics

### Required

- [kSecAttrKeyType](ksecattrkeytype.md) — A key whose value indicates the item’s algorithm.
- [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md) — A key whose value indicates the number of bits in a cryptographic key.

### Key Specific

- [kSecPrivateKeyAttrs](ksecprivatekeyattrs.md) — A key whose value is a dictionary of cryptographic key attributes specific to a private key.
- [kSecPublicKeyAttrs](ksecpublickeyattrs.md) — A key whose value is a dictionary of cryptographic key attributes specific to a public key.

### Optional

- [kSecAttrLabel](ksecattrlabel.md) — A key with a value that’s a string indicating the item’s label.
- [kSecAttrTokenID](ksecattrtokenid.md) — A key whose value indicates that a cryptographic key is in an external store.
- [kSecAttrIsPermanent](ksecattrispermanent.md) — A key whose value indicates the item’s permanence.
- [kSecAttrApplicationTag](ksecattrapplicationtag.md) — A key whose value indicates the item’s private tag.
- [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md) — A key whose value indicates the effective number of bits in a cryptographic key.
- [kSecAttrCanEncrypt](ksecattrcanencrypt.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for encryption.
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.
- [kSecAttrCanDerive](ksecattrcanderive.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for derivation.
- [kSecAttrCanSign](ksecattrcansign.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for digital signing.
- [kSecAttrCanVerify](ksecattrcanverify.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for signature verification.
- [kSecAttrCanWrap](ksecattrcanwrap.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for wrapping.
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for unwrapping.
