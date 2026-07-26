---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/delegate.json'
content_hash: 'sha256:474bed22217dfde4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# delegate

<sub>Instance Property</sub>

The delegate you want to receive popover controller messages.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak var delegate: (any UIPopoverControllerDelegate)? { get set }
```

## Discussion

The popover controller uses its delegate to determine whether it should dismiss the popover and provides a notification when such an event occurs. For more information about the methods you can implement in your delegate, see [UIPopoverControllerDelegate](../uipopovercontrollerdelegate.md).
