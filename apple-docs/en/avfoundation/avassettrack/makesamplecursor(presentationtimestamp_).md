---
title: 'makeSampleCursor(presentationTimeStamp:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassettrack/makesamplecursor(presentationtimestamp:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/makesamplecursor(presentationtimestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/makesamplecursor%28presentationtimestamp%3A%29.json'
content_hash: 'sha256:fde995bcb6b45fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# makeSampleCursor(presentationTimeStamp:)

<sub>Instance Method</sub>

Creates a sample cursor and positions it at or near the specified presentation timestamp.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSampleCursor(presentationTimeStamp: CMTime) -> AVSampleCursor?
```

## Parameters

- `presentationTimeStamp` — The initial presentation timestamp of the sample cursor.

## Return Value

An instance of [AVSampleCursor](../avsamplecursor.md).

## Discussion

If the track’s [asset](asset.md) property value for [providesPreciseDurationAndTiming](../avasset/providesprecisedurationandtiming.md) is [true](../../swift/true.md), the sample cursor is accurately positioned at the track’slast media sample with a presentation timestamp less than or equal to the desired timestamp, or, if there are no such samples, the first sample in presentation order.

If the track’s [asset](asset.md) property value for [providesPreciseDurationAndTiming](../avasset/providesprecisedurationandtiming.md) is [false](../../swift/false.md), and it’s prohibitively expensive to locate the precise sample at the desired timestamp, the sample cursor may be approximately positioned.

## See Also

### Creating sample cursors

- [- makeSampleCursorAtFirstSampleInDecodeOrder](<makesamplecursoratfirstsampleindecodeorder().md>) — Creates a sample cursor and positions it at the track’s first media sample in decode order.
- [- makeSampleCursorAtLastSampleInDecodeOrder](<makesamplecursoratlastsampleindecodeorder().md>) — Creates a sample cursor and positions it at the track’s last media sample in decode order.
