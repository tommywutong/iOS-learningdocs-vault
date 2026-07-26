---
title: contentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundextensionview/contentview
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundextensionview/contentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundextensionview/contentview.json'
content_hash: 'sha256:ef425224521f1bd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundExtensionView](../uibackgroundextensionview.md)

# contentView

<sub>Instance Property</sub>

The content view to extend to fill the `UIBackgroundExtensionView`.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentView: UIView? { get set }
```

## Discussion

The content view will be added as a subview of the extension view and placed within the safe area by default. See `automaticallyPlacesContentView` to customize the layout.
