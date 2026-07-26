---
title: 'init(layoutManager:range:unifyRects:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:unifyrects:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:unifyrects:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer/init%28layoutmanager%3Arange%3Aunifyrects%3A%29.json'
content_hash: 'sha256:eb3719fd4fb97d47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragPreviewRenderer](../uitextdragpreviewrenderer.md)

# init(layoutManager:range:unifyRects:)

<sub>Initializer</sub>

Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(layoutManager: NSLayoutManager, range: NSRange, unifyRects: Bool)
```

## Parameters

- `layoutManager` — The layout manager that renders the preview.

- `range` — The range to render the preview.

- `unifyRects` — A Boolean value that indicates whether the vertical position and height of the detection rectangles adjust to touch each other. If `true`, the [firstLineRect](firstlinerect.md), [bodyRect](bodyrect.md), and [lastLineRect](lastlinerect.md) properties adjust; otherwise, they don’t. The default value is `true`.

## Return Value

A renderer of a text drag preview using the specified layout manager, range, and detection behavior.

## See Also

### Initializing a text drag preview renderer

- [- initWithLayoutManager:range:](<init(layoutmanager_range_).md>) — Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.
