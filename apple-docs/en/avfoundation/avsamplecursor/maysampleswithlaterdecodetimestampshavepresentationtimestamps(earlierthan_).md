---
title: 'maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursor/maysampleswithlaterdecodetimestampshavepresentationtimestamps(earlierthan:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/maysampleswithlaterdecodetimestampshavepresentationtimestamps(earlierthan:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/maysampleswithlaterdecodetimestampshavepresentationtimestamps%28earlierthan%3A%29.json'
content_hash: 'sha256:cfd3ec8e175b9162'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan:)

<sub>Instance Method</sub>

Determines whether a sample later in decode order can have a presentation timestamp earlier than that of the specified sample cursor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maySamplesWithLaterDecodeTimeStampsHavePresentationTimeStamps(earlierThan cursor: AVSampleCursor) -> Bool
```

## Parameters

- `cursor` — An instance of `AVSampleCursor` with which to test the sample reordering boundary.

## Return Value

[true](../../swift/true.md) if it’s possible for any sample later in decode order than the sample at the position of the receiver can have a presentation timestamp earlier than that of the specified sample cursor; otherwise, [false](../../swift/false.md).

## Discussion

Undefined results occur if this cursor and the passed in cursor reference different sequences of samples, such as when they’re created by different instances of [AVAssetTrack](../avassettrack.md).

## See Also

### Accessing samples

- [- samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:](<maysampleswithearlierdecodetimestampshavepresentationtimestamps(laterthan_).md>) — Determines whether a sample earlier in decode order can have a presentation timestamp later than that of the specified sample cursor.
- [samplesRequiredForDecoderRefresh](samplesrequiredfordecoderrefresh.md) — The number of samples prior to the current sample, in decode order, the decoder requires to achieve a coherent output at the current decode time.
