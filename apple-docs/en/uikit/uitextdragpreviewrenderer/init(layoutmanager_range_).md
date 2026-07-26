---
title: 'init(layoutManager:range:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragpreviewrenderer/init(layoutmanager:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragpreviewrenderer/init%28layoutmanager%3Arange%3A%29.json'
content_hash: 'sha256:104cd486c3758f66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragPreviewRenderer](../uitextdragpreviewrenderer.md)

# init(layoutManager:range:)

<sub>Initializer</sub>

Initializes and returns a text drag preview renderer with the specified layout managers and range to render the text drag preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(layoutManager: NSLayoutManager, range: NSRange)
```

## Parameters

- `layoutManager` — The layout manager that renders the text drag preview.

- `range` — The range to render the text drag preview.

## Return Value

A renderer of a text drag preview using the specified layout manager and range.

## See Also

### Initializing a text drag preview renderer

- [- initWithLayoutManager:range:unifyRects:](<init(layoutmanager_range_unifyrects_).md>) — Returns an initialized renderer of a text drag preview with the specified layout manager, range, and rectangle detection behavior.
