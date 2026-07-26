---
title: 'fontStyleAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/fontstyleatindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/fontstyleatindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/fontstyleatindex%3Arange%3A.json'
content_hash: 'sha256:f19f9c858042cde1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# fontStyleAtIndex:range:

<sub>Instance Method</sub>

Returns the font style and range at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (AVCaptionFontStyle) fontStyleAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned style applies.

## Return Value

The font style.

## See Also

### Accessing font styles

- [FontStyle](fontstyle.md) — Font styles for caption text.
- [fontWeightAtIndex:range:](fontweightatindex_range_.md) — Returns the font weight and range at the index position.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [decorationAtIndex:range:](decorationatindex_range_.md) — Returns the text decoration at the index position.
- [Decoration](decoration.md) — Text decorations for caption text.
