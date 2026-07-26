---
title: minor
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeaconidentityconstraint/minor
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint/minor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentityconstraint/minor.json'
content_hash: 'sha256:857d640dadb68c08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md)

# minor

<sub>Instance Property</sub>

The constraint’s value for the minor identity characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var minor: UInt16? { get }
```

## Discussion

The minor characteristic is optional. If it’s present, a beacon’s minor value needs to match the constraint’s minor value to represent a match. If the constraint has no minor value, it acts as a wildcard and matches any minor value.

## See Also

### Getting the beacon identity

- [major](major.md) — The constraint’s value for the major identity characteristic.
