---
title: 'decoration(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/decoration(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/decoration(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/decoration%28at%3A%29.json'
content_hash: 'sha256:fadc3756411671ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# decoration(at:)

<sub>Instance Method</sub>

Returns the text decoration at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func decoration(at index: String.Index) -> (AVCaption.Decoration, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the text decoration and range to which it applies.

## See Also

### Accessing font styles

- [fontStyle(at:)](<fontstyle(at_).md>) — Returns the font style and range at the index position.
- [FontStyle](fontstyle.md) — Font styles for caption text.
- [fontWeight(at:)](<fontweight(at_).md>) — Returns the font weight and range at the index position.
- [FontWeight](fontweight.md) — Font weights for a caption.
- [Decoration](decoration.md) — Text decorations for caption text.
