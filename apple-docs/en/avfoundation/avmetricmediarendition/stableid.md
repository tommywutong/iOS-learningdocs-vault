---
title: stableID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetricmediarendition/stableid
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetricmediarendition/stableid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetricmediarendition/stableid.json'
content_hash: 'sha256:40e2055e30e78e39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricMediaRendition](../avmetricmediarendition.md)

# stableID

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stableID: String? { get }
```

## Discussion

Provides ID corresponding to the rendition. This is equivalent to the STABLE-RENDITION-ID in the HLS playlist. If not available, value is nil.

## See Also

### Inspecting the rendition

- [URL](url.md)
