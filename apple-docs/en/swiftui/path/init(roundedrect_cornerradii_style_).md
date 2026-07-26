---
title: 'init(roundedRect:cornerRadii:style:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/init(roundedrect:cornerradii:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/init(roundedrect:cornerradii:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/init%28roundedrect%3Acornerradii%3Astyle%3A%29.json'
content_hash: 'sha256:3649cf079ab4041a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# init(roundedRect:cornerRadii:style:)

<sub>Initializer</sub>

Creates a path as the given rounded rectangle, which may have uneven corner radii.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(roundedRect rect: CGRect, cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle = .continuous)
```

## Parameters

- `rect` — A rectangle, specified in user space coordinates.

- `cornerRadii` — The radius of each corner of the rectangle, specified in user space coordinates.

- `style` — The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle. Using this function is more efficient than creating a path and adding a rounded rectangle to it.

## See Also

### Creating a path

- [init()](<init().md>) — Creates an empty path.
- [init(_:)](<init(__).md>) — Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn:)](<init(ellipsein_).md>) — Creates a path as an ellipse within the given rectangle.
- [init(roundedRect:cornerRadius:style:)](<init(roundedrect_cornerradius_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerSize:style:)](<init(roundedrect_cornersize_style_).md>) — Creates a path containing a rounded rectangle.
