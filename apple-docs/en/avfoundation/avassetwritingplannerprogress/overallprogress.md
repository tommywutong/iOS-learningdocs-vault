---
title: overallProgress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwritingplannerprogress/overallprogress
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwritingplannerprogress/overallprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwritingplannerprogress/overallprogress.json'
content_hash: 'sha256:7e431650868b320a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWritingPlannerProgress](../avassetwritingplannerprogress.md)

# overallProgress

<sub>Instance Property</sub>

The overall progress across all tracks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var overallProgress: Float { get }
```

## Discussion

Returns a float value between 0.0 and 1.0 representing the overall progress. This is calculated as the average progress of all tracks weighted by their durations.

## See Also

### Getting progress

- [- progressForTrack:](<progress(fortrack_).md>) — Returns the progress for a specific track identified by its assemblyTrackID. _(beta)_
- [- progressForTrack:](<progress(fortrack_).md>) — Returns the progress for a specific track identified by its assemblyTrackID. _(beta)_
