---
title: 'init(uuid:major:identifier:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clbeaconregion/init(uuid:major:identifier:)-8ur0j'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/init(uuid:major:identifier:)-8ur0j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/init%28uuid%3Amajor%3Aidentifier%3A%29-8ur0j.json'
content_hash: 'sha256:b2f18b6703a2b165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# init(uuid:major:identifier:)

<sub>Initializer</sub>

Creates and returns a region object that targets beacons with the specified UUID and major value.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(uuid: UUID, major: CLBeaconMajorValue, identifier: String)
```

## Parameters

- `uuid` — A [NSUUID](../../foundation/nsuuid.md) that identifies the beacons to target.

- `major` — The [CLBeaconMajorValue](../clbeaconmajorvalue.md) that characterizes beacons for this region to target.

- `identifier` — A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil.`

## See Also

### Creating a beacon region

- [- initWithBeaconIdentityConstraint:identifier:](<init(beaconidentityconstraint_identifier_).md>) — Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints. _(deprecated)_
- [- initWithUUID:identifier:](<init(uuid_identifier_)-6hg8v.md>) — Creates and returns a region object that targets beacons with the specified UUID. _(deprecated)_
- [- initWithUUID:major:minor:identifier:](<init(uuid_major_minor_identifier_)-24h7w.md>) — Creates and returns a region object that targets beacons with the specified UUID, and major and minor values. _(deprecated)_
- [CLBeaconMajorValue](../clbeaconmajorvalue.md) — The most significant value in a beacon.
- [CLBeaconMinorValue](../clbeaconminorvalue.md) — The least significant value in a beacon.
