---
title: SecGuestRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secguestref
source_url: 'https://developer.apple.com/documentation/security/secguestref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secguestref.json'
content_hash: 'sha256:18bbca49d819c1df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecGuestRef

<sub>Type Alias</sub>

A reference to a guest object, which identifies a particular block of guest code in the context of its code signing host.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecGuestRef = UInt32
```

## Discussion

Guest handles are assigned by the host at will, with [kSecNoGuest](ksecnoguest.md) being reserved as the `NULL` value. They can be reused for new children if desired.
