---
title: kSecGuestAttributeArchitecture
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecguestattributearchitecture
source_url: 'https://developer.apple.com/documentation/security/ksecguestattributearchitecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecguestattributearchitecture.json'
content_hash: 'sha256:468a60f0faf63331'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecGuestAttributeArchitecture

<sub>Global Variable</sub>

A key whose value is a number representing the CPU type under which the guest code is designed to run.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecGuestAttributeArchitecture: CFString
```

## Discussion

See the ARCH(3) manual page for a list of possible CPU types.
