---
title: aspectRatio
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguideaspectfitting/aspectratio
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguideaspectfitting/aspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguideaspectfitting/aspectratio.json'
content_hash: 'sha256:2975d3db5187598b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuideAspectFitting](../uilayoutguideaspectfitting.md)

# aspectRatio

<sub>Instance Property</sub>

The content’s aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var aspectRatio: CGFloat { get set }
```

## Discussion

This property represents the ratio of the content’s width to its height. The value of this property must be greater than `0.0` and less than or equal to `100.0`. The default value is `1.0`.
