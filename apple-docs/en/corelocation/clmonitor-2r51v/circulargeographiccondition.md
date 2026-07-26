---
title: CLMonitor.CircularGeographicCondition
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/circulargeographiccondition
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/circulargeographiccondition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/circulargeographiccondition.json'
content_hash: 'sha256:535fb9aea463fafc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# CLMonitor.CircularGeographicCondition

<sub>Structure</sub>

A condition that describes a circular geographic area that a center point and radius define.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
struct CircularGeographicCondition
```

## Overview

Use `CLMonitor.CircularGeographicCondition` to monitor events that occur in a circular geographic condition that you describe.

## Relationships

- **Conforms To**: [CLCondition](../clcondition-swift.protocol.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a circular geographic condition

- [init(center:radius:)](<circulargeographiccondition/init(center_radius_).md>) — Creates a circular geographic condition with a center point and radius you specify.

### Condition characteristics

- [center](circulargeographiccondition/center.md) — The center point of the condition’s area.
- [radius](circulargeographiccondition/radius.md) — The radius of the condition’s area, in meters.

## See Also

### Monitor conditions

- [BeaconIdentityCondition](beaconidentitycondition.md) — A condition that describes the characteristics of a beacon.
