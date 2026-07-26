---
title: 'initWithUUID:major:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clbeaconidentitycondition/initwithuuid:major:'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentitycondition/initwithuuid:major:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentitycondition/initwithuuid%3Amajor%3A.json'
content_hash: 'sha256:ed9b08cf351a2e44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconIdentityCondition](../clbeaconidentitycondition.md)

# initWithUUID:major:

<sub>Instance Method</sub>

Creates a new beacon identity condition with the identifier and major value you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid major:(CLBeaconMajorValue) major;
```

## Parameters

- `uuid` — A [UUID](uuid.md) to use as the beacon’s identifier.

- `major` — A [CLBeaconMajorValue](../clbeaconmajorvalue.md) to use as the beacon’s major value.

## See Also

### Creating beacon identity conditions

- [initWithUUID:](initwithuuid_.md) — Creates a new beacon identity condition with the identifier you specify.
- [initWithUUID:major:minor:](initwithuuid_major_minor_.md) — Creates a new beacon identity condition with the identifier, and major and minor values you specify.
