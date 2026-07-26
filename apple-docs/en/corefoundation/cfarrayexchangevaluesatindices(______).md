---
title: 'CFArrayExchangeValuesAtIndices(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayexchangevaluesatindices(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayexchangevaluesatindices(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayexchangevaluesatindices%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4f50fa2e330c982c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayExchangeValuesAtIndices(_:_:_:)

<sub>Function</sub>

Exchanges the values at two indices of an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayExchangeValuesAtIndices(_ theArray: CFMutableArray!, _ idx1: CFIndex, _ idx2: CFIndex)
```

## Parameters

- `theArray` — The array that contains the values to be swapped.

- `idx1` — The index of the value to swap with the value at `idx2`. The index must not exceed the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray` before the operation).

- `idx2` — The index of the value to swap with the value at `idx1`. The index must not exceed the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray` before the operation).

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
