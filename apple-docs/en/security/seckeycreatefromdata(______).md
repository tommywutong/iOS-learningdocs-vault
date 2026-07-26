---
title: 'SecKeyCreateFromData(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeycreatefromdata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeycreatefromdata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeycreatefromdata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:db89109e4b728c05'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyCreateFromData(_:_:_:)

<sub>Function</sub>

Constructs a SecKeyRef object for a symmetric key.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
func SecKeyCreateFromData(_ parameters: CFDictionary, _ keyData: CFData, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> SecKey?
```

## Parameters

- `parameters` — A parameter dictionary that describes the key. See the discussion for details.

- `keyData` — A `CFDataRef` object that contains the raw key data.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

A symmetric key. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the key’s memory when you are done with it.

## Discussion

The parameters dictionary must contain (at minimum) an entry for the [kSecAttrKeyType](ksecattrkeytype.md) key with a value of [kSecAttrKeyTypeAES](ksecattrkeytypeaes.md) or any other key type defined in Key Type Value.

The keys below may be optionally set in the parameters dictionary (with a `CFBooleanRef` value) to override the default key usage values:

- [kSecAttrCanEncrypt](ksecattrcanencrypt.md)
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md)
- [kSecAttrCanWrap](ksecattrcanwrap.md)
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md)

These values default to `true` if no value is specified.
