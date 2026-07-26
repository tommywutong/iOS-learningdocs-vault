---
title: 'CFSetGetValueIfPresent(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetgetvalueifpresent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgetvalueifpresent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgetvalueifpresent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1418f56fda2efd95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetValueIfPresent(_:_:_:)

<sub>Function</sub>

Reports whether or not a value is in a set, and if it exists returns the value indirectly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetValueIfPresent(_ theSet: CFSet!, _ candidate: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

## Parameters

- `theSet` — The set to examine.

- `candidate` — The value for which to search in `theSet`. Comparisons are made using the equal callback provided when `theSet` was created. If the equal callback was `NULL`, pointer equality (in C, ==) is used.

- `value` — Upon return contains the matching value if it exists in `theSet`, otherwise `NULL`. If the value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Return Value

`true` if `value` exists in `theSet`, otherwise `false`.

## Discussion

This function uses the equal callback. `candidate` and all elements in the set must be understood by the equal callback. Depending on the implementation of the equal callback specified when creating `theSet`, the value returned in `value` may not have the same pointer equality as `candidate`.

## See Also

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.
