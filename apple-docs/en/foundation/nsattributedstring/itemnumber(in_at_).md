---
title: 'itemNumber(in:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/itemnumber(in:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/itemnumber(in:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/itemnumber%28in%3Aat%3A%29.json'
content_hash: 'sha256:1beb004a6ed513c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# itemNumber(in:at:)

<sub>Instance Method</sub>

Returns the index of the item at the specified location within the list.

<sub>macOS</sub>

```swift
func itemNumber(in list: NSTextList, at location: Int) -> Int
```

## Parameters

- `list` — The text list.

- `location` — The location of the item.

## Return Value

Returns the index within the list.

## See Also

### Calculating ranges for common elements

- [- rangeOfTextBlock:atIndex:](<range(of_at_)-1wrcp.md>) — Returns the range of the individual text block that contains the specified location.
- [- rangeOfTextList:atIndex:](<range(of_at_)-6um0x.md>) — Returns the range of the specified text list that contains the specified location.
- [- rangeOfTextTable:atIndex:](<range(of_at_)-3fevu.md>) — Returns the range of the specified text table that contains the specified location.
