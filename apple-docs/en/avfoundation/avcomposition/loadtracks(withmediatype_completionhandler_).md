---
title: 'loadTracks(withMediaType:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcomposition/loadtracks(withmediatype:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcomposition/loadtracks(withmediatype:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcomposition/loadtracks%28withmediatype%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:1d21c151cae63895'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVComposition](../avcomposition.md)

# loadTracks(withMediaType:completionHandler:)

<sub>Instance Method</sub>

Loads tracks that contain media of a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaType mediaType: AVMediaType, completionHandler: @escaping @Sendable ([AVCompositionTrack]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaType mediaType: AVMediaType) async throws -> [AVCompositionTrack]
```

## Parameters

- `mediaType` — The media type of the tracks to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading operation. It passes the completion handler the following parameters: - **tracks** — An array of tracks, which may be empty if no tracks with the specified media type exist. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-9eows.md) — The tracks that a composition contains.
- [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
