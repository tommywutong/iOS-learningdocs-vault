---
title: isSimulatedBySoftware
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationsourceinformation/issimulatedbysoftware
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationsourceinformation/issimulatedbysoftware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationsourceinformation/issimulatedbysoftware.json'
content_hash: 'sha256:a6ef8db59ce2990e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationSourceInformation](../cllocationsourceinformation.md)

# isSimulatedBySoftware

<sub>Instance Property</sub>

A Boolean value that indicates whether the system generates the location using on-device software simulation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSimulatedBySoftware: Bool { get }
```

## Discussion

Core Location sets [isSimulatedBySoftware](issimulatedbysoftware.md) to `true` if the system generated the location using on-device software simulation. You can simulate locations by loading GPX files using the Xcode debugger. The default value is `false`.

## See Also

### Identifying the source of location data

- [isProducedByAccessory](isproducedbyaccessory.md) — A Boolean value that indicates whether the system receives the location from an external accessory.
