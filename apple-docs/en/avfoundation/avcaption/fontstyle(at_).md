---
title: 'fontStyle(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/fontstyle(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/fontstyle(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/fontstyle%28at%3A%29.json'
content_hash: 'sha256:53c0f79b559bc7ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# fontStyle(at:)

<sub>Instance Method</sub>

Returns the font style and range at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func fontStyle(at index: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the font style and range to which it applies.

## See Also

### Accessing font styles

- [FontStyle](fontstyle.md) — Font styles for caption text.
- [fontWeight(at:)](<fontweight(at_).md>) — Returns the font weight and range at the index position.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [decoration(at:)](<decoration(at_).md>) — Returns the text decoration at the index position.
- [Decoration](decoration.md) — Text decorations for caption text.
