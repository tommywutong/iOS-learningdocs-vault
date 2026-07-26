---
title: endSubelementIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswhosespecifier/endsubelementidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nswhosespecifier/endsubelementidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswhosespecifier/endsubelementidentifier.json'
content_hash: 'sha256:9b7fd3b3f50804ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSWhoseSpecifier](../nswhosespecifier.md)

# endSubelementIdentifier

<sub>Instance Property</sub>

Sets the end sub-element identifier for the specifier to the value of a given sub-element.

<sub>Mac Catalyst, macOS</sub>

```swift
var endSubelementIdentifier: NSWhoseSpecifier.SubelementIdentifier { get set }
```

## Parameters

- `subelement` — The end sub-element for the receiver.

## See Also

### Accessing information about a whose specifier

- [endSubelementIndex](endsubelementindex.md) — Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.
- [startSubelementIdentifier](startsubelementidentifier.md) — Returns the start sub-element identifier for the receiver.
- [startSubelementIndex](startsubelementindex.md) — Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [test](test.md) — Returns the test object encapsulated by the receiver.
