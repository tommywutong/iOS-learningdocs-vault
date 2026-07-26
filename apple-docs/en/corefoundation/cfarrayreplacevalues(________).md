---
title: 'CFArrayReplaceValues(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayreplacevalues(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayreplacevalues(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayreplacevalues%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:06d0a2db7c44ea34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayReplaceValues(_:_:_:_:)

<sub>Function</sub>

Replaces a range of values in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayReplaceValues(_ theArray: CFMutableArray!, _ range: CFRange, _ newValues: UnsafeMutablePointer<UnsafeRawPointer?>!, _ newCount: CFIndex)
```

## Parameters

- `theArray` — The array in which some values are to be replaced. If this parameter is not a valid CFMutableArray object, the behavior is undefined.

- `range` — The range of values within `theArray` to replace. The range location or end point (defined by the location plus length minus 1) must not lie outside the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray`). The range length must not be negative. The range may be empty (length 0), in which case the new values are merely inserted at the range location.

- `newValues` — A C array of the pointer-sized values to be placed into `theArray`. The new values in `theArray` are ordered in the same order in which they appear in this C array. This parameter may be `NULL` if the `newCount` parameter is 0. This C array is not changed or freed by this function. If this parameter is not a valid pointer to a C array of at least `newCount` pointers, the behavior is undefined.

- `newCount` — The number of values to copy from the `newValues` C array into `theArray`. If this parameter is different from the range length, the excess `newCount` values are inserted after the range or the excess range values are deleted. This parameter may be 0, in which case no new values are replaced into `theArray` and the values in the range are simply removed. If this parameter is negative or greater than the number of values actually in the `newValues` C array, the behavior is undefined.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
