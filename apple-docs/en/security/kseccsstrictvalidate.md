---
title: kSecCSStrictValidate
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccsstrictvalidate
source_url: 'https://developer.apple.com/documentation/security/kseccsstrictvalidate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccsstrictvalidate.json'
content_hash: 'sha256:322575900d50facb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCSStrictValidate

<sub>Global Variable</sub>

Perform additional checks to ensure the validity of code in bundle form.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecCSStrictValidate: UInt32 { get }
```

## Discussion

For code in bundle form, perform additional checks to verify that the bundle is not structured in a way that would allow tampering, and reject any resource envelope that introduces weaknesses into the signature.
