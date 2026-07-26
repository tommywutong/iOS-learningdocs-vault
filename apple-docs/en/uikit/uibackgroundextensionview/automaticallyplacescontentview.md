---
title: automaticallyPlacesContentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundextensionview/automaticallyplacescontentview
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundextensionview/automaticallyplacescontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundextensionview/automaticallyplacescontentview.json'
content_hash: 'sha256:76be191d516ce58e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundExtensionView](../uibackgroundextensionview.md)

# automaticallyPlacesContentView

<sub>Instance Property</sub>

Controls the automatic safe area placement of the `contentView` within the container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyPlacesContentView: Bool { get set }
```

## Discussion

When `NO`, the frame of the content view must be explicitly set or constraints added. The extension effect will be used to fill the container view around the content.

Defaults to `YES`.
