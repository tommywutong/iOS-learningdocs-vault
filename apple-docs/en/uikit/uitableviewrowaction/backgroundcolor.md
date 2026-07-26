---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewrowaction/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewrowaction/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewrowaction/backgroundcolor.json'
content_hash: 'sha256:08805a1a7bd23e5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewRowAction](../uitableviewrowaction.md)

# backgroundColor

<sub>Instance Property</sub>

The background color of the action button.

> [!warning] Deprecated
> For more information, see [UITableViewRowAction](../uitableviewrowaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@NSCopying var backgroundColor: UIColor? { get set }
```

## Discussion

Use this property to specify the background color for your button. If you don’t specify a value for this property, UIKit assigns a default color based on the value in the [style](style-swift.property.md) property.

## See Also

### Configuring the action’s appearance

- [style](style-swift.property.md) — The style applied to the action button. _(deprecated)_
- [Style](style-swift.enum.md) — Constants that specify the appearance of action buttons. _(deprecated)_
- [title](title.md) — The title of the action button. _(deprecated)_
- [backgroundEffect](backgroundeffect.md) — The visual effect to apply to the button. _(deprecated)_
