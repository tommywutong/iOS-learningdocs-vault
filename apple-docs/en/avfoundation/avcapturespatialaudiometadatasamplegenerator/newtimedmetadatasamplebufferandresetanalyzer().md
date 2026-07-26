---
title: newTimedMetadataSampleBufferAndResetAnalyzer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/newtimedmetadatasamplebufferandresetanalyzer%28%29.json'
content_hash: 'sha256:174316a1bc4b7be1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSpatialAudioMetadataSampleGenerator](../avcapturespatialaudiometadatasamplegenerator.md)

# newTimedMetadataSampleBufferAndResetAnalyzer()

<sub>Instance Method</sub>

Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func newTimedMetadataSampleBufferAndResetAnalyzer() -> Unmanaged<CMSampleBuffer>?
```

## Return Value

A `CMSampleBufferRef` containing the spatial audio timed metadata sample, or `NULL` if no value can be computed.

## Discussion

Call this method after you pass the last audio sample buffer of your recording to [- analyzeAudioSample:](<analyzeaudiosample(__).md>). Then pass the returned `CMSampleBufferRef` directly to your [AVAssetWriterInput](../avassetwriterinput.md) to add the sample to your recording’s audio timed metadata track. Note that [AVAssetWriter](../avassetwriter.md) expects one and only one spatial audio metadata sample buffer to be present in the timed metadata track.

> [!note] Note
> Calling this method also resets the analyzer, making it ready for another run of audio sample buffers. Thus one generator can be re-used for multiple recordings.

## See Also

### Analyzing audio samples

- [- analyzeAudioSample:](<analyzeaudiosample(__).md>) — Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [timedMetadataSampleBufferFormatDescription](timedmetadatasamplebufferformatdescription.md) — Returns the format description of the sample buffer returned from the [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) method.
- [- resetAnalyzer](<resetanalyzer().md>) — Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.
