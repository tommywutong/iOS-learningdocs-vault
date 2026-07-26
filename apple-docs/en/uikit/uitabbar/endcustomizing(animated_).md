---
title: 'endCustomizing(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitabbar/endcustomizing(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/endcustomizing(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/endcustomizing%28animated%3A%29.json'
content_hash: 'sha256:d4730bfe90cbe773'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# endCustomizing(animated:)

<sub>Instance Method</sub>

Dismisses the standard interface used to customize the tab bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func endCustomizing(animated: Bool) -> Bool
```

## Parameters

- `animated` — If [true](../../swift/true.md), animate the dismissal of the interface.

## Return Value

[true](../../swift/true.md) if items on the tab bar changed or [false](../../swift/false.md) if they did not.

## Discussion

You rarely need to call this method. Typically, the user dismisses the modal view by tapping the built-in Done button in the interface. However, you might call this method to cancel the customization process because of changes to other parts of your interface.

## See Also

### Supporting user customization of tab bars

- [- beginCustomizingItems:](<begincustomizingitems(__).md>) — Presents a standard interface that lets the user customize the contents of the tab bar.
- [customizing](iscustomizing.md) — A Boolean value indicating whether the user is currently customizing the tab bar.
