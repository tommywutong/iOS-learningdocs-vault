---
title: kSecGuestAttributeCanonical
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecguestattributecanonical
source_url: 'https://developer.apple.com/documentation/security/ksecguestattributecanonical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecguestattributecanonical.json'
content_hash: 'sha256:71e1469dc5846ff8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecGuestAttributeCanonical

<sub>Global Variable</sub>

A key whose value is the guest code object for that guest.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecGuestAttributeCanonical: CFString
```

## Discussion

This object plus the process ID ([kSecGuestAttributePid](ksecguestattributepid.md)) uniquely identify the guest.
