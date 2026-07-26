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
doc_path: '/documentation/avfoundation/avasset/loadtracks(withmediatype:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/loadtracks(withmediatype:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/loadtracks%28withmediatype%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:0b0a00af205ea258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# loadTracks(withMediaType:completionHandler:)

<sub>Instance Method</sub>

Loads tracks that contain media of a specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaType mediaType: AVMediaType, completionHandler: @escaping @Sendable ([AVAssetTrack]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadTracks(withMediaType mediaType: AVMediaType) async throws -> [AVAssetTrack]
```

## Parameters

- `mediaType` — The media type of the tracks to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading operation. It passes the completion handler the following parameters: - **tracks** — An array of tracks, which may be empty if no tracks with the specified media type exist. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-48zyw.md) — The tracks of media that an asset contains.
- [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
- [- findUnusedTrackIDWithCompletionHandler:](<findunusedtrackid(completionhandler_).md>) — Loads an identifier that no other track in the asset uses.
