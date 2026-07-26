---
title: 'addRoundedRect(in:cornerRadii:style:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/addroundedrect(in:cornerradii:style:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/addroundedrect(in:cornerradii:style:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/addroundedrect%28in%3Acornerradii%3Astyle%3Atransform%3A%29.json'
content_hash: 'sha256:9c98f262f06ee353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# addRoundedRect(in:cornerRadii:style:transform:)

<sub>Instance Method</sub>

Adds a rounded rectangle with uneven corners to the path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func addRoundedRect(in rect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle = .continuous, transform: CGAffineTransform = .identity)
```

## Parameters

- `rect` — A rectangle, specified in user space coordinates.

- `cornerRadii` — The radius of each corner of the rectangle, specified in user space coordinates.

- `style` — The corner style. Defaults to the `continous` style if not specified.

- `transform` — An affine transform to apply to the rectangle before adding to the path. Defaults to the identity transform if not specified.

## Discussion

This is a convenience function that adds a rounded rectangle to a path, starting by moving to the center of the right edge and then adding lines and curves counter-clockwise to create a rounded rectangle, closing the subpath.
