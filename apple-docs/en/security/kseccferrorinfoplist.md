---
title: kSecCFErrorInfoPlist
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorinfoplist
source_url: 'https://developer.apple.com/documentation/security/kseccferrorinfoplist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorinfoplist.json'
content_hash: 'sha256:4867d408fc4f4f72'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorInfoPlist

<sub>Global Variable</sub>

A key whose value is a Core Foundation object identifying the invalid component or key in the dictionary.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorInfoPlist: CFString
```

## Discussion

This key is present when the `Info.plist` dictionary or other component has been found to be invalid.
