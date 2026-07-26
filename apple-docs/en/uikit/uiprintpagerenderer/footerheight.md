---
title: footerHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintpagerenderer/footerheight
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/footerheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/footerheight.json'
content_hash: 'sha256:bdc53ae35b9c41b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# footerHeight

<sub>Instance Property</sub>

The height of the page footer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var footerHeight: CGFloat { get set }
```

## Discussion

The footer is measured in points from the bottom of [printableRect](printablerect.md) and is below the content area. The default footer height is 0.0

## See Also

### Specifying header and footer heights

- [headerHeight](headerheight.md) — The height of the page header.
