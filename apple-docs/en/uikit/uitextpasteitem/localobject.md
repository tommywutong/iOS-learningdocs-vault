---
title: localObject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextpasteitem/localobject
source_url: 'https://developer.apple.com/documentation/uikit/uitextpasteitem/localobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextpasteitem/localobject.json'
content_hash: 'sha256:b739f400346a423f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextPasteItem](../uitextpasteitem.md)

# localObject

<sub>Instance Property</sub>

The custom local object that the copy or drag source optionally attached to the drag item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var localObject: Any? { get }
```

## Discussion

The local object is available only to the app that initiates the copy or drag activity.

## See Also

### Accessing the text paste item’s data

- [itemProvider](itemprovider.md) — The item provider for the item being pasted or dropped.
