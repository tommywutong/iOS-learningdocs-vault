---
title: 'fontWeightAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/fontweightatindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/fontweightatindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/fontweightatindex%3Arange%3A.json'
content_hash: 'sha256:aedc28eddd69027b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# fontWeightAtIndex:range:

<sub>Instance Method</sub>

Returns the font weight and range at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (AVCaptionFontWeight) fontWeightAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned weight applies.

## Return Value

The font weight.

## See Also

### Accessing font styles

- [fontStyleAtIndex:range:](fontstyleatindex_range_.md) — Returns the font style and range at the index position.
- [FontStyle](fontstyle.md) — Font styles for caption text.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [decorationAtIndex:range:](decorationatindex_range_.md) — Returns the text decoration at the index position.
- [Decoration](decoration.md) — Text decorations for caption text.
