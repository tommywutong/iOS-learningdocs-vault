---
title: 'CFCharacterSetIntersect(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetintersect(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetintersect(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetintersect%28_%3A_%3A%29.json'
content_hash: 'sha256:f131e046a48663ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetIntersect(_:_:)

<sub>Function</sub>

Forms an intersection of two character sets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetIntersect(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

## Parameters

- `theSet` — The source character set, modified by intersection with `theOtherSet`.

- `theOtherSet` — The character set with which the intersection is formed.

## See Also

### Logical Operations

- [CFCharacterSetInvert](<cfcharactersetinvert(__).md>) — Inverts the content of a given character set.
- [CFCharacterSetUnion](<cfcharactersetunion(____).md>) — Forms the union of two character sets.
