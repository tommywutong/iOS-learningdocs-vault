---
title: kSecAttrAccessControl
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecattraccesscontrol
source_url: 'https://developer.apple.com/documentation/security/ksecattraccesscontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecattraccesscontrol.json'
content_hash: 'sha256:3e63531a8130a908'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecAttrAccessControl

<sub>Global Variable</sub>

A key with a value that’s an access control instance indicating access control settings for the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecAttrAccessControl: CFString
```

## Discussion

The corresponding value is a [SecAccessControl](secaccesscontrol.md) instance, created with the [SecAccessControlCreateWithFlags](<secaccesscontrolcreatewithflags(________).md>) method, containing access control conditions for the item. See [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md) for more details.

> [!important] Important
> This attribute is mutually exclusive with the [kSecAttrAccess](ksecattraccess.md) attribute.
