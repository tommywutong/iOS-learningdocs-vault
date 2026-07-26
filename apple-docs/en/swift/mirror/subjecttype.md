---
title: subjectType
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/subjecttype
source_url: 'https://developer.apple.com/documentation/swift/mirror/subjecttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/subjecttype.json'
content_hash: 'sha256:19a1b9157b4ed236'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# subjectType

<sub>Instance Property</sub>

The static type of the subject being reflected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let subjectType: any Any.Type
```

## Discussion

This type may differ from the subject’s dynamic type when this mirror is the `superclassMirror` of another mirror.
