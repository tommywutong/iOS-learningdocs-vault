---
title: kSecTransformPreviousErrorKey
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectransformpreviouserrorkey
source_url: 'https://developer.apple.com/documentation/security/ksectransformpreviouserrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformpreviouserrorkey.json'
content_hash: 'sha256:e4aaa8553c342d34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformPreviousErrorKey

<sub>Global Variable</sub>

The key in an error’s `userInfo` dictionary whose value specifies the previous error when multiple errors occur during transform evaluation.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecTransformPreviousErrorKey: CFString
```

## Discussion

Use the value associated with this key to trace through a chain of [CFError](../corefoundation/cferror.md) objects when more than one error occurs during transform evaluation.
