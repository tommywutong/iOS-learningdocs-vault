---
title: kSecRandomDefault
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecrandomdefault
source_url: 'https://developer.apple.com/documentation/security/ksecrandomdefault'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecrandomdefault.json'
content_hash: 'sha256:08a34d2b4516223e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecRandomDefault

<sub>Global Variable</sub>

An alias for the default random number generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kSecRandomDefault: SecRandomRef
```

## Discussion

When passed to the [SecRandomCopyBytes](<secrandomcopybytes(______).md>) function as the random number generator reference, this constant indicates that the default number generator should be used.

This constant is a synonym for `NULL`.
