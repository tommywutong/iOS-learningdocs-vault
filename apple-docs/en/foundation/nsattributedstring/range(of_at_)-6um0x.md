---
title: 'range(of:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/range(of:at:)-6um0x'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/range(of:at:)-6um0x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/range%28of%3Aat%3A%29-6um0x.json'
content_hash: 'sha256:d18518bb476cfbc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# range(of:at:)

<sub>Instance Method</sub>

Returns the range of the specified text list that contains the specified location.

<sub>macOS</sub>

```swift
func range(of list: NSTextList, at location: Int) -> NSRange
```

## Parameters

- `list` — The text list.

- `location` — The location in the text list.

## Return Value

The range of the given text list containing the location.

## See Also

### Calculating ranges for common elements

- [- itemNumberInTextList:atIndex:](<itemnumber(in_at_).md>) — Returns the index of the item at the specified location within the list.
- [- rangeOfTextBlock:atIndex:](<range(of_at_)-1wrcp.md>) — Returns the range of the individual text block that contains the specified location.
- [- rangeOfTextTable:atIndex:](<range(of_at_)-3fevu.md>) — Returns the range of the specified text table that contains the specified location.
