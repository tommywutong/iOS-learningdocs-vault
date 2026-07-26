---
title: default
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pointerstyle/default
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle/default.json'
content_hash: 'sha256:9aea9c781105576d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PointerStyle](../pointerstyle.md)

# default

<sub>Type Property</sub>

The pointer style that uses the default platform appearance.

<sub>macOS, visionOS</sub>

```swift
static let `default`: PointerStyle
```

## Discussion

This is the default pointer style for interacting with content and UI elements if no other pointer style is more appropriate. This pointer style displays an arrow in macOS and a circle in iPadOS and visionOS.

You might want to set this pointer style explicitly using the [pointerStyle(_:)](<../view/pointerstyle(__).md>) modifier to override another style in the environment.

## See Also

### Getting built-in pointer styles

- [horizontalText](horizontaltext.md) — The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [verticalText](verticaltext.md) — The pointer style appropriate for selecting or inserting text in a vertical layout.
- [rectSelection](rectselection.md) — The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [grabIdle](grabidle.md) — The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [grabActive](grabactive.md) — The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [link](link.md) — The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.
- [zoomIn](zoomin.md) — The pointer style appropriate to indicate that the content can be zoomed in.
- [zoomOut](zoomout.md) — The pointer style appropriate to indicate that the content can be zoomed out.
- [frameResize(position:directions:)](<frameresize(position_directions_).md>) — The pointer style for resizing a rectangular frame from a specific edge or corner.
- [columnResize(directions:)](<columnresize(directions_).md>) — The pointer style for resizing a column, or vertical division.
- [rowResize(directions:)](<rowresize(directions_).md>) — The pointer style for resizing a row, or horizontal division.
