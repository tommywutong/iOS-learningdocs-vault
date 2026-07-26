---
title: resetAnalyzer()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturespatialaudiometadatasamplegenerator/resetanalyzer%28%29.json'
content_hash: 'sha256:ae831dfec36c1562'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSpatialAudioMetadataSampleGenerator](../avcapturespatialaudiometadatasamplegenerator.md)

# resetAnalyzer()

<sub>Instance Method</sub>

Calling this method resets the analyzer to its initial state so that a new run of audio sample buffers can be analyzed.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func resetAnalyzer()
```

## Discussion

Call this method if you need to abort generating the audio timed metadata buffer for audio already provided to [- analyzeAudioSample:](<analyzeaudiosample(__).md>).

## See Also

### Analyzing audio samples

- [- analyzeAudioSample:](<analyzeaudiosample(__).md>) — Analyzes the provided audio sample buffer for its contribution to the spatial audio timed metadata value.
- [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) — Creates a sample buffer containing a spatial audio timed metadata sample computed from all analyzed audio buffers, and resets the analyzer to its initial state.
- [timedMetadataSampleBufferFormatDescription](timedmetadatasamplebufferformatdescription.md) — Returns the format description of the sample buffer returned from the [- newTimedMetadataSampleBufferAndResetAnalyzer](<newtimedmetadatasamplebufferandresetanalyzer().md>) method.
