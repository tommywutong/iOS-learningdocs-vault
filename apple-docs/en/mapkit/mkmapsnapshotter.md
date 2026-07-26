---
title: MKMapSnapshotter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter.json'
content_hash: 'sha256:f5b4795dc24a2732'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapSnapshotter

<sub>Class</sub>

A utility class for capturing a map and its content into an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class MKMapSnapshotter
```

## Overview

Use an [MKMapSnapshotter](mkmapsnapshotter.md) object when you want to capture the system-provided map content, including the map tiles and imagery. The snapshotter object captures the best image possible by loading all of the available map tiles before capturing the image.

Configure a snapshotter object using an [Options](mkmapsnapshotter/options.md) object. The snapshot options specify the appearance of the map, including which portion of the map the snapshotter captures.

> [!note] Note
> Snapshotter objects don’t capture the visual representations of any overlays or annotations that your app creates. If you want those items to appear in the final snapshot, you must draw them on the resulting snapshot image. For more information about drawing custom content on map snapshots, see [Snapshot](mkmapsnapshotter/snapshot.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a snapshotter object

- [- initWithOptions:](<mkmapsnapshotter/init(options_).md>) — Creates and returns a snapshotter object based on the specified options.
- [Options](mkmapsnapshotter/options.md) — The options the snapshotter initializer uses to create a snapshotter to capture map-based imagery.

### Generating a snapshot

- [- startWithCompletionHandler:](<mkmapsnapshotter/start(completionhandler_).md>) — Submits the request to create a snapshot and delivers the results to the specified block.
- [- startWithQueue:completionHandler:](<mkmapsnapshotter/start(with_completionhandler_).md>) — Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [CompletionHandler](mkmapsnapshotter/completionhandler.md) — A block that processes the results of a snapshot request.
- [- cancel](<mkmapsnapshotter/cancel().md>) — Cancels the request to create a snapshot.
- [loading](mkmapsnapshotter/isloading.md) — A Boolean value that indicates whether the snapshotter is generating an image.

### Snapshot output

- [Snapshot](mkmapsnapshotter/snapshot.md) — An image that a snapshotter object generates.

## See Also

### Static map snapshots

- [Snapshot](mkmapsnapshotter/snapshot.md) — An image that a snapshotter object generates.
