---
title: 'CFSetGetValues(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetgetvalues(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgetvalues(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgetvalues%28_%3A_%3A%29.json'
content_hash: 'sha256:67b0eeb558a7c56d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetValues(_:_:)

<sub>Function</sub>

Obtains all values in a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetValues(_ theSet: CFSet!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theSet` — The set to examine.

- `values` — A C array of pointer-sized values to be filled with values from `theSet`. The value must be a valid C array of the appropriate type and of a size at least equal to the count of `theSet`). If the values are Core Foundation objects, ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCount](<cfsetgetcount(__).md>) — Returns the number of values currently in a set.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
