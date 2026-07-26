---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/keyframesbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/keyframesbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframesbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:eb1376459153a2f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyframesBuilder](../keyframesbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Keyframes

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func buildExpression<Content>(_ expression: Content) -> Content where Value == Content.Value, Content : Keyframes
```

## See Also

### Building keyframes

- [buildArray(_:)](<buildarray(__).md>)
- [buildBlock()](<buildblock().md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildFinalResult(_:)](<buildfinalresult(__).md>)
- [buildPartialBlock(accumulated:next:)](<buildpartialblock(accumulated_next_).md>)
- [buildPartialBlock(first:)](<buildpartialblock(first_).md>)
