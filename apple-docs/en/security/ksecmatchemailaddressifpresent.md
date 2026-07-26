---
title: kSecMatchEmailAddressIfPresent
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecmatchemailaddressifpresent
source_url: 'https://developer.apple.com/documentation/security/ksecmatchemailaddressifpresent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecmatchemailaddressifpresent.json'
content_hash: 'sha256:0820cf722fd2def4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecMatchEmailAddressIfPresent

<sub>Global Variable</sub>

A key whose value is a string to match against a certificate or identity’s email address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecMatchEmailAddressIfPresent: CFString
```

## Discussion

The corresponding value is of type [CFString](../corefoundation/cfstring.md) and contains an RFC822 email address. If provided, returned certificates or identities are limited to those that either contain the address or do not contain any email address.
