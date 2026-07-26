---
title: 'loadTrack(withTrackID:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmovie/loadtrack(withtrackid:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmovie/loadtrack(withtrackid:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmovie/loadtrack%28withtrackid%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:e4a99ac931ee6ec3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMovie](../avmovie.md)

# loadTrack(withTrackID:completionHandler:)

<sub>Instance Method</sub>

Loads a track that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID, completionHandler: @escaping @Sendable (AVMovieTrack?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID) async throws -> AVMovieTrack?
```

## Parameters

- `trackID` — The identifier of the track to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **track** — The loaded track, or `nil` if no track with the specified identifier exists or if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-80a83.md) — The tracks that a movie contains.
- [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
