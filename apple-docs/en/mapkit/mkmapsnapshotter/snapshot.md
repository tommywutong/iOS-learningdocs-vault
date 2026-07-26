---
title: MKMapSnapshotter.Snapshot
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/snapshot
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/snapshot.json'
content_hash: 'sha256:997d4d53e35d9b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapSnapshotter](../mkmapsnapshotter.md)

# MKMapSnapshotter.Snapshot

<sub>Class</sub>

An image that a snapshotter object generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Snapshot
```

## Overview

You don’t create instances of this class directly. Instead, you use an [MKMapSnapshotter](../mkmapsnapshotter.md) object to capture the map contents asynchronously. An `MKMapSnapshotter.Snapshot` object contains the image that the snapshotter generates from the map contents.

Snapshot images don’t include any custom overlays or annotations that your app adds to the map view. If you want your annotations and overlays to appear on the final image, you need to draw them yourself. To position those items correctly on the image, use the [- pointForCoordinate:](<snapshot/point(for_).md>) method of this class to translate the overlay or annotation coordinate value to an appropriate location inside the image’s coordinate space.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Getting the snapshot image

- [image](snapshot/image.md) — The image of the map’s content.
- [appearance](snapshot/appearance.md) — The visual style that MapKit uses when rendering the snapshot.

### Getting points on the image

- [- pointForCoordinate:](<snapshot/point(for_).md>) — Converts the specified map coordinate to a point in the coordinate space of the image.

### Getting appearance traits

- [traitCollection](snapshot/traitcollection.md) — Traits to use when creating the snapshot.

## See Also

### Static map snapshots

- [MKMapSnapshotter](../mkmapsnapshotter.md) — A utility class for capturing a map and its content into an image.
