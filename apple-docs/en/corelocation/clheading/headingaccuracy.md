---
title: headingAccuracy
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clheading/headingaccuracy
source_url: 'https://developer.apple.com/documentation/corelocation/clheading/headingaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clheading/headingaccuracy.json'
content_hash: 'sha256:eb71937b2f36bb49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLHeading](../clheading.md)

# headingAccuracy

<sub>Instance Property</sub>

The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var headingAccuracy: CLLocationDirection { get }
```

## Discussion

A positive value in this property represents the potential error between the value reported by the [magneticHeading](magneticheading.md) property and the actual direction of magnetic north. Thus, the lower the value of this property, the more accurate the heading. A negative value means that the reported heading is invalid, which can occur when the device is uncalibrated or there is strong interference from local magnetic fields.

## See Also

### Getting the heading values

- [magneticHeading](magneticheading.md) — The heading (measured in degrees) relative to magnetic north.
- [trueHeading](trueheading.md) — The heading (measured in degrees) relative to true north.
