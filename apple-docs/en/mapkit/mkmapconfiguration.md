---
title: MKMapConfiguration
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapconfiguration.json'
content_hash: 'sha256:f822837c574467a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapConfiguration

<sub>Class</sub>

An abstract class that represents the shared elements of map configurations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMapConfiguration
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MKHybridMapConfiguration](mkhybridmapconfiguration.md), [MKImageryMapConfiguration](mkimagerymapconfiguration.md), [MKStandardMapConfiguration](mkstandardmapconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Controlling the elevation style

- [elevationStyle](mkmapconfiguration/elevationstyle-swift.property.md) — The value that indicates the map’s elevation style.
- [ElevationStyle](mkmapconfiguration/elevationstyle-swift.enum.md) — Values that control the map’s elevation style.

### Initializers

- [init(coder:)](<mkmapconfiguration/init(coder_).md>)

## See Also

### Configuring the map appearance

- [preferredConfiguration](mkmapview/preferredconfiguration.md) — The characteristics of the map view, including the map type and features the map displays.
- [pitchButtonVisibility](mkmapview/pitchbuttonvisibility.md) — A value that indicates whether the map’s pitch button is visible.
- [showsUserTrackingButton](mkmapview/showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKStandardMapConfiguration](mkstandardmapconfiguration.md) — The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [MKHybridMapConfiguration](mkhybridmapconfiguration.md) — The class that represents a satellite image of the area with road and road name information layers on top.
- [MKImageryMapConfiguration](mkimagerymapconfiguration.md) — The class that represents an imagery-based map presentation, such as one using satellite imagery.
