---
title: trueHeading
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clheading/trueheading
source_url: 'https://developer.apple.com/documentation/corelocation/clheading/trueheading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clheading/trueheading.json'
content_hash: 'sha256:fbe4e2d440d9774b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLHeading](../clheading.md)

# trueHeading

<sub>Instance Property</sub>

The heading (measured in degrees) relative to true north.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var trueHeading: CLLocationDirection { get }
```

## Discussion

The value in this property represents the heading relative to the geographic North Pole. The value `0` means the device is pointed toward true north, `90` means it is pointed due east, `180` means it is pointed due south, and so on. A negative value indicates that the heading could not be determined.

In iOS 3.x and earlier, the value in this property is always measured relative to the top of the device in a portrait orientation, regardless of the device’s actual physical or interface orientation. In iOS 4.0 and later, the value is measured relative to the heading orientation specified by the location manager. For more information, see the [headingOrientation](../cllocationmanager/headingorientation.md) property in [CLLocationManager](../cllocationmanager.md).

> [!important] Important
> This property contains a valid value only if location updates are also enabled for the corresponding location manager object. Because the position of true north is different from the position of magnetic north on the Earth’s surface, Core Location needs the current location of the device to compute the value of this property.

## See Also

### Getting the heading values

- [magneticHeading](magneticheading.md) — The heading (measured in degrees) relative to magnetic north.
- [headingAccuracy](headingaccuracy.md) — The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.
