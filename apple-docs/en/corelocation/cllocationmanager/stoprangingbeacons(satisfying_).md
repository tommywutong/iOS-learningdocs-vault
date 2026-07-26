---
title: 'stopRangingBeacons(satisfying:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/stoprangingbeacons(satisfying:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/stoprangingbeacons(satisfying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/stoprangingbeacons%28satisfying%3A%29.json'
content_hash: 'sha256:60208e1bcccb4bb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# stopRangingBeacons(satisfying:)

<sub>Instance Method</sub>

Stops the delivery of notifications for the specified beacon constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func stopRangingBeacons(satisfying constraint: CLBeaconIdentityConstraint)
```

## Parameters

- `constraint` — A [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md) constraint.

## See Also

### Performing beacon ranging

- [- startRangingBeaconsSatisfyingConstraint:](<startrangingbeacons(satisfying_).md>) — Starts the delivery of notifications for the specified beacon constraints.
- [rangedBeaconConstraints](rangedbeaconconstraints.md) — The set of beacon constraints currently being tracked using ranging.
