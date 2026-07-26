---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/image
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/image.json'
content_hash: 'sha256:adf0da4d741bc90c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# image

<sub>Instance Property</sub>

The image to display alongside the menu element’s title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var image: UIImage? { get }
```

## Discussion

Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

## See Also

### Getting the element attributes

- [title](title.md) — The title of the menu element.
- [subtitle](subtitle.md) — The subtitle to display alongside the menu element’s title.
