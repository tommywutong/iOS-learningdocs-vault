---
title: major
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeaconregion/major
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconregion/major'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconregion/major.json'
content_hash: 'sha256:0bd8272e1eaec5f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconRegion](../clbeaconregion.md)

# major

<sub>Instance Property</sub>

The major value from the beacon identity constraint that defines the beacon region.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@NSCopying var major: NSNumber? { get }
```

## Discussion

If you don’t specify a [major](../clbeaconidentityconstraint/major.md) value for the beacon, the value of this property is `nil`. Operations that compare a beacon’s identity characteristics with the constraint’s characteristics ignore the `major` value if this property is `nil`.

## See Also

### Getting the beacon identity

- [UUID](uuid.md) — The UUID value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [minor](minor.md) — The minor value from the beacon identity constraint that defines the beacon region. _(deprecated)_
- [beaconIdentityConstraint](beaconidentityconstraint.md) — The beacon identity constraint that defines the beacon region. _(deprecated)_
