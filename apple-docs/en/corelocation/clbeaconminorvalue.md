---
title: CLBeaconMinorValue
framework: Core Location
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeaconminorvalue
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconminorvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconminorvalue.json'
content_hash: 'sha256:78004e0f8d3a9983'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBeaconMinorValue

<sub>Type Alias</sub>

The least significant value in a beacon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CLBeaconMinorValue = UInt16
```

## See Also

### Creating a beacon region

- [- initWithBeaconIdentityConstraint:identifier:](<clbeaconregion/init(beaconidentityconstraint_identifier_).md>) — Creates and returns a region object that targets beacons that satisfy the specified beacon identity constraints. _(deprecated)_
- [- initWithUUID:identifier:](<clbeaconregion/init(uuid_identifier_)-6hg8v.md>) — Creates and returns a region object that targets beacons with the specified UUID. _(deprecated)_
- [- initWithUUID:major:identifier:](<clbeaconregion/init(uuid_major_identifier_)-8ur0j.md>) — Creates and returns a region object that targets beacons with the specified UUID and major value. _(deprecated)_
- [- initWithUUID:major:minor:identifier:](<clbeaconregion/init(uuid_major_minor_identifier_)-24h7w.md>) — Creates and returns a region object that targets beacons with the specified UUID, and major and minor values. _(deprecated)_
- [CLBeaconMajorValue](clbeaconmajorvalue.md) — The most significant value in a beacon.
