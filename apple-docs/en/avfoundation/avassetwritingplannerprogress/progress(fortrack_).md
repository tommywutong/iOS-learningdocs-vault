---
title: 'progress(forTrack:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avassetwritingplannerprogress/progress(fortrack:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress/progress(fortrack:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplannerprogress/progress%28fortrack%3A%29.json'
content_hash: 'sha256:351821955e84a7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlannerProgress](../avassetwritingplannerprogress.md)

# progress(forTrack:)

<sub>Instance Method</sub>

Returns the progress for a specific track identified by its assemblyTrackID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func progress(forTrack assemblyTrackID: CMPersistentTrackID) -> Float
```

## Parameters

- `assemblyTrackID` — The track ID to query progress for.

## Return Value

A float value between 0.0 and 1.0 representing the percentage of duration completed for the track. Returns 0.0 if the track ID is not found.

## Discussion

The progress is calculated as the ratio of completed duration to total duration for the track.

## See Also

### Getting progress

- [overallProgress](overallprogress.md) — The overall progress across all tracks. _(beta)_
