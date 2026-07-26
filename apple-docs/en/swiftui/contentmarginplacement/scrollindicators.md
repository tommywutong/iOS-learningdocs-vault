---
title: scrollIndicators
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentmarginplacement/scrollindicators
source_url: 'https://developer.apple.com/documentation/swiftui/contentmarginplacement/scrollindicators'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentmarginplacement/scrollindicators.json'
content_hash: 'sha256:ec805d04785b5789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentMarginPlacement](../contentmarginplacement.md)

# scrollIndicators

<sub>Type Property</sub>

The scroll indicators placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var scrollIndicators: ContentMarginPlacement { get }
```

## Discussion

Scrollable views like [ScrollView](../scrollview.md) will use this placement to inset their scroll indicators, but not their content.

## See Also

### Getting the placement

- [automatic](automatic.md) — The automatic placement.
- [scrollContent](scrollcontent.md) — The scroll content placement.
