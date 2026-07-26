---
title: 'Mirror.AncestorRepresentation.customized(_:)'
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mirror/ancestorrepresentation/customized(_:)'
source_url: 'https://developer.apple.com/documentation/swift/mirror/ancestorrepresentation/customized(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/ancestorrepresentation/customized%28_%3A%29.json'
content_hash: 'sha256:69fff6d319821c43'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Mirror](../../mirror.md) · [AncestorRepresentation](../ancestorrepresentation.md)

# Mirror.AncestorRepresentation.customized(_:)

<sub>Case</sub>

Uses the nearest ancestor’s implementation of `customMirror` to create a mirror for that ancestor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case customized(() -> Mirror)
```

## Discussion

Other classes derived from such an ancestor are given a default mirror. The payload for this option should always be `{ super.customMirror }`:

```swift
var customMirror: Mirror {
    return Mirror(
        self,
        children: ["someProperty": self.someProperty],
        ancestorRepresentation: .customized({ super.customMirror })) // <==
}
```
