---
title: 'columnResize(directions:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pointerstyle/columnresize(directions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle/columnresize(directions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle/columnresize%28directions%3A%29.json'
content_hash: 'sha256:7eb7acd9109d19eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PointerStyle](../pointerstyle.md)

# columnResize(directions:)

<sub>Type Method</sub>

The pointer style for resizing a column, or vertical division.

<sub>macOS</sub>

```swift
static func columnResize(directions: HorizontalDirection.Set) -> PointerStyle
```

## Parameters

- `directions` — The horizontal directions in which a column can be resized. This must not be empty.

## Return Value

A pointer style for resizing a column.

## Discussion

You may apply this pointer style to a single view or a view hierarchy using the [pointerStyle(_:)](<../view/pointerstyle(__).md>) modifier.

## See Also

### Getting built-in pointer styles

- [default](default.md) — The pointer style that uses the default platform appearance.
- [horizontalText](horizontaltext.md) — The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [verticalText](verticaltext.md) — The pointer style appropriate for selecting or inserting text in a vertical layout.
- [rectSelection](rectselection.md) — The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [grabIdle](grabidle.md) — The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [grabActive](grabactive.md) — The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [link](link.md) — The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.
- [zoomIn](zoomin.md) — The pointer style appropriate to indicate that the content can be zoomed in.
- [zoomOut](zoomout.md) — The pointer style appropriate to indicate that the content can be zoomed out.
- [frameResize(position:directions:)](<frameresize(position_directions_).md>) — The pointer style for resizing a rectangular frame from a specific edge or corner.
- [rowResize(directions:)](<rowresize(directions_).md>) — The pointer style for resizing a row, or horizontal division.
