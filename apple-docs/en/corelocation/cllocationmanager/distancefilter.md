---
title: distanceFilter
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationmanager/distancefilter
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/distancefilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/distancefilter.json'
content_hash: 'sha256:4624c7e3a7f9cc43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# distanceFilter

<sub>Instance Property</sub>

The minimum distance in meters the device must move horizontally before an update event is generated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var distanceFilter: CLLocationDistance { get set }
```

## Discussion

This location manager measures this relative to the previously delivered location. Specify the value [kCLDistanceFilterNone](../kcldistancefilternone.md) to receive notifications for all movements. The default value of this property is [kCLDistanceFilterNone](../kcldistancefilternone.md).

Use this property only in conjunction with the Standard location services and not with the Significant-change or Visits services.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Specifying distance and accuracy

- [CLLocationDistanceMax](../cllocationdistancemax.md) — A constant indicating the maximum distance.
- [kCLDistanceFilterNone](../kcldistancefilternone.md) — A constant indicating that all movement should be reported.
- [CLLocationDistance](../cllocationdistance.md) — A distance in meters from an existing location.
- [desiredAccuracy](desiredaccuracy.md) — The accuracy of the location data that your app wants to receive.
- [CLLocationAccuracy](../cllocationaccuracy.md) — The accuracy of a geographical coordinate.
