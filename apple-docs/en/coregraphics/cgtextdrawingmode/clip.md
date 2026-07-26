---
title: CGTextDrawingMode.clip
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgtextdrawingmode/clip
source_url: 'https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/clip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgtextdrawingmode/clip.json'
content_hash: 'sha256:5cf6ab9754c85a51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGTextDrawingMode](../cgtextdrawingmode.md)

# CGTextDrawingMode.clip

<sub>Case</sub>

Specifies to intersect the text with the current clipping path. This mode does not paint the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case clip
```

## See Also

### Constants

- [kCGTextFill](fill.md) — Perform a fill operation on the text.
- [kCGTextStroke](stroke.md) — Perform a stroke operation on the text.
- [kCGTextFillStroke](fillstroke.md) — Perform fill, then stroke operations on the text.
- [kCGTextInvisible](invisible.md) — Do not draw the text, but do update the text position.
- [kCGTextFillClip](fillclip.md) — Perform a fill operation, then intersect the text with the current clipping path.
- [kCGTextStrokeClip](strokeclip.md) — Perform a stroke operation, then intersect the text with the current clipping path.
- [kCGTextFillStrokeClip](fillstrokeclip.md) — Perform fill then stroke operations, then intersect the text with the current clipping path.
