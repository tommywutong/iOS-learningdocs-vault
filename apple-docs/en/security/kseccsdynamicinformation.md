---
title: kSecCSDynamicInformation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsdynamicinformation
source_url: 'https://developer.apple.com/documentation/security/kseccsdynamicinformation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsdynamicinformation.json'
content_hash: 'sha256:ce9e29d35ca92d1b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSDynamicInformation

<sub>Global Variable</sub>

Dynamic validity information about running code.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSDynamicInformation: UInt32 { get }
```

## Discussion

This information cannot be returned for code on disk (represented by a [SecStaticCode](secstaticcode.md) object).
