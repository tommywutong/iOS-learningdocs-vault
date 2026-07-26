---
title: 'CFArrayCreateMutableCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraycreatemutablecopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraycreatemutablecopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraycreatemutablecopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8fea5e6c12c2e771'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayCreateMutableCopy(_:_:_:)

<sub>Function</sub>

Creates a new mutable array with the values from another array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayCreateMutableCopy(_ allocator: CFAllocator!, _ capacity: CFIndex, _ theArray: CFArray!) -> CFMutableArray!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new array and its storage for values. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `capacity` — The maximum number of values that can be contained by the new array. The array starts with the same number of values as `theArray` and can grow to this number of values (and it can have less). Pass `0` to specify that the maximum capacity is not limited. If non-`0`, `capacity` must be greater than or equal to the count of `theArray`.

- `theArray` — The array to copy. The pointer values from the array are copied into the new array. However, the values are also retained by the new array.

## Return Value

A new mutable array that contains the same values as `theArray`. The new array has the same count as the `theArray` and uses the same callbacks. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
