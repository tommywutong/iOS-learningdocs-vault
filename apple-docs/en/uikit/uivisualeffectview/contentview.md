---
title: contentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uivisualeffectview/contentview
source_url: 'https://developer.apple.com/documentation/uikit/uivisualeffectview/contentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uivisualeffectview/contentview.json'
content_hash: 'sha256:49e51310df78f397'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIVisualEffectView](../uivisualeffectview.md)

# contentView

<sub>Instance Property</sub>

A view object that can have a visual effect view added to it.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentView: UIView { get }
```

## Discussion

Add subviews to the [contentView](contentview.md) and not to [UIVisualEffectView](../uivisualeffectview.md) directly.

## See Also

### Retrieving view information

- [effect](effect.md) — The visual effect provided by the view.
