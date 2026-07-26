---
title: 'rulerAttributes(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/rulerattributes(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/rulerattributes(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/rulerattributes%28in%3A%29.json'
content_hash: 'sha256:3c6f96e122386641'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# rulerAttributes(in:)

<sub>Instance Method</sub>

Returns the ruler (paragraph) attributes in effect for the characters within the specified range.

<sub>macOS</sub>

```swift
func rulerAttributes(in range: NSRange) -> [NSAttributedString.Key : Any]
```

## Parameters

- `range` — The range.

## Return Value

A dictionary containing the ruler attributes in the range.

## Discussion

The only ruler attribute currently defined is that named by [paragraphStyle](key/paragraphstyle.md). Use this method to obtain attributes that are to be copied or pasted with “copy ruler” operations.

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if any part of `aRange` lies beyond the end of the receiver’s characters.

## See Also

### Getting font attribute information

- [- fontAttributesInRange:](<fontattributes(in_).md>) — Returns the font attributes in effect for the character at the specified location.
