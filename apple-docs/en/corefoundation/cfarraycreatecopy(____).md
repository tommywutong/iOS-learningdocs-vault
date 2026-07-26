---
title: 'CFArrayCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraycreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:be29246e3757e455'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCreateCopy(_:_:)

<sub>Function</sub>

Creates a new immutable array with the values from another array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayCreateCopy(_ allocator: CFAllocator!, _ theArray: CFArray!) -> CFArray!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new array and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `theArray` — The array to copy.

## Return Value

A new CFArray object that contains the same values as `theArray`. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The pointer values from `theArray` are copied into the new array; the values are also retained by the new array. The count of the new array is the same as `theArray`. The new array uses the same callbacks as `theArray`.

## See Also

### Creating an Array

- [CFArrayCreate](<cfarraycreate(________).md>) — Creates a new immutable array with the given values.
