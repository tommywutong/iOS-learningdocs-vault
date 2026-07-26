---
title: uuid
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeaconregion/uuid
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/uuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/uuid.json'
content_hash: 'sha256:ae3b9c3f842d2a0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# uuid

<sub>Instance Property</sub>

The UUID value from the beacon identity constraint that defines the beacon region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var uuid: UUID { get }
```

## Discussion

Typically, the UUID is unique to your company and is the same for all of the beacons that you install. Use the [major](major.md) and [minor](minor.md) values to differentiate the beacons in your installation.

## See Also

### Getting the beacon identity

- [major](major.md) — The major value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [minor](minor.md) — The minor value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [beaconIdentityConstraint](beaconidentityconstraint.md) — The beacon identity constraint that defines the beacon region. _(deprecated)_
