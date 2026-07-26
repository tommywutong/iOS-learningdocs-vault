---
title: Mirror.AncestorRepresentation.generated
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mirror/ancestorrepresentation/generated
source_url: 'https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation/generated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/ancestorrepresentation/generated.json'
content_hash: 'sha256:fb53e6e5516674ab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Mirror](../../mirror.md) · [AncestorRepresentation](../ancestorrepresentation.md)

# Mirror.AncestorRepresentation.generated

<sub>Case</sub>

Generates a default mirror for all ancestor classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case generated
```

## Discussion

This case is the default when initializing a `Mirror` instance.

When you use this option, a subclass’s mirror generates default mirrors even for ancestor classes that conform to the `CustomReflectable` protocol. To avoid dropping the customization provided by ancestor classes, an override of `customMirror` should pass `.customized({ super.customMirror })` as `ancestorRepresentation` when initializing its mirror.
