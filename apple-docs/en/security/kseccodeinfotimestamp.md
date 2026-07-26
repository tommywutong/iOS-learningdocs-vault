---
title: kSecCodeInfoTimestamp
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccodeinfotimestamp
source_url: 'https://developer.apple.com/documentation/security/kseccodeinfotimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccodeinfotimestamp.json'
content_hash: 'sha256:b0667fe699c431a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCodeInfoTimestamp

<sub>Global Variable</sub>

A key whose value indicates the actual signing date.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCodeInfoTimestamp: CFString
```

## Discussion

The value is a [CFDate](../corefoundation/cfdate.md) object describing the signing date as (securely) certified by a timestamp authority service. This timestamp cannot be falsified by the signer, and is trusted to the same degree as the timestamp service that created the timestamp.
