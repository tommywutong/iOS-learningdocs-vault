---
title: kSecCSContentInformation
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccscontentinformation
source_url: 'https://developer.apple.com/documentation/security/kseccscontentinformation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccscontentinformation.json'
content_hash: 'sha256:d1a0f4ee64a6c473'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSContentInformation

<sub>Global Variable</sub>

More information about the file system contents making up the signed code on disk.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSContentInformation: UInt32 { get }
```

## Discussion

It is not generally advisable to make use of this information, but some utilities (such as software-update tools) may find it useful.
