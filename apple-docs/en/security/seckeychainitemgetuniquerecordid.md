---
title: SecKeychainItemGetUniqueRecordID
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeychainitemgetuniquerecordid
source_url: 'https://developer.apple.com/documentation/security/seckeychainitemgetuniquerecordid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainitemgetuniquerecordid.json'
content_hash: 'sha256:35013a666f7c7e7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainItemGetUniqueRecordID

<sub>Function</sub>

Returns a CSSM unique record for the given keychain item object.

> [!warning] Deprecated
> The common security services manager module is no longer used.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecKeychainItemGetUniqueRecordID(SecKeychainItemRef itemRef, const CSSM_DB_UNIQUE_RECORD **uniqueRecordID);
```

## Parameters

- `itemRef` — A keychain item object.

- `uniqueRecordID` — On return, a pointer to a CSSM unique record for the given item. The unique record is valid until the item object is released.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

> [!important] Important
> This function is deprecated. The common security services manager module is no longer used.
