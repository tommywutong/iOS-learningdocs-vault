---
title: 'init(point:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(point:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28point%3A%29.json'
content_hash: 'sha256:b71895b3c2a98a6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(point:)

<sub>Initializer</sub>

Creates a new value object containing the specified Foundation point structure.

<sub>Mac Catalyst, macOS</sub>

```swift
init(point: NSPoint)
```

## Parameters

- `point` — The value for the new object.

## Return Value

A new value object that contains the point information.

## See Also

### Related Documentation

- [NSPoint](../nspoint.md) — A point in a Cartesian coordinate system.

### Working with Foundation Geometry Values

- [+ valueWithSize:](<init(size_).md>) — Creates a new value object containing the specified Foundation size structure.
- [+ valueWithRect:](<init(rect_).md>) — Creates a new value object containing the specified Foundation rectangle structure.
- [pointValue](pointvalue.md) — The Foundation point structure representation of the value.
- [sizeValue](sizevalue.md) — The Foundation size structure representation of the value.
- [rectValue](rectvalue.md) — The Foundation rectangle structure representation of the value.
