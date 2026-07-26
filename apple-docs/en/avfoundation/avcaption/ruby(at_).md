---
title: 'ruby(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/ruby(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/ruby(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/ruby%28at%3A%29.json'
content_hash: 'sha256:ce67a92d640b6fd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# ruby(at:)

<sub>Instance Method</sub>

Returns the ruby text at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func ruby(at index: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the ruby text and range to which it applies.

## See Also

### Accessing advanced typography

- [Ruby](ruby.md) — An object that presents ruby characters.
- [textCombine(at:)](<textcombine(at_).md>) — Returns the text combine at the index position.
- [TextCombine](textcombine.md) — The caption’s supported rendering policy options.
