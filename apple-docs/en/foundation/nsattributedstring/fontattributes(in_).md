---
title: 'fontAttributes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/fontattributes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/fontattributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/fontattributes%28in%3A%29.json'
content_hash: 'sha256:420fdeb545ba1ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# fontAttributes(in:)

<sub>Instance Method</sub>

Returns the font attributes in effect for the character at the specified location.

<sub>macOS</sub>

```swift
func fontAttributes(in range: NSRange) -> [NSAttributedString.Key : Any]
```

## Parameters

- `range` — The range.

## Return Value

A dictionary containing the font attributes for the range.

## Discussion

The dictionary attributes are all those listed in `Character Attributes`, except [link](key/link.md), [paragraphStyle](key/paragraphstyle.md), and [attachment](key/attachment.md).

Use this method to obtain font attributes that are to be copied or pasted with “copy font” operations.

Raises an `NSRangeException` if any part of `aRange` lies beyond the end of the receiver’s characters.

## See Also

### Getting font attribute information

- [- rulerAttributesInRange:](<rulerattributes(in_).md>) — Returns the ruler (paragraph) attributes in effect for the characters within the specified range.
