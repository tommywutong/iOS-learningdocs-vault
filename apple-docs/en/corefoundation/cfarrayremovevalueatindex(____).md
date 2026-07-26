---
title: 'CFArrayRemoveValueAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayremovevalueatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayremovevalueatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayremovevalueatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:9a7de4d393df2733'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayRemoveValueAtIndex(_:_:)

<sub>Function</sub>

Removes the value at a given index from an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayRemoveValueAtIndex(_ theArray: CFMutableArray!, _ idx: CFIndex)
```

## Parameters

- `theArray` — The array from which the value is removed.

- `idx` — The index of the value to remove. The index must be in the range 0 to N-1 inclusive, where N is the count of `theArray` before the operation.

## Discussion

All values in `theArray` with indices larger than `idx` have their indices decreased by one.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
