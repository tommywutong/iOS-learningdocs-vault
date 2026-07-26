---
title: NSKeyValueChange.insertion
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechange/insertion
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechange/insertion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechange/insertion.json'
content_hash: 'sha256:cc464c08c202ec83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueChange](../nskeyvaluechange.md)

# NSKeyValueChange.insertion

<sub>Case</sub>

Indicates that an object has been inserted into the to-many relationship that is being observed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case insertion
```

## See Also

### Constants

- [NSKeyValueChangeSetting](setting.md) — Indicates that the value of the observed key path was set to a new value. This change can occur when observing an attribute of an object, as well as properties that specify to-one and to-many relationships.
- [NSKeyValueChangeRemoval](removal.md) — Indicates that an object has been removed from the to-many relationship that is being observed.
- [NSKeyValueChangeReplacement](replacement.md) — Indicates that an object has been replaced in the to-many relationship that is being observed.
