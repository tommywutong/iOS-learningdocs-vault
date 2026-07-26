---
title: CLMonitor.BeaconIdentityCondition
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/beaconidentitycondition
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition.json'
content_hash: 'sha256:a7625cfc6f81cd84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# CLMonitor.BeaconIdentityCondition

<sub>Structure</sub>

A condition that describes the characteristics of a beacon.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct BeaconIdentityCondition
```

## Overview

Use `CLMonitor.BeaconIdentityCondition` to observe events from beacons based on any combination on their UUID, major, or minor characteristics.

## Relationships

- **Conforms To**: [CLCondition](../clcondition-swift.protocol.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a beacon identity condition

- [init(uuid:)](<beaconidentitycondition/init(uuid_).md>) — Creates a beacon identity condition with the UUID characteristic only, and wildcard values for the major and minor characteristics.
- [init(uuid:major:)](<beaconidentitycondition/init(uuid_major_).md>) — Creates a beacon identity condition with UUID and major characteristics, and a wildcard for the minor characteristic.
- [init(uuid:major:minor:)](<beaconidentitycondition/init(uuid_major_minor_).md>) — Creates a beacon identity condition with UUID, and major and minor characteristics.

### Instance Properties

- [major](beaconidentitycondition/major.md)
- [minor](beaconidentitycondition/minor.md)
- [uuid](beaconidentitycondition/uuid.md)

## See Also

### Monitor conditions

- [CircularGeographicCondition](circulargeographiccondition.md) — A condition that describes a circular geographic area that a center point and radius define.
