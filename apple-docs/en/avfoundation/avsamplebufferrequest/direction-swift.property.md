---
title: direction
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/direction-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/direction-swift.property.json'
content_hash: 'sha256:d4bfe543c97e180f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRequest](../avsamplebufferrequest.md)

# direction

<sub>Instance Property</sub>

The buffer sample direction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var direction: AVSampleBufferRequest.Direction { get set }
```

## Discussion

The default value is [AVSampleBufferRequestDirectionNone](direction-swift.enum/none.md).

## See Also

### Configuring sample buffer request parameters

- [Direction](direction-swift.enum.md) — The modes that describe the buffer request direction.
- [limitCursor](limitcursor.md) — The limiting position for sample loading.
- [maxSampleCount](maxsamplecount.md) — The maximum number of samples to load.
- [mode](mode-swift.property.md) — The sample buffer request mode.
- [Mode](mode-swift.enum.md) — The modes in which a sample buffer generator processes a request.
- [overrideTime](overridetime.md) — The deadline for sample data and output PTS for the sample buffer.
- [preferredMinSampleCount](preferredminsamplecount.md) — The preferred minimum number of samples to load.
- [startCursor](startcursor.md) — The starting cursor position.
