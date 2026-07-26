---
title: 'init(uuid:major:minor:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition/init(uuid:major:minor:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition/init(uuid:major:minor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/beaconidentitycondition/init%28uuid%3Amajor%3Aminor%3A%29.json'
content_hash: 'sha256:08db28f2fe8be8cc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLMonitor](../../clmonitor-2r51v.md) · [BeaconIdentityCondition](../beaconidentitycondition.md)

# init(uuid:major:minor:)

<sub>Initializer</sub>

Creates a beacon identity condition with UUID, and major and minor characteristics.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(uuid: UUID, major: UInt16, minor: UInt16)
```

## Parameters

- `uuid` — The [NSUUID](../../../foundation/nsuuid.md) that identifies the beacon.

- `major` — The [CLBeaconMajorValue](../../clbeaconmajorvalue.md) that represents the beacon’s major value.

- `minor` — The [CLBeaconMinorValue](../../clbeaconminorvalue.md) that represents the beacon’s minor value.

## See Also

### Creating a beacon identity condition

- [init(uuid:)](<init(uuid_).md>) — Creates a beacon identity condition with the UUID characteristic only, and wildcard values for the major and minor characteristics.
- [init(uuid:major:)](<init(uuid_major_).md>) — Creates a beacon identity condition with UUID and major characteristics, and a wildcard for the minor characteristic.
