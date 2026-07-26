---
title: 'textColor(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/textcolor(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/textcolor(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/textcolor%28at%3A%29.json'
content_hash: 'sha256:b369ffb160fdb26b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# textColor(at:)

<sub>Instance Method</sub>

Returns the text color at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@nonobjc func textColor(at index: String.Index) -> (CGColor?, Range<String.Index>)
```

## Parameters

- `index` — A character position in the caption text.

## Return Value

A tuple that contains the text color and range to which it applies.

## See Also

### Accessing colors

- [backgroundColor(at:)](<backgroundcolor(at_).md>) — Returns the background color at the index position.
