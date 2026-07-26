---
title: baselineOffsetFromBottom
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/baselineoffsetfrombottom-23gkf
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/baselineoffsetfrombottom-23gkf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/baselineoffsetfrombottom-23gkf.json'
content_hash: 'sha256:eec0f34df4e132ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# baselineOffsetFromBottom

<sub>Instance Property</sub>

The position of the baseline relative to the bottom of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CGFloat baselineOffsetFromBottom;
```

## Discussion

Positive values place the baseline up inside the image, and negative values place the baseline below the bottom of the image. When the value of this property is `0.0`, the baseline position is equal to the bottom of the image.

## See Also

### Managing the baseline

- [hasBaseline](hasbaseline.md) — A Boolean value that indicates whether the image has a defined baseline offset.
