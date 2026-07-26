---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentmarginplacement/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/contentmarginplacement/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentmarginplacement/automatic.json'
content_hash: 'sha256:28a55bd543506d62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentMarginPlacement](../contentmarginplacement.md)

# automatic

<sub>Type Property</sub>

The automatic placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ContentMarginPlacement { get }
```

## Discussion

Views that support margin customization can automatically use margins with this placement. For example, a [ScrollView](../scrollview.md) will use this placement to automatically inset both its content and scroll indicators by the specified amount.

## See Also

### Getting the placement

- [scrollContent](scrollcontent.md) — The scroll content placement.
- [scrollIndicators](scrollindicators.md) — The scroll indicators placement.
