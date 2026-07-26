---
title: scrollContent
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentmarginplacement/scrollcontent
source_url: 'https://developer.apple.com/documentation/swiftui/contentmarginplacement/scrollcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentmarginplacement/scrollcontent.json'
content_hash: 'sha256:d039cf6105cf270c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentMarginPlacement](../contentmarginplacement.md)

# scrollContent

<sub>Type Property</sub>

The scroll content placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var scrollContent: ContentMarginPlacement { get }
```

## Discussion

Scrollable views like [ScrollView](../scrollview.md) will use this placement to inset their content, but not their scroll indicators.

## See Also

### Getting the placement

- [automatic](automatic.md) — The automatic placement.
- [scrollIndicators](scrollindicators.md) — The scroll indicators placement.
