---
title: id
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subview/id-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/subview/id-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subview/id-swift.property.json'
content_hash: 'sha256:d177394cc84c79a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Subview](../subview.md)

# id

<sub>Instance Property</sub>

The unique identifier of the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var id: Subview.ID { get }
```

## Discussion

This identifier persists across updates, changes to the order of subviews, etc. so can be used to track the lifetime of a subview.
