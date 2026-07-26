---
title: 'loadSegment(forTrackTime:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassettrack/loadsegment(fortracktime:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/loadsegment(fortracktime:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/loadsegment%28fortracktime%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:ad9d098513ebb39d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# loadSegment(forTrackTime:completionHandler:)

<sub>Instance Method</sub>

Loads a segment with a target time range that contains, or is closest to, the specified track time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadSegment(forTrackTime trackTime: CMTime, completionHandler: @escaping @Sendable (AVAssetTrackSegment?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadSegment(forTrackTime trackTime: CMTime) async throws -> AVAssetTrackSegment?
```

## Parameters

- `trackTime` — The track time of the segment to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **segment** — The loaded track segment, or `nil` if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## Discussion

If the specified track time doesn’t map to a sample presentation time, the system returns the segment with the closest matching time.

## See Also

### Loading track segments

- [segments](../avpartialasyncproperty/segments.md) — The time mappings from the track’s media samples to its timeline.
- [- loadSamplePresentationTimeForTrackTime:completionHandler:](<loadsamplepresentationtime(fortracktime_completionhandler_).md>) — Loads a sample presentation time that maps to the specified track time.
- [AVAssetTrackSegment](../avassettracksegment.md) — An object that represents a time range segment of an asset track.
