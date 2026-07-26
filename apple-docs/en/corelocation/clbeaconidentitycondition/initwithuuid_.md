---
title: 'initWithUUID:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clbeaconidentitycondition/initwithuuid:'
source_url: 'https://developer.apple.com/documentation/corelocation/clbeaconidentitycondition/initwithuuid:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbeaconidentitycondition/initwithuuid%3A.json'
content_hash: 'sha256:a48192eed197ae17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBeaconIdentityCondition](../clbeaconidentitycondition.md)

# initWithUUID:

<sub>Instance Method</sub>

Creates a new beacon identity condition with the identifier you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid;
```

## Parameters

- `uuid` — A [UUID](uuid.md) to use as the beacon’s identifier.

## See Also

### Creating beacon identity conditions

- [initWithUUID:major:](initwithuuid_major_.md) — Creates a new beacon identity condition with the identifier and major value you specify.
- [initWithUUID:major:minor:](initwithuuid_major_minor_.md) — Creates a new beacon identity condition with the identifier, and major and minor values you specify.
