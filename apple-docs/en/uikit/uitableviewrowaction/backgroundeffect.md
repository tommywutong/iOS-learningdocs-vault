---
title: backgroundEffect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（13.0 起废弃）, iPadOS 8.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitableviewrowaction/backgroundeffect
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewrowaction/backgroundeffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewrowaction/backgroundeffect.json'
content_hash: 'sha256:49be779d2d3aa16a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewRowAction](../uitableviewrowaction.md)

# backgroundEffect

<sub>Instance Property</sub>

The visual effect to apply to the button.

> [!warning] Deprecated
> For more information, see [UITableViewRowAction](../uitableviewrowaction.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@NSCopying var backgroundEffect: UIVisualEffect? { get set }
```

## Discussion

Assigning a visual effect object to this property adds that effect to the background of the action button.

## See Also

### Configuring the action’s appearance

- [style](style-swift.property.md) — The style applied to the action button. _(deprecated)_
- [Style](style-swift.enum.md) — Constants that specify the appearance of action buttons. _(deprecated)_
- [title](title.md) — The title of the action button. _(deprecated)_
- [backgroundColor](backgroundcolor.md) — The background color of the action button. _(deprecated)_
