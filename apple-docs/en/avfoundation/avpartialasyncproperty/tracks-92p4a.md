---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/tracks-92p4a
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-92p4a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/tracks-92p4a.json'
content_hash: 'sha256:ea299b048e641c8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# tracks

<sub>Type Property</sub>

The tracks that a composition contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var tracks: AVAsyncProperty<Root, [AVMutableCompositionTrack]> { get }
```

## See Also

### Loading tracks

- [- loadTrackWithTrackID:completionHandler:](<../avmutablecomposition/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<../avmutablecomposition/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<../avmutablecomposition/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
