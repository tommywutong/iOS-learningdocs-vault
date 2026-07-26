---
title: 'setFontStyle:inRange:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecaption/setfontstyle:inrange:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecaption/setfontstyle:inrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecaption/setfontstyle%3Ainrange%3A.json'
content_hash: 'sha256:06b096ed49fcab06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableCaption](../avmutablecaption.md)

# setFontStyle:inRange:

<sub>Instance Method</sub>

Sets the font style for a range of text.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (void) setFontStyle:(AVCaptionFontStyle) fontStyle inRange:(NSRange) range;
```

## Parameters

- `fontStyle` — The font style.

- `range` — The range to which this style applies.

## See Also

### Configuring font styles

- [FontStyle](../avcaption/fontstyle.md) — Font styles for caption text.
- [removeFontStyleInRange:](removefontstyleinrange_.md) — Removes a font style from a range of text.
- [FontWeight](../avcaption/fontweight.md) — Font weights for a caption.
- [setFontWeight:inRange:](setfontweight_inrange_.md) — Sets the font weight for a range of text.
- [removeFontWeightInRange:](removefontweightinrange_.md) — Removes a font weight from a range of text.
- [Decoration](../avcaption/decoration.md) — Text decorations for caption text.
- [setDecoration:inRange:](setdecoration_inrange_.md) — Sets a decoration for a range of text.
- [removeDecorationInRange:](removedecorationinrange_.md) — Removes a decoration from a range of text.
