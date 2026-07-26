---
title: 'textColorAtIndex:range:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcaption/textcoloratindex:range:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaption/textcoloratindex:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaption/textcoloratindex%3Arange%3A.json'
content_hash: 'sha256:09cfd36d1fa7fb71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaption](../avcaption.md)

# textColorAtIndex:range:

<sub>Instance Method</sub>

Returns the text color at the index position.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```objc
- (CGColorRef) textColorAtIndex:(NSInteger) index range:(NSRange *) outRange;
```

## Parameters

- `index` — A character position in the caption text.

- `outRange` — A pointer that stores the range to which the returned text color applies.

## Return Value

The text color.

## See Also

### Accessing colors

- [backgroundColorAtIndex:range:](backgroundcoloratindex_range_.md) — Returns the background color at the index position.
