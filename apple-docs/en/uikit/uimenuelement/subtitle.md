---
title: subtitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenuelement/subtitle
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/subtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/subtitle.json'
content_hash: 'sha256:50b6711d29ac4089'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# subtitle

<sub>Instance Property</sub>

The subtitle to display alongside the menu element’s title.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var subtitle: String? { get set }
```

## Discussion

Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of a subtitle, and only when the app is running on iOS.

## See Also

### Getting the element attributes

- [title](title.md) — The title of the menu element.
- [image](image.md) — The image to display alongside the menu element’s title.
