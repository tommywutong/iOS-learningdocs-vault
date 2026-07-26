---
title: contentShape
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uishaperesolutioncontext/contentshape
source_url: 'https://developer.apple.com/documentation/uikit/uishaperesolutioncontext/contentshape'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uishaperesolutioncontext/contentshape.json'
content_hash: 'sha256:fbbe308c80ab86e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIShapeResolutionContext](../uishaperesolutioncontext.md)

# contentShape

<sub>Instance Property</sub>

The resolved shape of the content to which this shape can apply.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) UIResolvedShape * contentShape;
```

## Discussion

For example, if this shape applies an effect to a button, the [contentShape](contentshape.md) might represent the bounding shape of that button’s background. You typically size a dynamic shape relative to the bounding rectangle of the [contentShape](contentshape.md).
