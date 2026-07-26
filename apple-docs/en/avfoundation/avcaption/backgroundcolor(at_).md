---
title: 'backgroundColor(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/backgroundcolor(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/backgroundcolor(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/backgroundcolor%28at%3A%29.json'
content_hash: 'sha256:3f99912f4148e773'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# backgroundColor(at:)

<sub>Instance Method</sub>

Returns the background color at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func backgroundColor(at index: String.Index) -> (CGColor?, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the background color and range to which it applies.

## See Also

### Accessing colors

- [textColor(at:)](<textcolor(at_).md>) — Returns the text color at the index position.
