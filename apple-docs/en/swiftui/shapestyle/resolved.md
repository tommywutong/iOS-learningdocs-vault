---
title: Resolved
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shapestyle/resolved
source_url: 'https://developer.apple.com/documentation/swiftui/shapestyle/resolved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shapestyle/resolved.json'
content_hash: 'sha256:9d5d2e512dc68ca2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ShapeStyle](../shapestyle.md)

# Resolved

<sub>Associated Type</sub>

The type of shape style this will resolve to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Resolved : ShapeStyle = Never
```

## Discussion

When you create a custom shape style, Swift infers this type from your implementation of the required `resolve` function.

## See Also

### Resolving a shape style in an environment

- [resolve(in:)](<resolve(in_).md>) — Evaluate to a resolved shape style given the current `environment`.
