---
title: kSecKeyStartDate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.3+（12.0 起废弃）, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/kseckeystartdate
source_url: 'https://developer.apple.com/documentation/security/kseckeystartdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseckeystartdate.json'
content_hash: 'sha256:fa3c3ffa2f31501d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecKeyStartDate

<sub>Global Variable</sub>

Type `CSSM_DATE`.  Earliest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.

<sub>macOS</sub>

```swift
var kSecKeyStartDate: Int32 { get }
```
