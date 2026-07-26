---
title: purpose
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/purpose
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/purpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/purpose.json'
content_hash: 'sha256:43741adf6677194b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# purpose

<sub>Instance Property</sub>

An app-provided string that describes the reason for using location services.

> [!warning] Deprecated
> Set the purpose string using the [NSLocationWhenInUseUsageDescription](../../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) key in the app’s `Info.plist` instead.

<sub>macOS</sub>

```swift
var purpose: String? { get set }
```

## Discussion

If this property isn’t `nil` and the system needs to ask for the user’s consent to use location services, it displays the provided string. You can use this string to explain why your app is using location services.

You must set the value of this property prior to starting any location services. Because the string is ultimately displayed to the user, you should always load it from a localized strings file.

## See Also

### Properties

- [headingAvailable](headingavailable-swift.property.md) — A Boolean value indicating whether the location manager is able to generate heading-related events. _(deprecated)_
- [locationServicesEnabled](locationservicesenabled-swift.property.md) — A Boolean value indicating whether location services are enabled on the device. _(deprecated)_
- [rangedRegions](rangedregions.md) — The set of regions currently being tracked using ranging. _(deprecated)_
