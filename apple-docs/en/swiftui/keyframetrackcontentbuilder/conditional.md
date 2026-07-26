---
title: KeyframeTrackContentBuilder.Conditional
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/keyframetrackcontentbuilder/conditional
source_url: 'https://developer.apple.com/documentation/swiftui/keyframetrackcontentbuilder/conditional'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/keyframetrackcontentbuilder/conditional.json'
content_hash: 'sha256:970eb2588e8b382a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [KeyframeTrackContentBuilder](../keyframetrackcontentbuilder.md)

# KeyframeTrackContentBuilder.Conditional

<sub>Structure</sub>

A conditional result from the result builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Conditional<ConditionalValue, First, Second> where ConditionalValue == First.Value, First : KeyframeTrackContent, Second : KeyframeTrackContent, First.Value == Second.Value
```

## Relationships

- **Conforms To**: [KeyframeTrackContent](../keyframetrackcontent.md)

## See Also

### Building keyframe track content

- [buildArray(_:)](<buildarray(__).md>)
- [buildBlock()](<buildblock().md>)
- [buildEither(first:)](<buildeither(first_).md>)
- [buildEither(second:)](<buildeither(second_).md>)
- [buildExpression(_:)](<buildexpression(__).md>)
- [buildPartialBlock(accumulated:next:)](<buildpartialblock(accumulated_next_).md>)
- [buildPartialBlock(first:)](<buildpartialblock(first_).md>)
