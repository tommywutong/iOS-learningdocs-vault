---
title: isProducedByAccessory
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationsourceinformation/isproducedbyaccessory
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationsourceinformation/isproducedbyaccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationsourceinformation/isproducedbyaccessory.json'
content_hash: 'sha256:ae94a049b3fde0cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationSourceInformation](../cllocationsourceinformation.md)

# isProducedByAccessory

<sub>Instance Property</sub>

A Boolean value that indicates whether the system receives the location from an external accessory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isProducedByAccessory: Bool { get }
```

## Discussion

Core Location sets [isProducedByAccessory](isproducedbyaccessory.md) to `true` if the system retrieved the location from an external accessory attached to the device, such as a Made for iPhone GPS dongle or CarPlay. Otherwise, the default value is `false`.

## See Also

### Identifying the source of location data

- [isSimulatedBySoftware](issimulatedbysoftware.md) — A Boolean value that indicates whether the system generates the location using on-device software simulation.
