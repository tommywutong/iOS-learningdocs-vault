---
title: 'rubyAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/rubyatindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/rubyatindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/rubyatindex%3Arange%3A.json'
content_hash: 'sha256:02c6dbd5495d10cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# rubyAtIndex:range:

<sub>Instance Method</sub>

Returns the ruby text at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (AVCaptionRuby *) rubyAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned ruby text applies.

## Return Value

The ruby text.

## See Also

### Accessing advanced typography

- [Ruby](ruby.md) — An object that presents ruby characters.
- [textCombineAtIndex:range:](textcombineatindex_range_.md) — Returns the text combine at the index position.
- [TextCombine](textcombine.md) — The caption’s supported rendering policy options.
