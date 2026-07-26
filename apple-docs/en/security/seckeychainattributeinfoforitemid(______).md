---
title: 'SecKeychainAttributeInfoForItemID(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.2+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/seckeychainattributeinfoforitemid(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seckeychainattributeinfoforitemid(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainattributeinfoforitemid%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4efe99aa92f23d6f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainAttributeInfoForItemID(_:_:_:)

<sub>Function</sub>

Obtains tags for all possible attributes of a given item class.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecKeychainAttributeInfoForItemID(_ keychain: SecKeychain?, _ itemID: UInt32, _ info: UnsafeMutablePointer<UnsafeMutablePointer<SecKeychainAttributeInfo>?>) -> OSStatus
```

## Parameters

- `keychain` — A keychain object.

- `itemID` — The relation identifier of the item tags. An `itemID` is a `CSSM_DB_RECORDTYPE` type as defined in `cssmtype.h`.

- `info` — On return, a pointer to the keychain attribute information. Your application should call the [SecKeychainFreeAttributeInfo](<seckeychainfreeattributeinfo(__).md>) function to release this structure when done with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This call returns more attributes than are supported by the old style Keychain API and passing them into older calls yields an invalid attribute error. The recommended call to retrieve the attribute values is the [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) function.

> [!note] Note
> This is a CSSM-based API. CSSM is deprecated.
>
> For new development, where possible, you should generally use [SecItemCopyMatching](<secitemcopymatching(____).md>) to obtain the attributes of keychain items instead, because that function is based on Core Foundation types.
