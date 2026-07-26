---
title: MKLookAroundSnapshotter
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklookaroundsnapshotter
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundsnapshotter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundsnapshotter.json'
content_hash: 'sha256:44a2f23d3e312691'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLookAroundSnapshotter

<sub>Class</sub>

A utility class that you use to create a static image from a LookAround scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MKLookAroundSnapshotter
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a snapshotter object

- [- initWithScene:options:](<mklookaroundsnapshotter/init(scene_options_).md>) — Create a new snapshotter object with the scene and options you specify.

### Starting and stopping a snapshot

- [- cancel](<mklookaroundsnapshotter/cancel().md>) — Cancels an in-progress snapshot request.
- [- getSnapshotWithCompletionHandler:](<mklookaroundsnapshotter/getsnapshotwithcompletionhandler(__).md>) — Requests a new snapshot and calls the completion handler you provide.

### Monitoring the progress of a snaphot

- [loading](mklookaroundsnapshotter/isloading.md) — A Boolean value that indicates whether the snapshot request is loading.

### Customizing the snapshot

- [Options](mklookaroundsnapshotter/options.md) — Values you use to customize LookAround snapshots.

### Accessing snapshot imagery

- [Snapshot](mklookaroundsnapshotter/snapshot.md) — An object that contains a snapshot image.

## See Also

### Exploring at street level

- [MKLookAroundScene](mklookaroundscene.md) — A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [MKLookAroundSceneRequest](mklookaroundscenerequest.md) — A class you use to request a LookAround scene at the location you specify.
- [MKLookAroundViewController](mklookaroundviewcontroller.md) — A class that manages the presentation and display of a LookAround view.
