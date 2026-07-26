---
title: 'backgroundColorAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/backgroundcoloratindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/backgroundcoloratindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/backgroundcoloratindex%3Arange%3A.json'
content_hash: 'sha256:26ecfd439138618e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# backgroundColorAtIndex:range:

<sub>Instance Method</sub>

Returns the background color at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (CGColorRef) backgroundColorAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned background color applies.

## Return Value

The background color.

## See Also

### Accessing colors

- [textColorAtIndex:range:](textcoloratindex_range_.md) — Returns the text color at the index position.
