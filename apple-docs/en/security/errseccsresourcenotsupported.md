---
title: errSecCSResourceNotSupported
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccsresourcenotsupported
source_url: 'https://developer.apple.com/documentation/security/errseccsresourcenotsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccsresourcenotsupported.json'
content_hash: 'sha256:4c4993c87f038edc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSResourceNotSupported

<sub>Global Variable</sub>

Found an unsupported resource.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSResourceNotSupported: OSStatus { get }
```

## Discussion

Resources other than directories, plain files, and symbolic links are not supported.
