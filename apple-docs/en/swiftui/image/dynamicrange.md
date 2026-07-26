---
title: Image.DynamicRange
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/image/dynamicrange
source_url: 'https://developer.apple.com/documentation/swiftui/image/dynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/dynamicrange.json'
content_hash: 'sha256:9918ca669646933a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# Image.DynamicRange

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct DynamicRange
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting dynamic range values

- [standard](dynamicrange/standard.md) — Restrict the image content dynamic range to the standard range.
- [high](dynamicrange/high.md) — Allow image content to use an unrestricted extended range.
- [constrainedHigh](dynamicrange/constrainedhigh.md) — Allow image content to use some extended range. This is appropriate for placing HDR content next to SDR content.

## See Also

### Specifying dynamic range

- [allowedDynamicRange(_:)](<alloweddynamicrange(__).md>) — Returns a new image configured with the specified allowed dynamic range.
- [allowedDynamicRange](../environmentvalues/alloweddynamicrange.md) — The allowed dynamic range for the view, or nil.
