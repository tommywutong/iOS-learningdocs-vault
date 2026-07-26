---
title: 'CFArrayInsertValueAtIndex(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayinsertvalueatindex(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayinsertvalueatindex(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayinsertvalueatindex%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c48586cfdcaff7b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayInsertValueAtIndex(_:_:_:)

<sub>Function</sub>

Inserts a value into an array at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayInsertValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!)
```

## Parameters

- `theArray` — The array into which `value` is inserted. If `theArray` is a fixed-capacity array and it is full before this operation, the behavior is undefined.

- `idx` — The index at which to insert `value`. The index must be in the range `0` to `N` inclusive, where `N` is the count of `theArray` before the operation. If the index is the same as the count of `theArray`, this function has the same effect as [CFArrayAppendValue](<cfarrayappendvalue(____).md>).

- `value` — The value to insert into `theArray`. The value is retained by `theArray` using the retain callback provided when `theArray` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined.

## Discussion

The `value` parameter is assigned to the index `idx`, and all values in `theArray` with equal and larger indices have their indices increased by one.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
