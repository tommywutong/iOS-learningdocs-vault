---
title: AVFragmentedMovie
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.10+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avfragmentedmovie
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovie.json'
content_hash: 'sha256:ba7daf8e7e2e7061'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVFragmentedMovie

<sub>Class</sub>

An object that represents a fragmented movie file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVFragmentedMovie
```

## Relationships

- **Inherits From**: [AVMovie](avmovie.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [AVFragmentMinding](avfragmentminding.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-7fr6q.md) — The tracks that a movie contains.
- [- loadTrackWithTrackID:completionHandler:](<avfragmentedmovie/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<avfragmentedmovie/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<avfragmentedmovie/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.

### Accessing tracks

- [tracks](avfragmentedmovie/tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<avfragmentedmovie/track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<avfragmentedmovie/tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<avfragmentedmovie/tracks(withmediacharacteristic_).md>) — Retrieves tracks in the movie that present media of the specified characteristic. _(deprecated)_

## See Also

### Fragmented movies

- [AVFragmentedMovieTrack](avfragmentedmovietrack.md) — An object that represents a track in a fragmented movie.
- [AVFragmentedMovieMinder](avfragmentedmovieminder.md) — An object that checks whether a fragmented movie appends additional movie fragments.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.
