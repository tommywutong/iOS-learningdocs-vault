---
title: 'loadTracks(withMediaCharacteristic:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avfragmentedmovie/loadtracks(withmediacharacteristic:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avfragmentedmovie/loadtracks(withmediacharacteristic:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avfragmentedmovie/loadtracks%28withmediacharacteristic%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:43dc88bae8834087'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFragmentedMovie](../avfragmentedmovie.md)

# loadTracks(withMediaCharacteristic:completionHandler:)

<sub>Instance Method</sub>

Loads tracks that contain media of a specified characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic, completionHandler: @escaping @Sendable ([AVFragmentedMovieTrack]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaCharacteristic mediaCharacteristic: AVMediaCharacteristic) async throws -> [AVFragmentedMovieTrack]
```

## Parameters

- `mediaCharacteristic` — The media characteristic of the tracks to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **tracks** — An array of tracks, which may be empty if no tracks with the specified media characteristic exist. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-7fr6q.md) — The tracks that a movie contains.
- [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
