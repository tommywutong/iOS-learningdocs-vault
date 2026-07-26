---
title: 'buildEither(second:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyframetrackcontentbuilder/buildeither(second:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder/buildeither(second:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframetrackcontentbuilder/buildeither%28second%3A%29.json'
content_hash: 'sha256:d404144a2a22060d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyframeTrackContentBuilder](../keyframetrackcontentbuilder.md)

# buildEither(second:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildEither<First, Second>(second component: Second) -> KeyframeTrackContentBuilder<Value>.Conditional<Value, First, Second> where Value == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value
```

## See Also

### Building keyframe track content

- [buildArray(_:)](<buildarray(__).md>)
- [buildBlock()](<buildblock().md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildExpression(_:)](<buildexpression(__).md>)
- [buildPartialBlock(accumulated:next:)](<buildpartialblock(accumulated_next_).md>)
- [buildPartialBlock(first:)](<buildpartialblock(first_).md>)
- [Conditional](conditional.md) — A conditional result from the result builder.
