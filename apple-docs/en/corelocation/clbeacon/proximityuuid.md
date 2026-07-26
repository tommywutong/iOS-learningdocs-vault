---
title: proximityUUID
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeacon/proximityuuid
source_url: 'https://developer.apple.com/documentation/corelocation/clbeacon/proximityuuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeacon/proximityuuid.json'
content_hash: 'sha256:f7b358fff3c913db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeacon](../clbeacon.md)

# proximityUUID

<sub>Instance Property</sub>

The proximity ID of the beacon.

> [!warning] Deprecated
> Use [UUID](uuid.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var proximityUUID: UUID { get }
```

## See Also

### Getting the beacon identity

- [UUID](uuid.md) — The UUID that the observed beacon transmitted.
- [major](major.md) — The major value that the observed beacon transmitted.
- [minor](minor.md) — The minor value that the observed beacon transmitted.
