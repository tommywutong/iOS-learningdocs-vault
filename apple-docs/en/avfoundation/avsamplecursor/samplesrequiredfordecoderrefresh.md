---
title: samplesRequiredForDecoderRefresh
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.11+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursor/samplesrequiredfordecoderrefresh
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/samplesrequiredfordecoderrefresh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/samplesrequiredfordecoderrefresh.json'
content_hash: 'sha256:fad0a033610c532b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# samplesRequiredForDecoderRefresh

<sub>Instance Property</sub>

The number of samples prior to the current sample, in decode order, the decoder requires to achieve a coherent output at the current decode time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var samplesRequiredForDecoderRefresh: Int { get }
```

## Discussion

This property value is 0 when the decoder doesn’t require samples for refresh or when the track doesn’t contain this information.

Some sample sequences don’t indicate sample dependencies and instead indicate to decode a specific sample with all available accuracy. The system must decode samples in decode order before decoding the specific sample.

## See Also

### Accessing samples

- [- samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:](<maysampleswithearlierdecodetimestampshavepresentationtimestamps(laterthan_).md>) — Determines whether a sample earlier in decode order can have a presentation timestamp later than that of the specified sample cursor.
- [- samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:](<maysampleswithlaterdecodetimestampshavepresentationtimestamps(earlierthan_).md>) — Determines whether a sample later in decode order can have a presentation timestamp earlier than that of the specified sample cursor.
