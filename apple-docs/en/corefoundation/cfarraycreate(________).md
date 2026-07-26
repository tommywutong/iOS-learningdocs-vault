---
title: 'CFArrayCreate(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraycreate(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycreate(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycreate%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8e574c35a3ea4ea1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCreate(_:_:_:_:)

<sub>Function</sub>

Creates a new immutable array with the given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayCreate(_ allocator: CFAllocator!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!, _ numValues: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>!) -> CFArray!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new array and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `values` — A C array of the pointer-sized values to be in the new array. The values in the new array are ordered in the same order in which they appear in this C array. This value may be `NULL` if `numValues` is `0`. This C array is not changed or freed by this function. If `values` is not a valid pointer to a C array of at least `numValues` elements, the behavior is undefined.

- `numValues` — The number of values to copy from the values C array into the new array. This number will be the count of the new array—it must not be negative or greater than the number of elements in `values`.

- `callBacks` — A pointer to a [CFArrayCallBacks](cfarraycallbacks.md) structure initialized with the callbacks for the array to use on each value in the collection. The retain callback is used within this function, for example, to retain all of the new values from the values C array. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple collection creations. This value may be `NULL`, which is treated as if a valid structure of version `0` with all fields `NULL` had been passed in. Otherwise, if any of the fields are not valid pointers to functions of the correct type, or this value is not a valid pointer to a [CFArrayCallBacks](cfarraycallbacks.md) structure, the behavior is undefined. If any value put into the collection is not one understood by one of the callback functions, the behavior when that callback function is used is undefined. If the collection contains only CFType objects, then pass a pointer to [kCFTypeArrayCallBacks](kcftypearraycallbacks.md) (`&kCFTypeArrayCallBacks`) to use the default callback functions.

## Return Value

A new immutable array containing `numValues` from `values`, or `NULL` if there was a problem creating the object. Ownership follows [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating an Array

- [CFArrayCreateCopy](<cfarraycreatecopy(____).md>) — Creates a new immutable array with the values from another array.
