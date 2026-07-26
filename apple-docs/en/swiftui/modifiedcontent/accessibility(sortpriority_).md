---
title: 'accessibility(sortPriority:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/modifiedcontent/accessibility(sortpriority:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibility(sortpriority:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibility%28sortpriority%3A%29.json'
content_hash: 'sha256:21a18fac00261642'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibility(sortPriority:)

<sub>Instance Method</sub>

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

> [!warning] Deprecated
> Use [accessibilitySortPriority(_:)](<accessibilitysortpriority(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibility(sortPriority: Double) -> ModifiedContent<Content, Modifier>
```

## Discussion

Higher numbers are sorted first. The default sort priority is zero.
