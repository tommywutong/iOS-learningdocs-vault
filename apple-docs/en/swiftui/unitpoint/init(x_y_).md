---
title: 'init(x:y:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/unitpoint/init(x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/unitpoint/init(x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/unitpoint/init%28x%3Ay%3A%29.json'
content_hash: 'sha256:fdee78b30e799303'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UnitPoint](../unitpoint.md)

# init(x:y:)

<sub>Initializer</sub>

Creates a unit point with the specified horizontal and vertical offsets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(x: CGFloat, y: CGFloat)
```

## Parameters

- `x` — The normalized distance from the origin to the point in the horizontal direction.

- `y` — The normalized distance from the origin to the point in the vertical direction.

## Discussion

Values outside the range `[0, 1]` project to points outside of a view.

## See Also

### Creating a point

- [init()](<init().md>) — Creates a unit point at the origin.
