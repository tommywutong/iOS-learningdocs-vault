---
title: 'comparePositionInDecodeOrder(withPositionOf:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursor/comparepositionindecodeorder(withpositionof:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/comparepositionindecodeorder(withpositionof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/comparepositionindecodeorder%28withpositionof%3A%29.json'
content_hash: 'sha256:cebe726331350577'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# comparePositionInDecodeOrder(withPositionOf:)

<sub>Instance Method</sub>

Compares the relative positions of two sample cursors and returns their relative positions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func comparePositionInDecodeOrder(withPositionOf cursor: AVSampleCursor) -> ComparisonResult
```

## Parameters

- `cursor` — An instance of `AVSampleCursor` with which to compare positions.

## Return Value

Returns a comparison result that indicates of this cursor points at a sample before, the same as, or after the sample pointed to by the specified cursor.

## Discussion

Undefined results occur if this cursor and the passed in cursor reference different sequences of samples, such as when they’re created by different instances of [AVAssetTrack](../avassettrack.md).
