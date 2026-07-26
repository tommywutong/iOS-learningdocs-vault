---
title: maxFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avframeraterange/maxframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avframeraterange/maxframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avframeraterange/maxframeduration.json'
content_hash: 'sha256:21f956a763bdb1ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVFrameRateRange](../avframeraterange.md)

# maxFrameDuration

<sub>Instance Property</sub>

The maximum frame duration supported by the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxFrameDuration: CMTime { get }
```

## Discussion

This value is the reciprocal of [minFrameRate](minframerate.md), and expresses the minimum frame rate as a duration.

## See Also

### Accessing properties

- [maxFrameRate](maxframerate.md) — The maximum frame rate supported by the range.
- [minFrameDuration](minframeduration.md) — The minimum frame duration supported by the range.
- [minFrameRate](minframerate.md) — The minimum frame rate supported by the range.
