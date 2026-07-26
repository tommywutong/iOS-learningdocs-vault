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
doc_path: /documentation/corelocation/clbeaconregion/proximityuuid
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/proximityuuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/proximityuuid.json'
content_hash: 'sha256:e5ff8b3f2a77a3b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# proximityUUID

<sub>Instance Property</sub>

The unique ID of the beacons you’re targeting.

> [!warning] Deprecated
> Use [UUID](uuid.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var proximityUUID: UUID { get }
```

## Discussion

Typically, the UUID is unique to your company and is the same for all of the beacons that you install. Use the [major](major.md) and [minor](minor.md) values to differentiate the beacons in your installation.

## See Also

### Deprecated

- [- initWithProximityUUID:identifier:](<init(proximityuuid_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified UUID. _(deprecated)_
- [- initWithProximityUUID:major:identifier:](<init(proximityuuid_major_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified proximity ID and major value. _(deprecated)_
- [- initWithProximityUUID:major:minor:identifier:](<init(proximityuuid_major_minor_identifier_).md>) — Creates and returns a region object that targets a beacon with the specified proximity ID, major value, and minor value. _(deprecated)_
