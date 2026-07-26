---
title: 'CFSetGetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetgetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:0f0b832d956d97a6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetValue(_:_:)

<sub>Function</sub>

Obtains a specified value from a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetValue(_ theSet: CFSet!, _ value: UnsafeRawPointer!) -> UnsafeRawPointer!
```

## Parameters

- `theSet` — The set to examine.

- `value` — The value for which to search in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

## Return Value

A pointer to the requested value, or `NULL` if the value is not in `theSet`. If the value is a Core Foundation object, Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Since this function uses the equal callback, `value` all elements in the set must be understood by the equal callback. Depending on the implementation of the equal callback specified when creating `theSet`, the value returned may not have the same pointer equality as `value`.

## See Also

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.
