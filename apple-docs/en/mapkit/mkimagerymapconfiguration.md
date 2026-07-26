---
title: MKImageryMapConfiguration
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkimagerymapconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkimagerymapconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkimagerymapconfiguration.json'
content_hash: 'sha256:6a557bc88133beee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKImageryMapConfiguration

<sub>Class</sub>

The class that represents an imagery-based map presentation, such as one using satellite imagery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKImageryMapConfiguration
```

## Relationships

- **Inherits From**: [MKMapConfiguration](mkmapconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a map imagery configuration

- [- init](<mkimagerymapconfiguration/init().md>) — Creates a new imagery based map configuration.
- [- initWithElevationStyle:](<mkimagerymapconfiguration/init(elevationstyle_).md>) — Creates a new imagery based map configuration with the specified elevation style.

## See Also

### Configuring the map appearance

- [preferredConfiguration](mkmapview/preferredconfiguration.md) — The characteristics of the map view, including the map type and features the map displays.
- [pitchButtonVisibility](mkmapview/pitchbuttonvisibility.md) — A value that indicates whether the map’s pitch button is visible.
- [showsUserTrackingButton](mkmapview/showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKMapConfiguration](mkmapconfiguration.md) — An abstract class that represents the shared elements of map configurations.
- [MKStandardMapConfiguration](mkstandardmapconfiguration.md) — The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [MKHybridMapConfiguration](mkhybridmapconfiguration.md) — The class that represents a satellite image of the area with road and road name information layers on top.
