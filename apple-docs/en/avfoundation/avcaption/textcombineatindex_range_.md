---
title: 'textCombineAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/textcombineatindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/textcombineatindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/textcombineatindex%3Arange%3A.json'
content_hash: 'sha256:f782cb81738ad920'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# textCombineAtIndex:range:

<sub>Instance Method</sub>

Returns the text combine at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (AVCaptionTextCombine) textCombineAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned text combine applies.

## Return Value

The text combine.

## See Also

### Accessing advanced typography

- [rubyAtIndex:range:](rubyatindex_range_.md) — Returns the ruby text at the index position.
- [Ruby](ruby.md) — An object that presents ruby characters.
- [TextCombine](textcombine.md) — The caption’s supported rendering policy options.
