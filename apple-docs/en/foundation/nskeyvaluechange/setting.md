---
title: NSKeyValueChange.setting
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluechange/setting
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluechange/setting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluechange/setting.json'
content_hash: 'sha256:55a5903c2c3fd129'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueChange](../nskeyvaluechange.md)

# NSKeyValueChange.setting

<sub>Case</sub>

Indicates that the value of the observed key path was set to a new value. This change can occur when observing an attribute of an object, as well as properties that specify to-one and to-many relationships.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case setting
```

## See Also

### Constants

- [NSKeyValueChangeInsertion](insertion.md) — Indicates that an object has been inserted into the to-many relationship that is being observed.
- [NSKeyValueChangeRemoval](removal.md) — Indicates that an object has been removed from the to-many relationship that is being observed.
- [NSKeyValueChangeReplacement](replacement.md) — Indicates that an object has been replaced in the to-many relationship that is being observed.
