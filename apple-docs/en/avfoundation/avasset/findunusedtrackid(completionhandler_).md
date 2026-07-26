---
title: 'findUnusedTrackID(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avasset/findunusedtrackid(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/findunusedtrackid(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/findunusedtrackid%28completionhandler%3A%29.json'
content_hash: 'sha256:0d4903265631d078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# findUnusedTrackID(completionHandler:)

<sub>Instance Method</sub>

Loads an identifier that no other track in the asset uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func findUnusedTrackID(completionHandler: @escaping @Sendable (CMPersistentTrackID, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func findUnusedTrackID() async throws -> CMPersistentTrackID
```

## Parameters

- `completionHandler` — A completion handler the system calls after it finishes the request.

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-48zyw.md) — The tracks of media that an asset contains.
- [- loadTrackWithTrackID:completionHandler:](<loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.
