---
title: kSecCSBasicValidateOnly
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsbasicvalidateonly
source_url: 'https://developer.apple.com/documentation/security/kseccsbasicvalidateonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsbasicvalidateonly.json'
content_hash: 'sha256:6bc68cbe5701b9d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSBasicValidateOnly

<sub>Global Variable</sub>

Do not validate either the main executable or the bundle resources, if any.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSBasicValidateOnly: UInt32 { get }
```

## Discussion

This flag is the bitwise OR of the [kSecCSDoNotValidateExecutable](kseccsdonotvalidateexecutable.md) and [kSecCSDoNotValidateResources](kseccsdonotvalidateresources.md) flags.
