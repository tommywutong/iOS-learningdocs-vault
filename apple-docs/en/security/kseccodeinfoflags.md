---
title: kSecCodeInfoFlags
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfoflags
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfoflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfoflags.json'
content_hash: 'sha256:62daef6728db9ce7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoFlags

<sub>Global Variable</sub>

A key whose value indicates the static (on-disk) state of the object.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoFlags: CFString
```

## Discussion

The value is a [CFNumber](../corefoundation/cfnumber.md). See [SecCodeSignatureFlags](seccodesignatureflags.md) for a list of possible values.
