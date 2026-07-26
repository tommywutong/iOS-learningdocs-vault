---
title: timedMetadataSampleBufferFormatDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/timedmetadatasamplebufferformatdescription.json'
content_hash: 'sha256:6e2da15d7b9a1f63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSpatialAudioMetadataSampleGenerator](../avcapturespatialaudiometadatasamplegenerator.md)

# timedMetadataSampleBufferFormatDescription

<sub>Instance Property</sub>

Returns the format description of the sample buffer returned from the [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) method.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var timedMetadataSampleBufferFormatDescription: CMFormatDescription { get }
```

## Discussion

Use this format description when creating your [AVAssetWriter](../avassetwriter.md) track for spatial audio timed metadata.

## See Also

### Analyzing audio samples

- [- analyzeAudioSample:](<analyzeaudiosample(__).md>) — Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) — Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [- resetAnalyzer](<resetanalyzer().md>) — Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.
