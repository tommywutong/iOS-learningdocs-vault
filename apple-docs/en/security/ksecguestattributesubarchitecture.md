---
title: kSecGuestAttributeSubarchitecture
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecguestattributesubarchitecture
source_url: 'https://developer.apple.com/documentation/security/ksecguestattributesubarchitecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecguestattributesubarchitecture.json'
content_hash: 'sha256:c1666b462b9f66f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecGuestAttributeSubarchitecture

<sub>Global Variable</sub>

A key whose value is a number representing the CPU subtype under which the guest code is designed to run.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecGuestAttributeSubarchitecture: CFString
```

## Discussion

See the ARCH(3) manual page for a list of possible CPU subtypes.
