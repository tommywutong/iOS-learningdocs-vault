---
title: UI_USER_INTERFACE_IDIOM()
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（13.0 起废弃）, iPadOS 2.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/ui_user_interface_idiom()
source_url: 'https://developer.apple.com/documentation/uikit/ui_user_interface_idiom()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/ui_user_interface_idiom%28%29.json'
content_hash: 'sha256:214b73381440415c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UI_USER_INTERFACE_IDIOM()

<sub>Function</sub>

Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).

> [!warning] Deprecated
> If your app runs in iOS 3.2 and later, use [userInterfaceIdiom](uidevice/userinterfaceidiom.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom
```

## Return Value

[UIUserInterfaceIdiomPhone](uiuserinterfaceidiom/phone.md) if the device is an iPhone or iPod touch or [UIUserInterfaceIdiomPad](uiuserinterfaceidiom/pad.md) if the device is an iPad.

## See Also

### Getting the current idiom

- [UIUserInterfaceIdiom](uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
