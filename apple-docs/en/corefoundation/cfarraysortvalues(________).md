---
title: 'CFArraySortValues(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarraysortvalues(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarraysortvalues(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarraysortvalues%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0a2a9a2f51e6c015'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArraySortValues(_:_:_:_:)

<sub>Function</sub>

Sorts the values in an array using a given comparison function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArraySortValues(_ theArray: CFMutableArray!, _ range: CFRange, _ comparator: CFComparatorFunction!, _ context: UnsafeMutableRawPointer!)
```

## Parameters

- `theArray` — The array whose values are sorted.

- `range` — The range of values within `theArray` to sort. The range location or end point (defined by the location plus length minus 1) must not lie outside the index space of `theArray` (`0` to `N-1` inclusive, where `N` is the count of `theArray`). The range length must not be negative. The range may be empty (length 0).

- `comparator` — The function with the comparator function type signature that is used in the sort operation to compare the values in `theArray`. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. If there are values in `theArray` that the `comparator` function does not expect or cannot properly compare, the behavior is undefined. The values in the range are sorted from least to greatest according to this function.

- `context` — A pointer-sized program-defined value, which is passed as the third parameter to the `comparator` function, but is otherwise unused by this function. If the context is not what is expected by the `comparator` function, the behavior is undefined.

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
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
