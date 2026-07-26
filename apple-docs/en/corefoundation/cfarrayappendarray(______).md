---
title: 'CFArrayAppendArray(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayappendarray(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayappendarray(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayappendarray%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cca938fb48bdeb0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayAppendArray(_:_:_:)

<sub>Function</sub>

Adds the values from one array to another array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayAppendArray(_ theArray: CFMutableArray!, _ otherArray: CFArray!, _ otherRange: CFRange)
```

## Parameters

- `theArray` — The array to which values from `otherArray` are added. If `theArray` is a limited-capacity array, adding `otherRange.length` values from `otherArray` must not cause the capacity limit of `theArray` to be exceeded.

- `otherArray` — An array providing the values to be added to `theArray`.

- `otherRange` — The range within `otherArray` from which to add the values to `theArray`. The range must not exceed the index space of `otherArray`.

## Discussion

The new values are retained by `theArray` using the retain callback provided when `theArray` was created. If the values are not of the type expected by the retain callback, the behavior is undefined. The values are assigned to the indices one larger than the previous largest index in `theArray`, and beyond, and the count of `theArray` is increased by `otherRange.length`. The values are assigned new indices in `theArray` from smallest to largest index in the order in which they appear in `otherArray`.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
