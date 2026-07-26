---
title: SecItemAttr.creationDateItemAttr
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr/creationdateitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr/creationdateitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr/creationdateitemattr.json'
content_hash: 'sha256:67698fde7992c5e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemAttr](../secitemattr.md)

# SecItemAttr.creationDateItemAttr

<sub>Case</sub>

Identifies the creation date attribute.

<sub>Mac Catalyst, macOS</sub>

```swift
case creationDateItemAttr
```

## Discussion

You use this tag to get a string value that represents the date the item was created, expressed in Zulu Time format (“YYYYMMDDhhmmssZ”). This is the native format for stored time values in the CDSA specification (defined as `CSSM_DB_ATTRIBUTE_FORMAT_TIME_DATE` in the `CSSM_DB_ATTRIBUTE_FORMAT` enumeration, Section 17.2.6.). When specifying the creation date as input to a function (for example, [SecKeychainSearchCreateFromAttributes](../seckeychainsearchcreatefromattributes.md)), you may alternatively provide a numeric value of type `UInt32` or `SInt64`, expressed as seconds since 01 January 1904.
