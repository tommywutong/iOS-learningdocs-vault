---
title: errSecCSFileHardQuarantined
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccsfilehardquarantined
source_url: 'https://developer.apple.com/documentation/security/errseccsfilehardquarantined'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccsfilehardquarantined.json'
content_hash: 'sha256:c5d73ca8c6fc7e19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSFileHardQuarantined

<sub>Global Variable</sub>

File open or execution not allowed.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSFileHardQuarantined: OSStatus { get }
```

## Discussion

File has quarantine flags indicating that it should not be opened or executed under any circumstances. This usually occurs because the file was downloaded by a sandboxed application that does not have file download entitlements.
