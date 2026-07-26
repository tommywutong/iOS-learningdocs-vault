---
title: 'pointer(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointerarray/pointer(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointerarray/pointer(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointerarray/pointer%28at%3A%29.json'
content_hash: 'sha256:6d09de6dfb514afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPointerArray](../nspointerarray.md)

# pointer(at:)

<sub>Instance Method</sub>

Returns the pointer at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pointer(at index: Int) -> UnsafeMutableRawPointer?
```

## Parameters

- `index` — The index of an element in the receiver. This value must be less than the [count](count.md) of the receiver.

## Return Value

The pointer at `index`.

## Discussion

The returned value may be `NULL`.

## See Also

### Managing the Collection

- [count](count.md) — The number of elements in the receiver.
- [allObjects](allobjects.md) — All the objects in the receiver.
- [- addPointer:](<addpointer(__).md>) — Adds a given pointer to the receiver.
- [- removePointerAtIndex:](<removepointer(at_).md>) — Removes the pointer at a given index.
- [- insertPointer:atIndex:](<insertpointer(__at_).md>) — Inserts a pointer at a given index.
- [- replacePointerAtIndex:withPointer:](<replacepointer(at_withpointer_).md>) — Replaces the pointer at a given index.
- [- compact](<compact().md>) — Removes `NULL` values from the receiver.
