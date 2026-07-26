---
title: 'CFSetContainsValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetcontainsvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcontainsvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcontainsvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:33f15961c883ec90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetContainsValue(_:_:)

<sub>Function</sub>

Returns a Boolean that indicates whether a set contains a given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetContainsValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> Bool
```

## Parameters

- `theSet` — The set to search.

- `value` — The value to match in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## Return Value

`true` if `value` is contained in `theSet`, otherwise `false`.

## Discussion

This function uses the equal callback. `value` and all elements in the set must be understood by the equal callback.

## See Also

### Examining a Set

- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.
