---
title: 'textCombine(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/textcombine(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/textcombine(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/textcombine%28at%3A%29.json'
content_hash: 'sha256:95959a904130eb5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# textCombine(at:)

<sub>Instance Method</sub>

Returns the text combine at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func textCombine(at index: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the text combine color and range to which it applies.

## See Also

### Accessing advanced typography

- [ruby(at:)](<ruby(at_).md>) — Returns the ruby text at the index position.
- [Ruby](ruby.md) — An object that presents ruby characters.
- [TextCombine](textcombine.md) — The caption’s supported rendering policy options.
