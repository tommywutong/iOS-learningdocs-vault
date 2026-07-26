---
title: kSecTransformAbortOriginatorKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectransformabortoriginatorkey
source_url: 'https://developer.apple.com/documentation/security/ksectransformabortoriginatorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformabortoriginatorkey.json'
content_hash: 'sha256:ff5b1cba7597fa2f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformAbortOriginatorKey

<sub>Global Variable</sub>

The key in an error’s `userInfo` dictionary whose value indicates the transform that caused the chain to abort.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecTransformAbortOriginatorKey: CFString
```

## Discussion

Use the value associated with this key to determine exactly which transform failed when more than one error occurs during transform evaluation.
