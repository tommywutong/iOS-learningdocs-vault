---
title: selectionRects
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionhighlightview/selectionrects
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionhighlightview/selectionrects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionhighlightview/selectionrects.json'
content_hash: 'sha256:5d529da1bb590a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionHighlightView](../uitextselectionhighlightview.md)

# selectionRects

<sub>Instance Property</sub>

The rectangles to draw with the selection highlight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectionRects: [UITextSelectionRect] { get set }
```

## Discussion

Use this property to get the rectangles to draw in a custom highlight view. The rectangles are in the coordinate space of the view that adopts this protocol.
