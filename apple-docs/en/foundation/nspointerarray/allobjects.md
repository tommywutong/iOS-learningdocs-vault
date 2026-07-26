---
title: allObjects
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspointerarray/allobjects
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/allobjects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/allobjects.json'
content_hash: 'sha256:ca0430cab646eef3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# allObjects

<sub>Instance Property</sub>

All the objects in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allObjects: [Any] { get }
```

## See Also

### Managing the Collection

- [count](count.md) — The number of elements in the receiver.
- [- pointerAtIndex:](<pointer(at_).md>) — Returns the pointer at a given index.
- [- addPointer:](<addpointer(__).md>) — Adds a given pointer to the receiver.
- [- removePointerAtIndex:](<removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
