---
title: 'setFontWeight:inRange:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/setfontweight:inrange:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/setfontweight:inrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/setfontweight%3Ainrange%3A.json'
content_hash: 'sha256:e8aea9d3d91f5e00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setFontWeight:inRange:

<sub>Instance Method</sub>

Sets the font weight for a range of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (void) setFontWeight:(AVCaptionFontWeight) fontWeight inRange:(NSRange) range;
```

## Parameters

- `fontWeight` — The font weight.

- `range` — The range to which this font weight applies.

## See Also

### Configuring font styles

- [FontStyle](../avcaption/fontstyle.md) — Font styles for caption text.
- [setFontStyle:inRange:](setfontstyle_inrange_.md) — Sets the font style for a range of text.
- [removeFontStyleInRange:](removefontstyleinrange_.md) — Removes a font style from a range of text.
- [FontWeight](../avcaption/fontweight.md) — Font weights for a caption.
- [removeFontWeightInRange:](removefontweightinrange_.md) — Removes a font weight from a range of text.
- [Decoration](../avcaption/decoration.md) — Text decorations for caption text.
- [setDecoration:inRange:](setdecoration_inrange_.md) — Sets a decoration for a range of text.
- [removeDecorationInRange:](removedecorationinrange_.md) — Removes a decoration from a range of text.
