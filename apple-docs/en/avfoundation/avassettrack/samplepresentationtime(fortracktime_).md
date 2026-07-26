---
title: 'samplePresentationTime(forTrackTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassettrack/samplepresentationtime(fortracktime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/samplepresentationtime(fortracktime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/samplepresentationtime%28fortracktime%3A%29.json'
content_hash: 'sha256:53caa4f6ed1b7ad4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# samplePresentationTime(forTrackTime:)

<sub>Instance Method</sub>

Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

> [!warning] Deprecated
> Use [- loadSamplePresentationTimeForTrackTime:completionHandler:](<loadsamplepresentationtime(fortracktime_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
func samplePresentationTime(forTrackTime trackTime: CMTime) -> CMTime
```

## Parameters

- `trackTime` — The track time for which to request the sample presentation time.

## Return Value

The sample presentation time corresponding to the specified time; otherwise [invalid](../../coremedia/cmtime/invalid.md) if the time is out of range.

## Discussion

Apple discourages using this method in iOS 15, tvOS 15, macOS 12, and watchOS 8 or later. Load a sample presentation time asynchronously using [- loadSamplePresentationTimeForTrackTime:completionHandler:](<loadsamplepresentationtime(fortracktime_completionhandler_).md>) instead.
