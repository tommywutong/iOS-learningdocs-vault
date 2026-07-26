---
title: 'SecKeychainItemFreeAttributesAndData(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainitemfreeattributesanddata(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemfreeattributesanddata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemfreeattributesanddata%28_%3A_%3A%29.json'
content_hash: 'sha256:9779c9c8f9b90564'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemFreeAttributesAndData(_:_:)

<sub>Function</sub>

Releases the memory used by the keychain attribute list and/or the keychain data retrieved in a call to `SecKeychainItemCopyAttributesAndData`.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainItemFreeAttributesAndData(_ attrList: UnsafeMutablePointer<SecKeychainAttributeList>?, _ data: UnsafeMutableRawPointer?) -> OSStatus
```

## Parameters

- `attrList` — A pointer to the attribute list to release. Pass `NULL` if there is no attribute list to release.

- `data` — A pointer to the data buffer to release. Pass `NULL` if there is no data to release.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
