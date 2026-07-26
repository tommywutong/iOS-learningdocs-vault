---
title: 'CFSetGetCountOfValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetgetcountofvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgetcountofvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgetcountofvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:01d74636c13a3281'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetCountOfValue(_:_:)

<sub>Function</sub>

Returns the number of values in a set that match a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetCountOfValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> CFIndex
```

## Parameters

- `theSet` — The set to examine.

- `value` — The value for which to search in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## Return Value

The number of times `value` occurs in `theSet`. By definition, sets can not contain duplicate values, so returns `1` if `value` is contained in `theSet`, otherwise `0`.

## Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## See Also

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.
