---
title: 'init(uuid:major:minor:identifier:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clbeaconregion/init(uuid:major:minor:identifier:)-24h7w'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/init(uuid:major:minor:identifier:)-24h7w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/init%28uuid%3Amajor%3Aminor%3Aidentifier%3A%29-24h7w.json'
content_hash: 'sha256:c907e5eb13f0c6da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# init(uuid:major:minor:identifier:)

<sub>Initializer</sub>

Creates and returns a region object that targets beacons with the specified UUID, and major and minor values.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(uuid: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)
```

## Parameters

- `uuid` — A [NSUUID](../../foundation/nsuuid.md) that identifies the beacons to target.

- `major` — The [CLBeaconMajorValue](../clbeaconmajorvalue.md) that characterizes beacons for this region to target.

- `minor` — The [CLBeaconMinorValue](../clbeaconminorvalue.md) that characterizes beacons for this region to target.

- `identifier` — A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil.`

## See Also

### Creating a beacon region

- [- initWithBeaconIdentityConstraint:identifier:](<init(beaconidentityconstraint_identifier_).md>) — Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints. _(deprecated)_
- [- initWithUUID:identifier:](<init(uuid_identifier_)-6hg8v.md>) — Creates and returns a region object that targets beacons with the specified UUID. _(deprecated)_
- [- initWithUUID:major:identifier:](<init(uuid_major_identifier_)-8ur0j.md>) — Creates and returns a region object that targets beacons with the specified UUID and major value. _(deprecated)_
- [CLBeaconMajorValue](../clbeaconmajorvalue.md) — The most significant value in a beacon.
- [CLBeaconMinorValue](../clbeaconminorvalue.md) — The least significant value in a beacon.
