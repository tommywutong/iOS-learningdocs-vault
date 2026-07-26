---
title: MKMapSnapshotter.Options
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options.json'
content_hash: 'sha256:3ac17367484aec16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# MKMapSnapshotter.Options

<sub>Class</sub>

The options the snapshotter initializer uses to create a snapshotter to capture map-based imagery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Overview

After creating and configuring an instance of this class, you pass that instance to an [MKMapSnapshotter](../mkmapsnapshotter.md) object. The snapshotter uses the configuration options to determine which portion of the map to capture, the viewing angle to use for the camera, and the map’s overall appearance.

In macOS 10.14 and later, you can apply a light or dark appearance to your map snapshots by modifying the [appearance](options/appearance.md) property of your snapshot options. Even if you specify a custom appearance, users can use the Maps app to force all maps to adopt a light appearance.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the snapshot region

- [region](options/region.md) — The area of the map that you want to capture.
- [mapRect](options/maprect.md) — The map rectangle that you want to capture.
- [camera](options/camera.md) — The camera to use when taking the map snapshot.

### Configuring the map data

- [preferredConfiguration](options/preferredconfiguration.md) — The map configuration style to use for snapshots.
- [mapType](options/maptype.md) — The map’s visual style. _(deprecated)_
- [showsBuildings](options/showsbuildings.md) — A Boolean that indicates whether the map displays extruded building information. _(deprecated)_
- [pointOfInterestFilter](options/pointofinterestfilter.md) — The filter to use for determining the points of interest that appear in the snapshot. _(deprecated)_
- [showsPointsOfInterest](options/showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_

### Configuring the image output

- [traitCollection](options/traitcollection.md) — Traits that determine the appearance of the map snapshot.
- [size](options/size.md) — The size of the image that you want to create.
- [appearance](options/appearance.md) — The visual style (light or dark) to apply to the map when rendering the snapshot image.
- [scale](options/scale.md) — The scale factor to use when creating the image. _(deprecated)_

## See Also

### Creating a snapshotter object

- [- initWithOptions:](<init(options_).md>) — Creates and returns a snapshotter object based on the specified options.
