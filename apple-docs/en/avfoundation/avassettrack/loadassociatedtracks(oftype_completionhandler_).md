---
title: 'loadAssociatedTracks(ofType:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassettrack/loadassociatedtracks(oftype:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/loadassociatedtracks(oftype:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/loadassociatedtracks%28oftype%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:6acb0b77559a84dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# loadAssociatedTracks(ofType:completionHandler:)

<sub>Instance Method</sub>

Loads associated tracks that have the specified association type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadAssociatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType, completionHandler: @escaping @Sendable ([AVAssetTrack]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadAssociatedTracks(ofType trackAssociationType: AVAssetTrack.AssociationType) async throws -> [AVAssetTrack]
```

## Parameters

- `trackAssociationType` — The track association type to load tracks for.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **tracks** — The array of associated tracks, which may be empty if there are no tracks for the specified association type. The value is `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading track associations

- [availableTrackAssociationTypes](../avpartialasyncproperty/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
