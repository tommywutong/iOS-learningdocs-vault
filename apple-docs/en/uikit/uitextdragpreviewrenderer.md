---
title: UITextDragPreviewRenderer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragpreviewrenderer
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer.json'
content_hash: 'sha256:703ded344c6c9138'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextDragPreviewRenderer

<sub>Class</sub>

Renders previews of text dragged by the user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UITextDragPreviewRenderer
```

## Overview

Use this class to provide custom previews of dragged text that follows user interface guidelines and handles right-to-left text. You provide the layout manager and the range to render the preview.

Subclasses may override the [- adjustFirstLineRect:bodyRect:lastLineRect:textOrigin:](<uitextdragpreviewrenderer/adjust(firstlinerect_bodyrect_lastlinerect_textorigin_).md>) method to modify the detected rectangles as needed during the drag operation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a text drag preview renderer

- [- initWithLayoutManager:range:](<uitextdragpreviewrenderer/init(layoutmanager_range_).md>) — Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.
- [- initWithLayoutManager:range:unifyRects:](<uitextdragpreviewrenderer/init(layoutmanager_range_unifyrects_).md>) — Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.

### Getting and setting bounding rectangles

- [bodyRect](uitextdragpreviewrenderer/bodyrect.md) — The bounding rectangle of the text in the middle of the drag preview.
- [firstLineRect](uitextdragpreviewrenderer/firstlinerect.md) — The bounding rectangle of the first line of text in the drag preview.
- [lastLineRect](uitextdragpreviewrenderer/lastlinerect.md) — The bounding rectangle of the last line of text in the drag preview.
- [- adjustFirstLineRect:bodyRect:lastLineRect:textOrigin:](<uitextdragpreviewrenderer/adjust(firstlinerect_bodyrect_lastlinerect_textorigin_).md>) — Adjusts the size and origin of the bounding rectangles during a text drag operation.

### Getting the preview image

- [image](uitextdragpreviewrenderer/image.md) — The image of the text drag preview that’s rendered by the layout manager.

### Getting the layout manager

- [layoutManager](uitextdragpreviewrenderer/layoutmanager.md) — The layout manager that renders the text drag preview.

## See Also

### Drag content

- [UITextDragRequest](uitextdragrequest.md) — The interface for describing the attributes of a drag activity originating in a text view.
