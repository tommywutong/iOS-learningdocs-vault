---
title: 'SecKeyGeneratePairAsync(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeygeneratepairasync(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeygeneratepairasync(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygeneratepairasync%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e733c992fe498c8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGeneratePairAsync(_:_:_:)

<sub>Function</sub>

Generates a public/private key pair.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
func SecKeyGeneratePairAsync(_ parameters: CFDictionary, _ deliveryQueue: dispatch_queue_t, _ result: @escaping SecKeyGeneratePairBlock)
```

## Parameters

- `parameters` — A key generation parameter dictionary. At minimum, this must contain [kSecAttrKeyType](ksecattrkeytype.md) and [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md). In addition, this function assumes default values for the following keys: - [kSecAttrLabel](ksecattrlabel.md) defaults to `NULL`. - [kSecAttrIsPermanent](ksecattrispermanent.md) if this key is present and has a value of [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), the key or key pair will be added to the default keychain. - [kSecAttrApplicationTag](ksecattrapplicationtag.md) defaults to `NULL`. - [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md) defaults to `NULL`, which means the effective key size is the same as the key size ([kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md)). - [kSecAttrCanEncrypt](ksecattrcanencrypt.md) defaults to [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for private keys, [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for public keys. - [kSecAttrCanDecrypt](ksecattrcandecrypt.md) defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for private keys, [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for public keys. - [kSecAttrCanDerive](ksecattrcanderive.md) defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md). - [kSecAttrCanSign](ksecattrcansign.md) defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for private keys, [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for public keys. - [kSecAttrCanVerify](ksecattrcanverify.md) defaults to [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for private keys, [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for public keys. - [kSecAttrCanWrap](ksecattrcanwrap.md) defaults to [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for private keys, [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for public keys. - [kSecAttrCanUnwrap](ksecattrcanunwrap.md) defaults to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) for private keys, [kCFBooleanFalse](../corefoundation/kcfbooleanfalse.md) for public keys. These default values can be overridden by adding a value for the associated key in the parameter dictionary.

- `deliveryQueue` — The dispatch queue on which the result block should be scheduled.

- `result` — A block of type [SecKeyGeneratePairBlock](seckeygeneratepairblock.md) that gets called with the result upon completion.
