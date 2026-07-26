---
title: 'initWithUUID:major:minor:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clbeaconidentitycondition/initwithuuid:major:minor:'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentitycondition/initwithuuid:major:minor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentitycondition/initwithuuid%3Amajor%3Aminor%3A.json'
content_hash: 'sha256:f72bd3b3a9ba3185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconIdentityCondition](../clbeaconidentitycondition.md)

# initWithUUID:major:minor:

<sub>Instance Method</sub>

Creates a new beacon identity condition with the identifier, and major and minor values you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid major:(CLBeaconMajorValue) major minor:(CLBeaconMinorValue) minor;
```

## Parameters

- `uuid` — A [UUID](uuid.md) to use as the beacon’s identifier.

- `major` — A [CLBeaconMajorValue](../clbeaconmajorvalue.md) to use as the beacon’s major value.

- `minor` — A [CLBeaconMinorValue](../clbeaconminorvalue.md) to use as the beacon’s minor value.

## See Also

### Creating beacon identity conditions

- [initWithUUID:](initwithuuid_.md) — Creates a new beacon identity condition with the identifier you specify.
- [initWithUUID:major:](initwithuuid_major_.md) — Creates a new beacon identity condition with the identifier and major value you specify.
