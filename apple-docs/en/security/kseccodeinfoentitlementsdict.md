---
title: kSecCodeInfoEntitlementsDict
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoentitlementsdict
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoentitlementsdict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoentitlementsdict.json'
content_hash: 'sha256:e782d532224bcd46'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoEntitlementsDict

<sub>Global Variable</sub>

A key whose value is a dictionary of embedded entitlements.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoEntitlementsDict: CFString
```

## Discussion

The value is a [CFDictionary](../corefoundation/cfdictionary.md) object containing the embedded entitlements of the code if it has entitlements and they are in standard dictionary form. The value is absent if the code has no entitlements, or they are in a different format (in which case, see [kSecCodeInfoEntitlements](kseccodeinfoentitlements.md)).
