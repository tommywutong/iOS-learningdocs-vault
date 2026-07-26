---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyframes/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/keyframes/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframes/body-swift.associatedtype.json'
content_hash: 'sha256:ed6f83f1792fd915'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Keyframes](../keyframes.md)

# Body

<sub>Associated Type</sub>

The type of keyframes representing the body of this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Body : Keyframes
```

## Discussion

When you create a custom keyframes type, Swift infers this type from your implementation of the required [body](body-swift.property.md) property.

## See Also

### Creating a keyframe

- [body](body-swift.property.md) — The composition of content that comprise the keyframes.
- [Value](value.md) — The type of value animated by this keyframes type
