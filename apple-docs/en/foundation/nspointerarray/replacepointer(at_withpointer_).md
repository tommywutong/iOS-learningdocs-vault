---
title: 'replacePointer(at:withPointer:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/replacepointer(at:withpointer:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/replacepointer(at:withpointer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/replacepointer%28at%3Awithpointer%3A%29.json'
content_hash: 'sha256:dc5c8766c3576568'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# replacePointer(at:withPointer:)

<sub>Instance Method</sub>

Replaces the pointer at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacePointer(at index: Int, withPointer item: UnsafeMutableRawPointer?)
```

## Parameters

- `index` — The index of an element in the receiver. This value must be less than the [count](count.md) of the receiver.

- `item` — The item with which to replace the element at `index`. This value may be `NULL`.

## See Also

### Managing the Collection

- [count](count.md) — The number of elements in the receiver.
- [allObjects](allobjects.md) — All the objects in the receiver.
- [- pointerAtIndex:](<pointer(at_).md>) — Returns the pointer at a given index.
- [- addPointer:](<addpointer(__).md>) — Adds a given pointer to the receiver.
- [- removePointerAtIndex:](<removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
