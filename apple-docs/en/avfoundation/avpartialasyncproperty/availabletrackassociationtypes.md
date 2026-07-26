---
title: availableTrackAssociationTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/availabletrackassociationtypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/availabletrackassociationtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/availabletrackassociationtypes.json'
content_hash: 'sha256:d65c1afed417eefa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# availableTrackAssociationTypes

<sub>Type Property</sub>

An array of association types that the track uses to associate with other tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var availableTrackAssociationTypes: AVAsyncProperty<Root, [AVAssetTrack.AssociationType]> { get }
```

## Discussion

Use the [load(_:isolation:)](<../avasynchronouskeyvalueloading/load(__isolation_).md>) method to retrieve the property value.

## See Also

### Loading track associations

- [- loadAssociatedTracksOfType:completionHandler:](<../avassettrack/loadassociatedtracks(oftype_completionhandler_).md>) — Loads associated tracks that have the specified association type.
