---
title: x
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clheading/x
source_url: 'https://developer.apple.com/documentation/corelocation/clheading/x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clheading/x.json'
content_hash: 'sha256:97725ea73365e8c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLHeading](../clheading.md)

# x

<sub>Instance Property</sub>

The geomagnetic data (measured in microteslas) for the x-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
var x: CLHeadingComponentValue { get }
```

## Discussion

This value represents the x-axis deviation from the magnetic field lines being tracked by the device.

## See Also

### Getting the raw heading data

- [y](y.md) — The geomagnetic data (measured in microteslas) for the y-axis.
- [z](z.md) — The geomagnetic data (measured in microteslas) for the z-axis.
- [CLHeadingComponentValue](../clheadingcomponentvalue.md) — A type used to report magnetic differences reported by the onboard hardware.
