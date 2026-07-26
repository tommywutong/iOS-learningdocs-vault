---
title: rangedBeaconConstraints
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/rangedbeaconconstraints
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/rangedbeaconconstraints'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/rangedbeaconconstraints.json'
content_hash: 'sha256:fb5f4d98b6a87f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# rangedBeaconConstraints

<sub>Instance Property</sub>

The set of beacon constraints currently being tracked using ranging.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var rangedBeaconConstraints: Set<CLBeaconIdentityConstraint> { get }
```

## See Also

### Performing beacon ranging

- [- startRangingBeaconsSatisfyingConstraint:](<startrangingbeacons(satisfying_).md>) — Starts the delivery of notifications for the specified beacon constraints.
- [- stopRangingBeaconsSatisfyingConstraint:](<stoprangingbeacons(satisfying_).md>) — Stops the delivery of notifications for the specified beacon constraints.
