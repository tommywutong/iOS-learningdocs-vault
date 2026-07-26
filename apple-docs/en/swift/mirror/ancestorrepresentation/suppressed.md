---
title: Mirror.AncestorRepresentation.suppressed
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/ancestorrepresentation/suppressed
source_url: 'https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation/suppressed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/ancestorrepresentation/suppressed.json'
content_hash: 'sha256:c82df6eec1b0a620'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Mirror](../../mirror.md) · [AncestorRepresentation](../ancestorrepresentation.md)

# Mirror.AncestorRepresentation.suppressed

<sub>Case</sub>

Suppresses the representation of all ancestor classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case suppressed
```

## Discussion

In a mirror created with this ancestor representation, the `superclassMirror` property is `nil`.
