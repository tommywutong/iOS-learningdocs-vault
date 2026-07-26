---
title: AVSampleBufferRequest.Direction.reverse
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/reverse
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/reverse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/direction-swift.enum/reverse.json'
content_hash: 'sha256:2d26642a48cb7d37'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferRequest](../../avsamplebufferrequest.md) · [Direction](../direction-swift.enum.md)

# AVSampleBufferRequest.Direction.reverse

<sub>Case</sub>

The number of previous samples may be zero or greater.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case reverse
```

## Discussion

The number of previous samples allowed is subject to the [limitCursor](../limitcursor.md), [preferredMinSampleCount](../preferredminsamplecount.md), and [maxSampleCount](../maxsamplecount.md) property values.

## See Also

### Buffer direction

- [AVSampleBufferRequestDirectionForward](forward.md) — The number of following samples may be zero or greater.
- [AVSampleBufferRequestDirectionNone](none.md) — A single sample will be loaded.
