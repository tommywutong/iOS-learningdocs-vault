---
title: overrideTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrequest/overridetime
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/overridetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrequest/overridetime.json'
content_hash: 'sha256:76a4cc4b4fb7e6c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRequest](../avsamplebufferrequest.md)

# overrideTime

<sub>Instance Property</sub>

The deadline for sample data and output PTS for the sample buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var overrideTime: CMTime { get set }
```

## See Also

### Configuring sample buffer request parameters

- [direction](direction-swift.property.md) — The buffer sample direction.
- [Direction](direction-swift.enum.md) — The modes that describe the buffer request direction.
- [limitCursor](limitcursor.md) — The limiting position for sample loading.
- [maxSampleCount](maxsamplecount.md) — The maximum number of samples to load.
- [mode](mode-swift.property.md) — The sample buffer request mode.
- [Mode](mode-swift.enum.md) — The modes in which a sample buffer generator processes a request.
- [preferredMinSampleCount](preferredminsamplecount.md) — The preferred minimum number of samples to load.
- [startCursor](startcursor.md) — The starting cursor position.
