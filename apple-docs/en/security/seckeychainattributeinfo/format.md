---
title: format
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainattributeinfo/format
source_url: 'https://developer.apple.com/documentation/security/seckeychainattributeinfo/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainattributeinfo/format.json'
content_hash: 'sha256:a6c8bf088c1e3609'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeychainAttributeInfo](../seckeychainattributeinfo.md)

# format

<sub>Instance Property</sub>

A pointer to the first attribute format in the array.

<sub>macOS</sub>

```swift
var format: UnsafeMutablePointer<UInt32>?
```

## Discussion

Attribute formats are of type `CSSM_DB_ATTRIBUTE_FORMAT` (`CSSM_DB_ATTRIBUTE_FORMAT_STRING`, for example), and are defined in the `cssmtype.h` header.
