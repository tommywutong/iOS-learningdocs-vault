---
title: uuid
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeacon/uuid
source_url: 'https://developer.apple.com/documentation/corelocation/clbeacon/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeacon/uuid.json'
content_hash: 'sha256:03d78724abaa7ded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeacon](../clbeacon.md)

# uuid

<sub>Instance Property</sub>

The UUID that the observed beacon transmitted.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var uuid: UUID { get }
```

## Discussion

The UUID is the most significant beacon identity characteristic.  Multiple beacon can transmit the same UUID.

## See Also

### Getting the beacon identity

- [major](major.md) — The major value that the observed beacon transmitted.
- [minor](minor.md) — The minor value that the observed beacon transmitted.
- [proximityUUID](proximityuuid.md) — The proximity ID of the beacon. _(deprecated)_
