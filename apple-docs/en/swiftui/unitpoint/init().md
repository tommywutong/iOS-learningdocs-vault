---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/unitpoint/init()
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint/init%28%29.json'
content_hash: 'sha256:5ba94aaaf5ebe1cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint](../unitpoint.md)

# init()

<sub>Initializer</sub>

Creates a unit point at the origin.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

A view’s origin appears in the top-left corner in a left-to-right language environment, with positive x toward the right. It appears in the top-right corner in a right-to-left language, with positive x toward the left. Positive y is always toward the bottom of the view.

## See Also

### Creating a point

- [init(x:y:)](<init(x_y_).md>) — Creates a unit point with the specified horizontal and vertical offsets.
