---
title: itemProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragitem/itemprovider
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem/itemprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem/itemprovider.json'
content_hash: 'sha256:20cad8d256f07c5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragItem](../uidragitem.md)

# itemProvider

<sub>Instance Property</sub>

The item provider associated with the drag item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var itemProvider: NSItemProvider { get }
```

## Discussion

The item provider conveys the data, or file, that the drag-and-drop activity shares between processes. The property is set when the [UIDragItem](../uidragitem.md) instance is created. For more information, see [- initWithItemProvider:](<init(itemprovider_).md>).

## See Also

### Accessing the drag item’s data

- [localObject](localobject.md) — A custom object associated with the drag item.
