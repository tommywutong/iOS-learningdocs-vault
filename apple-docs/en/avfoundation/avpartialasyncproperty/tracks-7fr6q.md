---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avpartialasyncproperty/tracks-7fr6q
source_url: 'https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/tracks-7fr6q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avpartialasyncproperty/tracks-7fr6q.json'
content_hash: 'sha256:da4ee57438f08bea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPartialAsyncProperty](../avpartialasyncproperty.md)

# tracks

<sub>Type Property</sub>

The tracks that a movie contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static var tracks: AVAsyncProperty<Root, [AVFragmentedMovieTrack]> { get }
```

## See Also

### Loading tracks

- [- loadTrackWithTrackID:completionHandler:](<../avfragmentedmovie/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<../avfragmentedmovie/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<../avfragmentedmovie/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
