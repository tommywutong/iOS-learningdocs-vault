---
title: 'loadSamplePresentationTime(forTrackTime:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/loadsamplepresentationtime(fortracktime:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/loadsamplepresentationtime%28fortracktime%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:34b7fa266d095049'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# loadSamplePresentationTime(forTrackTime:completionHandler:)

<sub>Instance Method</sub>

Loads a sample presentation time that maps to the specified track time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadSamplePresentationTime(forTrackTime trackTime: CMTime, completionHandler: @escaping @Sendable (CMTime, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadSamplePresentationTime(forTrackTime trackTime: CMTime) async throws -> CMTime
```

## Parameters

- `trackTime` — The track time of the presentation time to load.

- `completionHandler` — A callback that the system invokes after it finishes the loading request. It passes the completion handler the following parameters: - **time** — A [CMTime](../../coremedia/cmtime.md) value, which is [invalid](../../coremedia/cmtime/invalid.md) if the track time is out of range or if an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## See Also

### Loading track segments

- [segments](../avpartialasyncproperty/segments.md) — The time mappings from the track’s media samples to its timeline.
- [- loadSegmentForTrackTime:completionHandler:](<loadsegment(fortracktime_completionhandler_).md>) — Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [AVAssetTrackSegment](../avassettracksegment.md) — An object that represents a time range segment of an asset track.
