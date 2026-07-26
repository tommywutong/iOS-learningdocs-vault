---
title: 'CFArrayAppendValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfarrayappendvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfarrayappendvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfarrayappendvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:2c5dc82c4e116469'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFArrayAppendValue(_:_:)

<sub>Function</sub>

Adds a value to an array giving it the new largest index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFArrayAppendValue(_ theArray: CFMutableArray!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theArray` — The array to which `value` is to be added. If `theArray` is a limited-capacity array and it is full before this operation, the behavior is undefined.

- `value` — A CFType object or a pointer value to add to `theArray`.

## Discussion

The `value` parameter is retained by `theArray` using the retain callback provided when `theArray` was created. If `value` is not of the type expected by the retain callback, the behavior is undefined. The `value` parameter is assigned to the index one larger than the previous largest index and the count of `theArray` is increased by one.

## See Also

### CFMutableArray Miscellaneous Functions

- [CFArrayAppendArray](<cfarrayappendarray(______).md>) — Adds the values from one array to another array.
- [CFArrayCreateMutable](<cfarraycreatemutable(______).md>) — Creates a new empty mutable array.
- [CFArrayCreateMutableCopy](<cfarraycreatemutablecopy(______).md>) — Creates a new mutable array with the values from another array.
- [CFArrayExchangeValuesAtIndices](<cfarrayexchangevaluesatindices(______).md>) — Exchanges the values at two indices of an array.
- [CFArrayInsertValueAtIndex](<cfarrayinsertvalueatindex(______).md>) — Inserts a value into an array at a given index.
- [CFArrayRemoveAllValues](<cfarrayremoveallvalues(__).md>) — Removes all the values from an array, making it empty.
- [CFArrayRemoveValueAtIndex](<cfarrayremovevalueatindex(____).md>) — Removes the value at a given index from an array.
- [CFArrayReplaceValues](<cfarrayreplacevalues(________).md>) — Replaces a range of values in an array.
- [CFArraySetValueAtIndex](<cfarraysetvalueatindex(______).md>) — Changes the value at a given index in an array.
- [CFArraySortValues](<cfarraysortvalues(________).md>) — Sorts the values in an array using a given comparison function.
