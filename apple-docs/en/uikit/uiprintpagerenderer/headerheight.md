---
title: headerHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/headerheight
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/headerheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/headerheight.json'
content_hash: 'sha256:8fab64f642870f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# headerHeight

<sub>Instance Property</sub>

The height of the page header.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var headerHeight: CGFloat { get set }
```

## Discussion

The header is measured in points from the top of [printableRect](printablerect.md) and is above the content area. The default header height is 0.0.

## See Also

### Specifying header and footer heights

- [footerHeight](footerheight.md) — The height of the page footer.
