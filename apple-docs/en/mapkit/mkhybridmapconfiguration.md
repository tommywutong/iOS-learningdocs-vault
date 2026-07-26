---
title: MKHybridMapConfiguration
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkhybridmapconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkhybridmapconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkhybridmapconfiguration.json'
content_hash: 'sha256:ff968159bc3b3792'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKHybridMapConfiguration

<sub>Class</sub>

The class that represents a satellite image of the area with road and road name information layers on top.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKHybridMapConfiguration
```

## Relationships

- **Inherits From**: [MKMapConfiguration](mkmapconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a hybrid map configuration

- [- init](<mkhybridmapconfiguration/init().md>) — Creates a new hybrid map configuration.
- [- initWithElevationStyle:](<mkhybridmapconfiguration/init(elevationstyle_).md>) — Creates a new hybrid map configuration with the specified elevation style.
- [ElevationStyle](mkmapconfiguration/elevationstyle-swift.enum.md) — Values that control the map’s elevation style.

### Controlling what the map displays

- [pointOfInterestFilter](mkhybridmapconfiguration/pointofinterestfilter.md) — The filter the framework uses to determine the points of interest to show on the map.
- [showsTraffic](mkhybridmapconfiguration/showstraffic.md) — A Boolean value that indicates whether the maps shows traffic conditions.

## See Also

### Configuring the map appearance

- [preferredConfiguration](mkmapview/preferredconfiguration.md) — The characteristics of the map view, including the map type and features the map displays.
- [pitchButtonVisibility](mkmapview/pitchbuttonvisibility.md) — A value that indicates whether the map’s pitch button is visible.
- [showsUserTrackingButton](mkmapview/showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKMapConfiguration](mkmapconfiguration.md) — An abstract class that represents the shared elements of map configurations.
- [MKStandardMapConfiguration](mkstandardmapconfiguration.md) — The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [MKImageryMapConfiguration](mkimagerymapconfiguration.md) — The class that represents an imagery-based map presentation, such as one using satellite imagery.
