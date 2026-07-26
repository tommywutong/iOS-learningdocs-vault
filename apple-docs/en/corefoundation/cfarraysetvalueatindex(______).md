---
title: 'CFArraySetValueAtIndex(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraysetvalueatindex(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraysetvalueatindex(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraysetvalueatindex%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4678fb1a06b41c75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArraySetValueAtIndex(_:_:_:)

<sub>Function</sub>

Changes the value at a given index in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArraySetValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex, _ value: UnsafeRawPointer!)
```

## Parameters

- `theArray` — The array in which the value is to be changed.

- `idx` — The index at which to set the new value. The value must not lie outside the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of the array before the operation).

- `value` — The value to set in `theArray`. The value is retained by `theArray` using the retain callback provided when `theArray` was created and the previous value at `idx` is released. If the value is not of the type expected by the retain callback, the behavior is undefined. The indices of other values are not affected.

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
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
