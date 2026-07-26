---
title: preferredImageDynamicRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/preferredimagedynamicrange
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/preferredimagedynamicrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/preferredimagedynamicrange.json'
content_hash: 'sha256:19daad132e269216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# preferredImageDynamicRange

<sub>Instance Property</sub>

The preferred treatment to use for HDR images. By default the image view will defer to the value from its traitCollection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredImageDynamicRange: UIImage.DynamicRange { get set }
```

## See Also

### Specifying the dynamic range

- [imageDynamicRange](imagedynamicrange.md) — The resolved treatment to use for HDR images.
- [DynamicRange](../uiimage/dynamicrange.md)
