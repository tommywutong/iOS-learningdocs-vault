---
title: 'loadTrack(withTrackID:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablecomposition/loadtrack(withtrackid:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecomposition/loadtrack(withtrackid:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecomposition/loadtrack%28withtrackid%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:8474838d16850c4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableComposition](../avmutablecomposition.md)

# loadTrack(withTrackID:completionHandler:)

<sub>Instance Method</sub>

Loads a track that contains the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID, completionHandler: @escaping @Sendable (AVMutableCompositionTrack?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTrack(withTrackID trackID: CMPersistentTrackID) async throws -> AVMutableCompositionTrack?
```

## Parameters

- `trackID` — The identifier of the track to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **track** — The loaded track, or `nil` if no track with the specified identifier exists or if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-92p4a.md) — The tracks that a composition contains.
- [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
