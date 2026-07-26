---
title: SecTransformAttribute
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/sectransformattribute
source_url: 'https://developer.apple.com/documentation/security/sectransformattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformattribute.json'
content_hash: 'sha256:5fa8080e45f46e76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformAttribute

<sub>Type Alias</sub>

A direct reference to a security transform attribute.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
typealias SecTransformAttribute = CFTypeRef
```

## Discussion

Using an attribute reference rather than referring to it by name, such as in calls to the [SecTransformCustomSetAttribute](<sectransformcustomsetattribute(________).md>) function, speeds up the operation.
