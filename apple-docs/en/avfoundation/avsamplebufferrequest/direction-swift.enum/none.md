---
title: AVSampleBufferRequest.Direction.none
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/none
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/none.json'
content_hash: 'sha256:ef9d6c63dda524fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferRequest](../../avsamplebufferrequest.md) · [Direction](../direction-swift.enum.md)

# AVSampleBufferRequest.Direction.none

<sub>Case</sub>

A single sample will be loaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case none
```

## Discussion

When this constant is set, the [limitCursor](../limitcursor.md), [preferredMinSampleCount](../preferredminsamplecount.md), and [maxSampleCount](../maxsamplecount.md) properties are ignored.

## See Also

### Buffer direction

- [AVSampleBufferRequestDirectionForward](forward.md) — The number of following samples may be zero or greater.
- [AVSampleBufferRequestDirectionReverse](reverse.md) — The number of previous samples may be zero or greater.
