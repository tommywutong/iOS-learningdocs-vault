---
title: errSecCSHostReject
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/errseccshostreject
source_url: 'https://developer.apple.com/documentation/security/errseccshostreject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/errseccshostreject.json'
content_hash: 'sha256:83329aabe6a76890'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# errSecCSHostReject

<sub>Global Variable</sub>

Code rejected its host.

<sub>Mac Catalyst, macOS</sub>

```swift
var errSecCSHostReject: OSStatus { get }
```

## Discussion

This error indicates that there’s an internal requirement in the signature on the guest code that specifies conditions that the code host must meet, and the host failed to meet that requirement. For example, if the guest requires that the host be signed by Apple and it wasn’t, the system returns this error when validating requirements.
