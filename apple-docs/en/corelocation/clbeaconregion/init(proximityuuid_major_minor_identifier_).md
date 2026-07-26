---
title: 'init(proximityUUID:major:minor:identifier:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clbeaconregion/init(proximityuuid:major:minor:identifier:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/init(proximityuuid:major:minor:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/init%28proximityuuid%3Amajor%3Aminor%3Aidentifier%3A%29.json'
content_hash: 'sha256:56d1d08263bcb433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# init(proximityUUID:major:minor:identifier:)

<sub>Initializer</sub>

Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value.

> [!warning] Deprecated
> Use [- initWithUUID:major:minor:identifier:](<init(uuid_major_minor_identifier_)-24h7w.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(proximityUUID: UUID, major: CLBeaconMajorValue, minor: CLBeaconMinorValue, identifier: String)
```

## Parameters

- `proximityUUID` — The proximity ID of the beacon you’re targeting. This value can’t be `nil`.

- `major` — The major value that you use to identify one or more beacons.

- `minor` — The minor value that you use to identify a specific beacon.

- `identifier` — A unique identifier to associate with the returned region object. You use this identifier to differentiate regions within your app. This value can’t be `nil`.

## Return Value

An initialized beacon region object.

## Discussion

This method creates a region that reports the beacon with the specified `proximityUUID`, `major`, and `minor` values.

## See Also

### Deprecated

- [- initWithProximityUUID:identifier:](<init(proximityuuid_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified UUID. _(deprecated)_
- [- initWithProximityUUID:major:identifier:](<init(proximityuuid_major_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified proximity ID and major value. _(deprecated)_
- [proximityUUID](proximityuuid.md) — The unique ID of the beacons you’re targeting. _(deprecated)_
