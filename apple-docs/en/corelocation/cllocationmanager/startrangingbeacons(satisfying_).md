---
title: 'startRangingBeacons(satisfying:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/startrangingbeacons(satisfying:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startrangingbeacons(satisfying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startrangingbeacons%28satisfying%3A%29.json'
content_hash: 'sha256:387c1b0d2f118947'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startRangingBeacons(satisfying:)

<sub>Instance Method</sub>

Starts the delivery of notifications for the specified beacon constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func startRangingBeacons(satisfying constraint: CLBeaconIdentityConstraint)
```

## Parameters

- `constraint` — A [CLBeaconIdentityConstraint](../clbeaconidentityconstraint.md) constraint.

## See Also

### Performing beacon ranging

- [- stopRangingBeaconsSatisfyingConstraint:](<stoprangingbeacons(satisfying_).md>) — Stops the delivery of notifications for the specified beacon constraints.
- [rangedBeaconConstraints](rangedbeaconconstraints.md) — The set of beacon constraints currently being tracked using ranging.
