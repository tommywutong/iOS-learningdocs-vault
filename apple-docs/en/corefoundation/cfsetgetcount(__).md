---
title: 'CFSetGetCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsetgetcount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetgetcount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetgetcount%28_%3A%29.json'
content_hash: 'sha256:94ab2aea637d3167'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSetGetCount(_:)

<sub>Function</sub>

Returns the number of values currently in a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSetGetCount(_ theSet: CFSet!) -> CFIndex
```

## Parameters

- `theSet` — The set to examine.

## Return Value

The number of values in `theSet`.

## See Also

### Examining a Set

- [CFSetContainsValue](<cfsetcontainsvalue(____).md>) — Returns a Boolean that indicates whether a set contains a given value.
- [CFSetGetCountOfValue](<cfsetgetcountofvalue(____).md>) — Returns the number of values in a set that match a given value.
- [CFSetGetValue](<cfsetgetvalue(____).md>) — Obtains a specified value from a set.
- [CFSetGetValueIfPresent](<cfsetgetvalueifpresent(______).md>) — Reports whether or not a value is in a set, and if it exists returns the value indirectly.
- [CFSetGetValues](<cfsetgetvalues(____).md>) — Obtains all values in a set.
