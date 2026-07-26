---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/init%28_%3A%29.json'
content_hash: 'sha256:adb8d40da428263e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# init(_:)

<sub>Initializer</sub>

Creates an empty path, then executes a closure to add its initial elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ callback: (inout Path) -> ())
```

## Parameters

- `callback` — The Swift function that will be called to initialize the new path.

## See Also

### Creating a path

- [init()](<init().md>) — Creates an empty path.
- [init(ellipseIn:)](<init(ellipsein_).md>) — Creates a path as an ellipse within the given rectangle.
- [init(roundedRect:cornerRadius:style:)](<init(roundedrect_cornerradius_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerSize:style:)](<init(roundedrect_cornersize_style_).md>) — Creates a path containing a rounded rectangle.
- [init(roundedRect:cornerRadii:style:)](<init(roundedrect_cornerradii_style_).md>) — Creates a path as the given rounded rectangle, which may have uneven corner radii.
