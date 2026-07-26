---
title: MKLookAroundSceneRequest
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklookaroundscenerequest
source_url: 'https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklookaroundscenerequest.json'
content_hash: 'sha256:9ba379c40e50bd4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKLookAroundSceneRequest

<sub>Class</sub>

A class you use to request a LookAround scene at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class MKLookAroundSceneRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a LookAround scene

- [- initWithCoordinate:](<mklookaroundscenerequest/init(coordinate_).md>) — Creates a LookAround scene at the specified coordinates.
- [- initWithMapItem:](<mklookaroundscenerequest/init(mapitem_).md>) — Creates a LookAround scene with the location described by the specified map item.

### Specifying the request’s location

- [coordinate](mklookaroundscenerequest/coordinate.md) — A coordinate value that describes the location of the LookAround scene.
- [mapItem](mklookaroundscenerequest/mapitem.md) — A map item that describes the location of the LookAround scene.

### Starting and stopping scene requests

- [- cancel](<mklookaroundscenerequest/cancel().md>) — Cancels the pending scene request.
- [- getSceneWithCompletionHandler:](<mklookaroundscenerequest/getscenewithcompletionhandler(__).md>) — Requests a LookAround scene and calls the specified completion handler.

### Monitoring the progress of scene requests

- [cancelled](mklookaroundscenerequest/iscancelled.md) — A Boolean value that indicates if the cancellation of a scene request was successful.
- [loading](mklookaroundscenerequest/isloading.md) — A Boolean value that indicates whether a scene request is loading.

## See Also

### Exploring at street level

- [MKLookAroundScene](mklookaroundscene.md) — A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [MKLookAroundViewController](mklookaroundviewcontroller.md) — A class that manages the presentation and display of a LookAround view.
- [MKLookAroundSnapshotter](mklookaroundsnapshotter.md) — A utility class that you use to create a static image from a LookAround scene.
