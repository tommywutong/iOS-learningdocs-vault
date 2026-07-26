---
title: MKStandardMapConfiguration
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkstandardmapconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkstandardmapconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkstandardmapconfiguration.json'
content_hash: 'sha256:e4fef68909456eec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKStandardMapConfiguration

<sub>Class</sub>

The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKStandardMapConfiguration
```

## Relationships

- **Inherits From**: [MKMapConfiguration](mkmapconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a standard map configuration

- [- init](<mkstandardmapconfiguration/init().md>) — Creates a new standard map configuration.
- [- initWithElevationStyle:](<mkstandardmapconfiguration/init(elevationstyle_).md>) — Creates a new standard map configuration with the specified elevation style.
- [- initWithElevationStyle:emphasisStyle:](<mkstandardmapconfiguration/init(elevationstyle_emphasisstyle_).md>) — Creates a standard map configuration with the specified elevation and emphasis styles.
- [- initWithEmphasisStyle:](<mkstandardmapconfiguration/init(emphasisstyle_).md>) — Creates a standard map configuration with the specified emphasis style.
- [ElevationStyle](mkmapconfiguration/elevationstyle-swift.enum.md) — Values that control the map’s elevation style.
- [EmphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.enum.md) — Values that control how the framework emphasizes map features.

### Customizing the map display

- [emphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.property.md) — The value that indicates how the framework emphasizes map features.
- [EmphasisStyle](mkstandardmapconfiguration/emphasisstyle-swift.enum.md) — Values that control how the framework emphasizes map features.
- [pointOfInterestFilter](mkstandardmapconfiguration/pointofinterestfilter.md) — The filter used to determine the points of interest shown on the map.
- [showsTraffic](mkstandardmapconfiguration/showstraffic.md) — A Boolean value that controls whether the map displays traffic conditions.

## See Also

### Configuring the map appearance

- [preferredConfiguration](mkmapview/preferredconfiguration.md) — The characteristics of the map view, including the map type and features the map displays.
- [pitchButtonVisibility](mkmapview/pitchbuttonvisibility.md) — A value that indicates whether the map’s pitch button is visible.
- [showsUserTrackingButton](mkmapview/showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKMapConfiguration](mkmapconfiguration.md) — An abstract class that represents the shared elements of map configurations.
- [MKHybridMapConfiguration](mkhybridmapconfiguration.md) — The class that represents a satellite image of the area with road and road name information layers on top.
- [MKImageryMapConfiguration](mkimagerymapconfiguration.md) — The class that represents an imagery-based map presentation, such as one using satellite imagery.
