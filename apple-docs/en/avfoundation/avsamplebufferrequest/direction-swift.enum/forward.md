---
title: AVSampleBufferRequest.Direction.forward
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/forward
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/forward'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/forward.json'
content_hash: 'sha256:3c9243608d658fda'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferRequest](../../avsamplebufferrequest.md) · [Direction](../direction-swift.enum.md)

# AVSampleBufferRequest.Direction.forward

<sub>Case</sub>

The number of following samples may be zero or greater.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case forward
```

## Discussion

The number of following samples allowed is subject to the [limitCursor](../limitcursor.md), [preferredMinSampleCount](../preferredminsamplecount.md), and [maxSampleCount](../maxsamplecount.md) property values.

## See Also

### Buffer direction

- [AVSampleBufferRequestDirectionNone](none.md) — A single sample will be loaded.
- [AVSampleBufferRequestDirectionReverse](reverse.md) — The number of previous samples may be zero or greater.
