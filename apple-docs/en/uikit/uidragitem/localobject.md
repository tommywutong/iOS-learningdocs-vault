---
title: localObject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragitem/localobject
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem/localobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem/localobject.json'
content_hash: 'sha256:666b6d68bcc33064'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragItem](../uidragitem.md)

# localObject

<sub>Instance Property</sub>

A custom object associated with the drag item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var localObject: Any? { get set }
```

## Discussion

The `localObject` property gives you the option to associate a custom object, such as a model object, with the drag item. The local object is available only to the app that initiates the drag activity.

## See Also

### Accessing the drag item’s data

- [itemProvider](itemprovider.md) — The item provider associated with the drag item.
