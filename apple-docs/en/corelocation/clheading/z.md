---
title: z
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clheading/z
source_url: 'https://developer.apple.com/documentation/corelocation/clheading/z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clheading/z.json'
content_hash: 'sha256:7e65751392906770'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLHeading](../clheading.md)

# z

<sub>Instance Property</sub>

The geomagnetic data (measured in microteslas) for the z-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var z: CLHeadingComponentValue { get }
```

## Discussion

This value represents the z-axis deviation from the magnetic field lines being tracked by the device.

## See Also

### Getting the raw heading data

- [x](x.md) — The geomagnetic data (measured in microteslas) for the x-axis.
- [y](y.md) — The geomagnetic data (measured in microteslas) for the y-axis.
- [CLHeadingComponentValue](../clheadingcomponentvalue.md) — A type used to report magnetic differences reported by the onboard hardware.
