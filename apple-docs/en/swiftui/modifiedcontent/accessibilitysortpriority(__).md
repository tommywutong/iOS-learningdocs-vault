---
title: 'accessibilitySortPriority(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/modifiedcontent/accessibilitysortpriority(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilitysortpriority(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/modifiedcontent/accessibilitysortpriority%28_%3A%29.json'
content_hash: 'sha256:681ec67c4d239c67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ModifiedContent](../modifiedcontent.md)

# accessibilitySortPriority(_:)

<sub>Instance Method</sub>

Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessibilitySortPriority(_ sortPriority: Double) -> ModifiedContent<Content, Modifier>
```

## Discussion

Higher numbers are sorted first. The default sort priority is zero.
