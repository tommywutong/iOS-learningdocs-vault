---
title: 'addPointer(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/addpointer(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/addpointer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/addpointer%28_%3A%29.json'
content_hash: 'sha256:a8cf0c27c0a608e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# addPointer(_:)

<sub>Instance Method</sub>

Adds a given pointer to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addPointer(_ pointer: UnsafeMutableRawPointer?)
```

## Parameters

- `pointer` — The pointer to add. This value may be `NULL`.

## Discussion

`pointer` is added at index [count](count.md).

## See Also

### Managing the Collection

- [count](count.md) — The number of elements in the receiver.
- [allObjects](allobjects.md) — All the objects in the receiver.
- [- pointerAtIndex:](<pointer(at_).md>) — Returns the pointer at a given index.
- [- removePointerAtIndex:](<removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
