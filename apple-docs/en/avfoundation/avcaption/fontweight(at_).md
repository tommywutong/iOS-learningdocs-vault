---
title: 'fontWeight(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/fontweight(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/fontweight(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/fontweight%28at%3A%29.json'
content_hash: 'sha256:5321320a98ab7a15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# fontWeight(at:)

<sub>Instance Method</sub>

Returns the font weight and range at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func fontWeight(at index: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the font weight and range to which it applies.

## See Also

### Accessing font styles

- [fontStyle(at:)](<fontstyle(at_).md>) — Returns the font style and range at the index position.
- [FontStyle](fontstyle.md) — Font styles for caption text.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [decoration(at:)](<decoration(at_).md>) — Returns the text decoration at the index position.
- [Decoration](decoration.md) — Text decorations for caption text.
