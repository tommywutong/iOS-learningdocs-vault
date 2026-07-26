---
title: kSecCSUseAllArchitectures
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsuseallarchitectures
source_url: 'https://developer.apple.com/documentation/security/kseccsuseallarchitectures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsuseallarchitectures.json'
content_hash: 'sha256:96701e47ea83dfc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSUseAllArchitectures

<sub>Global Variable</sub>

Flag for requesting all architectures.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSUseAllArchitectures: UInt32 { get }
```

## Discussion

When this flag is used, if code refers to a single architecture of a universal binary, return a [SecStaticCode](secstaticcode.md) object that refers to the entire universal code with all its architectures. By default, the returned static reference identifies only the actual architecture of the running program.
