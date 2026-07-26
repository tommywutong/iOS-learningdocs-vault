---
title: 'init(rect:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(rect:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(rect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28rect%3A%29.json'
content_hash: 'sha256:aa95318ce34a42d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(rect:)

<sub>Initializer</sub>

Creates a new value object containing the specified Foundation rectangle structure.

<sub>Mac Catalyst, macOS</sub>

```swift
init(rect: NSRect)
```

## Parameters

- `rect` — The value for the new object.

## Return Value

A new value object that contains the data in the `rect` structure.

## See Also

### Related Documentation

- [NSRect](../nsrect.md) — A rectangle.

### Working with Foundation Geometry Values

- [+ valueWithPoint:](<init(point_).md>) — Creates a new value object containing the specified Foundation point structure.
- [+ valueWithSize:](<init(size_).md>) — Creates a new value object containing the specified Foundation size structure.
- [pointValue](pointvalue.md) — The Foundation point structure representation of the value.
- [sizeValue](sizevalue.md) — The Foundation size structure representation of the value.
- [rectValue](rectvalue.md) — The Foundation rectangle structure representation of the value.
