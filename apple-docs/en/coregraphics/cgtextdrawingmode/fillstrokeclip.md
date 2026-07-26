---
title: CGTextDrawingMode.fillStrokeClip
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgtextdrawingmode/fillstrokeclip
source_url: 'https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillstrokeclip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgtextdrawingmode/fillstrokeclip.json'
content_hash: 'sha256:633ec6e8c3efc9fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGTextDrawingMode](../cgtextdrawingmode.md)

# CGTextDrawingMode.fillStrokeClip

<sub>Case</sub>

Perform fill then stroke operations, then intersect the text with the current clipping path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case fillStrokeClip
```

## See Also

### Constants

- [kCGTextFill](fill.md) — Perform a fill operation on the text.
- [kCGTextStroke](stroke.md) — Perform a stroke operation on the text.
- [kCGTextFillStroke](fillstroke.md) — Perform fill, then stroke operations on the text.
- [kCGTextInvisible](invisible.md) — Do not draw the text, but do update the text position.
- [kCGTextFillClip](fillclip.md) — Perform a fill operation, then intersect the text with the current clipping path.
- [kCGTextStrokeClip](strokeclip.md) — Perform a stroke operation, then intersect the text with the current clipping path.
- [kCGTextClip](clip.md) — Specifies to intersect the text with the current clipping path. This mode does not paint the text.
