---
title: 'CFCharacterSetUnion(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetunion(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetunion(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetunion%28_%3A_%3A%29.json'
content_hash: 'sha256:28bac78c984aace0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetUnion(_:_:)

<sub>Function</sub>

Forms the union of two character sets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetUnion(_ theSet: CFMutableCharacterSet!, _ theOtherSet: CFCharacterSet!)
```

## Parameters

- `theSet` — The source character set, modified by union with `theOtherSet`.

- `theOtherSet` — The character set with which the union is formed.

## See Also

### Logical Operations

- [CFCharacterSetIntersect](<cfcharactersetintersect(____).md>) — Forms an intersection of two character sets.
- [CFCharacterSetInvert](<cfcharactersetinvert(__).md>) — Inverts the content of a given character set.
