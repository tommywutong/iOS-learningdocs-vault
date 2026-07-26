---
title: kSecCSDoNotValidateResources
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsdonotvalidateresources
source_url: 'https://developer.apple.com/documentation/security/kseccsdonotvalidateresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsdonotvalidateresources.json'
content_hash: 'sha256:bf8ae6626493b10d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSDoNotValidateResources

<sub>Global Variable</sub>

Do not validate the presence and contents of all bundle resources (if any).

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSDoNotValidateResources: UInt32 { get }
```

## Discussion

By default, a mismatch in any bundle resource causes validation to fail.
