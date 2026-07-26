---
title: endSubelementIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswhosespecifier/endsubelementindex
source_url: 'https://developer.apple.com/documentation/foundation/nswhosespecifier/endsubelementindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswhosespecifier/endsubelementindex.json'
content_hash: 'sha256:5eb09f8d74c984a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSWhoseSpecifier](../nswhosespecifier.md)

# endSubelementIndex

<sub>Instance Property</sub>

Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.

<sub>Mac Catalyst, macOS</sub>

```swift
var endSubelementIndex: Int { get set }
```

## Parameters

- `index` — The index position of the end sub-element.

## Discussion

Used only if the end sub-element identifier is `NSIndexSubelement`.

## See Also

### Accessing information about a whose specifier

- [endSubelementIdentifier](endsubelementidentifier.md) — Sets the end sub-element identifier for the specifier to the value of a given sub-element.
- [startSubelementIdentifier](startsubelementidentifier.md) — Returns the start sub-element identifier for the receiver.
- [startSubelementIndex](startsubelementindex.md) — Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [test](test.md) — Returns the test object encapsulated by the receiver.
