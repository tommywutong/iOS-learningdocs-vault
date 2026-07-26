---
title: major
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbeaconidentityconstraint/major
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint/major'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentityconstraint/major.json'
content_hash: 'sha256:5df68bca8366f4f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md)

# major

<sub>Instance Property</sub>

The constraint’s value for the major identity characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var major: UInt16? { get }
```

## Discussion

The major characteristic is optional. If it’s present, a beacon’s major value needs to match the constraint’s major value to represent a match. If the constraint has no major value, it acts as a wildcard and matches any major value. You can specify the major value when initializing the constraint.

## See Also

### Getting the beacon identity

- [minor](minor.md) — The constraint’s value for the minor identity characteristic.
