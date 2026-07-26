---
title: 'CFArrayRemoveAllValues(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayremoveallvalues(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayremoveallvalues(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayremoveallvalues%28_%3A%29.json'
content_hash: 'sha256:a518a0e79c621d1e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayRemoveAllValues(_:)

<sub>Function</sub>

Removes all the values from an array, making it empty.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayRemoveAllValues(_ theArray: CFMutableArray!)
```

## Parameters

- `theArray` — The array from which all of the values are removed.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayAppendValue](<cfarrayappendvalue(____).md>) — Adds a value to an array giving it the new largest index.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
