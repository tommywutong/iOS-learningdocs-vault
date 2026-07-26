---
title: 'removePointer(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/removepointer(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/removepointer(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/removepointer%28at%3A%29.json'
content_hash: 'sha256:4a1ea36a9dc6ea97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# removePointer(at:)

<sub>Instance Method</sub>

Removes the pointer at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removePointer(at index: Int)
```

## Parameters

- `index` — The index of an element in the receiver. This value must be less than the [count](count.md) of the receiver.

## Discussion

Elements above `index`, including `NULL` values, slide lower.

## See Also

### Managing the Collection

- [count](count.md) — The number of elements in the receiver.
- [allObjects](allobjects.md) — All the objects in the receiver.
- [- pointerAtIndex:](<pointer(at_).md>) — Returns the pointer at a given index.
- [- addPointer:](<addpointer(__).md>) — Adds a given pointer to the receiver.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
