---
title: 'CFBagCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfbagcreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b9fc67c81779102b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFBagCreate(_:_:_:_:)

<sub>Function</sub>

Creates an immutable bag containing specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFBagCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFBagCallBacks>!) -> CFBag!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new bag and its storage for values. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `values` — A C array of the pointer-sized values to be in the new bag. This parameter may be `NULL` if the `numValues` parameter is 0. The C array is not changed or freed by this function. `values` must be a valid pointer to a C array of at least `numValues` elements.

- `numValues` — The number of values to copy from the `values` C array in the new CFBag object. If the number is negative or is greater than the actual number of values, the behavior is undefined.

- `callBacks` — A pointer to a [CFBagCallBacks](cfbagcallbacks.md) structure initialized with the callbacks to use to retain, release, describe, and compare values in the bag. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple collection creations. This parameter may be `NULL`, which is treated as if a valid structure of version 0 with all fields `NULL` had been passed in. Otherwise, if any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a [CFBagCallBacks](cfbagcallbacks.md) structure, the behavior is undefined. If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined. If the collection contains CFType objects only, then pass [kCFTypeBagCallBacks](kcftypebagcallbacks.md) as this parameter to use the default callback functions.

## Return Value

A new bag, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Bag

- [CFBagCreateCopy](<cfbagcreatecopy(____).md>) — Creates an immutable bag with the values of another bag.
