---
title: 'init(roundedRect:cornerSize:style:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/init(roundedrect:cornersize:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/init(roundedrect:cornersize:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/init%28roundedrect%3Acornersize%3Astyle%3A%29.json'
content_hash: 'sha256:f38221bc011448fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# init(roundedRect:cornerSize:style:)

<sub>Initializer</sub>

Creates a path containing a rounded rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(roundedRect rect: CGRect, cornerSize: CGSize, style: RoundedCornerStyle = .continuous)
```

## Parameters

- `rect` — A rectangle, specified in user space coordinates.

- `cornerSize` — The size of the corners, specified in user space coordinates.

- `style` — The corner style. Defaults to the `continous` style if not specified.

## Discussion

This is a convenience function that creates a path of a rounded rectangle. Using this convenience function is more efficient than creating a path and adding a rounded rectangle to it.

## See Also

### Creating a path

- [init()](<init().md>) — Creates an empty path.
- [init(_:)](<init(__).md>) — Creates an empty path, then executes a closure to add its initial elements.
- [init(ellipseIn:)](<init(ellipsein_).md>) — Creates a path as an ellipse within the given rectangle.
- [init(roundedRect:cornerRadius:style:)](<init(roundedrect_cornerradius_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerRadii:style:)](<init(roundedrect_cornerradii_style_).md>) — Creates a path as the given rounded rectangle, which may have uneven corner radii.
