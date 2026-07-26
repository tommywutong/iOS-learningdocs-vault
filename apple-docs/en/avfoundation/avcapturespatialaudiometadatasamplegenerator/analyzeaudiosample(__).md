---
title: 'analyzeAudioSample(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/analyzeaudiosample%28_%3A%29.json'
content_hash: 'sha256:7a8807a029bf7cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSpatialAudioMetadataSampleGenerator](../avcapturespatialaudiometadatasamplegenerator.md)

# analyzeAudioSample(_:)

<sub>Instance Method</sub>

Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func analyzeAudioSample(_ sbuf: CMSampleBuffer) -> OSStatus
```

## Parameters

- `sbuf` — A sample buffer containing spatial audio.

## Return Value

`noErr` if the sample is successfully analyzed, otherwise a non-zero error code.

## Discussion

You must call this method with each and every spatial audio buffer you provide to [AVAssetWriter](../avassetwriter.md), so it can be analyzed for the generation of a proper spatial audio timed metadata value.

## See Also

### Analyzing audio samples

- [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) — Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [timedMetadataSampleBufferFormatDescription](timedmetadatasamplebufferformatdescription.md) — Returns the format description of the sample buffer returned from the [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) method.
- [- resetAnalyzer](<resetanalyzer().md>) — Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.
