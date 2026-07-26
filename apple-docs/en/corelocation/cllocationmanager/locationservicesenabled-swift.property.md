---
title: locationServicesEnabled
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/locationservicesenabled-swift.property
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/locationservicesenabled-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/locationservicesenabled-swift.property.json'
content_hash: 'sha256:561209b96bf053b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# locationServicesEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether location services are enabled on the device.

> [!warning] Deprecated
> Use the [+ locationServicesEnabled](<locationservicesenabled().md>) class method instead.

<sub>macOS</sub>

```swift
var locationServicesEnabled: Bool { get }
```

## Discussion

In iOS, the user can enable or disable location services using the controls in Settings \> Location Services. In macOS, the user can enable or disable location services from the Security & Privacy system preference.

If this property contains the value [false](../../swift/false.md) and you start location updates anyway, the Core Location framework prompts the user with a confirmation alert asking whether location services should be reenabled.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Properties

- [headingAvailable](headingavailable-swift.property.md) — A Boolean value indicating whether the location manager is able to generate heading-related events. _(deprecated)_
- [purpose](purpose.md) — An app-provided string that describes the reason for using location services. _(deprecated)_
- [rangedRegions](rangedregions.md) — The set of regions currently being tracked using ranging. _(deprecated)_
