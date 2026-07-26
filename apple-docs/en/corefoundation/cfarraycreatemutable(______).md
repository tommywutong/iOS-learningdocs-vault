---
title: 'CFArrayCreateMutable(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraycreatemutable(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycreatemutable(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycreatemutable%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d430b3308150c89b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCreateMutable(_:_:_:)

<sub>Function</sub>

Creates a new empty mutable array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayCreateMutable(_ allocator: CFAllocator!, _ capacity: CFIndex, _ callBacks: UnsafePointer<CFArrayCallBacks>!) -> CFMutableArray!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new array and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new array. The array starts empty and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. The value must not be negative.

- `callBacks` — A pointer to a [CFArrayCallBacks](cfarraycallbacks.md) structure initialized with the callbacks for the array to use on each value in the array. A copy of the contents of the callbacks structure is made, so that a pointer to a structure on the stack can be passed in or can be reused for multiple array creations. If the array contains CFType objects only, then pass [kCFTypeArrayCallBacks](kcftypearraycallbacks.md) to use the default callback functions. This parameter may be `NULL`, which is treated as if a valid structure of version `0` with all fields `NULL` had been passed in. If any of the fields are not valid pointers to functions of the correct type, or this parameter is not a valid pointer to a `CFArrayCallBacks` structure, the behavior is undefined. If any value put into the array is not one understood by one of the callback functions, the behavior when that callback function is used is undefined.

## Return Value

A new mutable array, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
