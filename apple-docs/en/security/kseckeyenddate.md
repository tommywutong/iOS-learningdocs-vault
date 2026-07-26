---
title: kSecKeyEndDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/kseckeyenddate
source_url: 'https://developer.apple.com/documentation/security/kseckeyenddate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseckeyenddate.json'
content_hash: 'sha256:eb6f3c7670bdb2aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecKeyEndDate

<sub>Global Variable</sub>

Type `CSSM_DATE`.  Latest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.

<sub>macOS</sub>

```swift
var kSecKeyEndDate: Int32 { get }
```
