---
title: count
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerarray/count
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/count.json'
content_hash: 'sha256:fea84606f0f645af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# count

<sub>Instance Property</sub>

The number of elements in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get set }
```

## Discussion

If you increase the `count`, `NULL` values are added. If you decrease the `count`, elements at indexes `count` and greater are removed.

## See Also

### Managing the Collection

- [allObjects](allobjects.md) — All the objects in the receiver.
- [- pointerAtIndex:](<pointer(at_).md>) — Returns the pointer at a given index.
- [- addPointer:](<addpointer(__).md>) — Adds a given pointer to the receiver.
- [- removePointerAtIndex:](<removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
