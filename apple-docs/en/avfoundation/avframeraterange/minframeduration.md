---
title: minFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avframeraterange/minframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avframeraterange/minframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avframeraterange/minframeduration.json'
content_hash: 'sha256:ca83f0e64d8e42fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFrameRateRange](../avframeraterange.md)

# minFrameDuration

<sub>Instance Property</sub>

The minimum frame duration supported by the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var minFrameDuration: CMTime { get }
```

## Discussion

This value is the reciprocal of [maxFrameRate](maxframerate.md), and expresses the maximum frame rate as a duration.

## See Also

### Accessing properties

- [maxFrameDuration](maxframeduration.md) — The maximum frame duration supported by the range.
- [maxFrameRate](maxframerate.md) — The maximum frame rate supported by the range.
- [minFrameRate](minframerate.md) — The minimum frame rate supported by the range.
