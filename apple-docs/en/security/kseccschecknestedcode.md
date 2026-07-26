---
title: kSecCSCheckNestedCode
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccschecknestedcode
source_url: 'https://developer.apple.com/documentation/security/kseccschecknestedcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccschecknestedcode.json'
content_hash: 'sha256:e29c05211575469a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSCheckNestedCode

<sub>Global Variable</sub>

For code in bundle form, locate and recursively check embedded code.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSCheckNestedCode: UInt32 { get }
```

## Discussion

Only code in standard locations is considered.
