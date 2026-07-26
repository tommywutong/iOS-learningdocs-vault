---
title: 'decorationAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/decorationatindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/decorationatindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/decorationatindex%3Arange%3A.json'
content_hash: 'sha256:842afc0f4a9fa895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# decorationAtIndex:range:

<sub>Instance Method</sub>

Returns the text decoration at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (AVCaptionDecoration) decorationAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer to store the range to which the returned decoration applies.

## Return Value

The text decoration.

## See Also

### Accessing font styles

- [fontStyleAtIndex:range:](fontstyleatindex_range_.md) — Returns the font style and range at the index position.
- [FontStyle](fontstyle.md) — Font styles for caption text.
- [fontWeightAtIndex:range:](fontweightatindex_range_.md) — Returns the font weight and range at the index position.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [Decoration](decoration.md) — Text decorations for caption text.
