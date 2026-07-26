---
title: link
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pointerstyle/link
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle/link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle/link.json'
content_hash: 'sha256:7bf44ba2de901854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PointerStyle](../pointerstyle.md)

# link

<sub>Type Property</sub>

The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.

<sub>macOS</sub>

```swift
static let link: PointerStyle
```

## Discussion

This pointer style displays a pointing hand. You may apply this pointer style to a single view or a view hierarchy using the [pointerStyle(_:)](<../view/pointerstyle(__).md>) modifier.

## See Also

### Getting built-in pointer styles

- [default](default.md) — The pointer style that uses the default platform appearance.
- [horizontalText](horizontaltext.md) — The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [verticalText](verticaltext.md) — The pointer style appropriate for selecting or inserting text in a vertical layout.
- [rectSelection](rectselection.md) — The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [grabIdle](grabidle.md) — The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [grabActive](grabactive.md) — The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [zoomIn](zoomin.md) — The pointer style appropriate to indicate that the content can be zoomed in.
- [zoomOut](zoomout.md) — The pointer style appropriate to indicate that the content can be zoomed out.
- [frameResize(position:directions:)](<frameresize(position_directions_).md>) — The pointer style for resizing a rectangular frame from a specific edge or corner.
- [columnResize(directions:)](<columnresize(directions_).md>) — The pointer style for resizing a column, or vertical division.
- [rowResize(directions:)](<rowresize(directions_).md>) — The pointer style for resizing a row, or horizontal division.
