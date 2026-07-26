---
title: contentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry/contentsize
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry/contentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry/contentsize.json'
content_hash: 'sha256:1e3c8b68e4e43c31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollGeometry](../scrollgeometry.md)

# contentSize

<sub>Instance Property</sub>

The size of the content of the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentSize: CGSize
```

## Discussion

Unlike the container size of the scroll view, this refers to the total size of the content of the scroll view which can be smaller or larger than its containing size.
