---
title: CLBeaconIdentityConstraint
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clbeaconidentityconstraint
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentityconstraint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentityconstraint.json'
content_hash: 'sha256:9e573bf55922f697'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBeaconIdentityConstraint

<sub>Class</sub>

Identity characteristics that can match one or more beacons.

> [!warning] Deprecated
> Use [CLBeaconIdentityCondition](clbeaconidentitycondition.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class CLBeaconIdentityConstraint
```

## Overview

A constraint specifies beacon identity characteristics. Use constraints to check for matching beacons by comparing the beacon’s identity characteristics ([UUID](clbeacon/uuid.md), [major](clbeacon/major.md), and [minor](clbeacon/minor.md)) to those in the constraint.

Constraints always specify a UUID value, but the major and minor values are optional. A beacon satisfies the constraint if all three identity characteristics of the beacon match the same characteristic of the constraint. Major and minor characteristics are wildcards if they have no value. A major or minor wildcard value matches any value in the beacon’s corresponding characteristic.

## Relationships

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the beacon identity

- [major](clbeaconidentityconstraint/major.md) — The constraint’s value for the major identity characteristic.
- [minor](clbeaconidentityconstraint/minor.md) — The constraint’s value for the minor identity characteristic.

## See Also

### Classes

- [CLBeaconRegion](clbeaconregion.md) — A region for detecting the presence of iBeacon devices. _(deprecated)_
- [CLCircularRegion](clcircularregion.md) — A circular geographic region that a center point and radius deine. _(deprecated)_
