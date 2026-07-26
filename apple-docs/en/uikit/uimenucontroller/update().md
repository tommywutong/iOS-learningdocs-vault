---
title: update()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（16.0 起废弃）, iPadOS 3.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenucontroller/update()
source_url: 'https://developer.apple.com/documentation/uikit/uimenucontroller/update()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenucontroller/update%28%29.json'
content_hash: 'sha256:90f2056f5c26caa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuController](../uimenucontroller.md)

# update()

<sub>Instance Method</sub>

Updates the appearance and enabled state of menu commands.

> [!warning] Deprecated
> For more information, see [UIMenuController](../uimenucontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func update()
```

## Discussion

By default, `UIMenuController` calls this method just before the editing menu is made visible and when touches occur in the menu. As a result, a responder object in the application enables or disables menu commands depending on the context; for example, if the pasteboard holds no data of a compatible type, the Paste command would be disabled. You can call this method to force an update of the editing menu. You may also override this method to add any custom behavior.
