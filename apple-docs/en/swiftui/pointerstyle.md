---
title: PointerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pointerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/pointerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pointerstyle.json'
content_hash: 'sha256:f9ea4195efc44110'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PointerStyle

<sub>Structure</sub>

A style describing the appearance of the pointer (also called a cursor) when it’s hovered over a view.

<sub>macOS, visionOS</sub>

```swift
struct PointerStyle
```

## Overview

Use the [pointerStyle(_:)](<view/pointerstyle(__).md>) view modifier to set a view’s pointer style.

For guidance on choosing an appropriate pointer style, refer to [Pointing devices](../design/human-interface-guidelines/pointing-devices.md) in the Human Interface Guidelines.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting built-in pointer styles

- [default](pointerstyle/default.md) — The pointer style that uses the default platform appearance.
- [horizontalText](pointerstyle/horizontaltext.md) — The pointer style appropriate for selecting or inserting text in a horizontal layout.
- [verticalText](pointerstyle/verticaltext.md) — The pointer style appropriate for selecting or inserting text in a vertical layout.
- [rectSelection](pointerstyle/rectselection.md) — The pointer style appropriate for precise rectangular selection, such as selecting a portion of an image or multiple lines of text.
- [grabIdle](pointerstyle/grabidle.md) — The pointer style appropriate to indicate that dragging to reposition content within specific bounds, such as panning a large image, is possible.
- [grabActive](pointerstyle/grabactive.md) — The pointer style appropriate for actively dragging to reposition content within specific bounds, such as panning a large image.
- [link](pointerstyle/link.md) — The pointer style appropriate for content opens a URL link to a webpage, document, or other item when clicked.
- [zoomIn](pointerstyle/zoomin.md) — The pointer style appropriate to indicate that the content can be zoomed in.
- [zoomOut](pointerstyle/zoomout.md) — The pointer style appropriate to indicate that the content can be zoomed out.
- [frameResize(position:directions:)](<pointerstyle/frameresize(position_directions_).md>) — The pointer style for resizing a rectangular frame from a specific edge or corner.
- [columnResize(directions:)](<pointerstyle/columnresize(directions_).md>) — The pointer style for resizing a column, or vertical division.
- [rowResize(directions:)](<pointerstyle/rowresize(directions_).md>) — The pointer style for resizing a row, or horizontal division.

### Creating custom pointer styles

- [image(_:hotSpot:)](<pointerstyle/image(__hotspot_).md>) — Initializes a pointer style with a given image and hot spot.
- [shape(_:eoFill:size:)](<pointerstyle/shape(__eofill_size_).md>) — Initializes a pointer style with a given shape.

### Supporting types

- [HorizontalDirection](horizontaldirection.md) — A direction on the horizontal axis.
- [VerticalDirection](verticaldirection.md) — A direction on the vertical axis.
- [FrameResizePosition](frameresizeposition.md) — The position along the perimeter of a rectangular frame (its edges and corners) from which it’s resized.
- [FrameResizeDirection](frameresizedirection.md) — The direction in which a rectangular frame can be resized.

### Type Properties

- [columnResize](pointerstyle/columnresize.md) — The pointer style for resizing a column, or vertical division, in either direction.
- [rowResize](pointerstyle/rowresize.md) — The pointer style for resizing a row, or horizontal division, in either direction.

## See Also

### Modifying pointer appearance

- [pointerStyle(_:)](<view/pointerstyle(__).md>) — Sets the pointer style to display when the pointer is over the view.
- [pointerVisibility(_:)](<view/pointervisibility(__).md>) — Sets the visibility of the pointer when it’s over the view.
