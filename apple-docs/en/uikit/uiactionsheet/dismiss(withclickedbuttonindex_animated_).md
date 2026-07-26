---
title: 'dismiss(withClickedButtonIndex:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/dismiss(withclickedbuttonindex:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/dismiss(withclickedbuttonindex:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/dismiss%28withclickedbuttonindex%3Aanimated%3A%29.json'
content_hash: 'sha256:f9e08e29b0141081'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# dismiss(withClickedButtonIndex:animated:)

<sub>Instance Method</sub>

Dismisses the action sheet immediately using an optional animation.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func dismiss(withClickedButtonIndex buttonIndex: Int, animated: Bool)
```

## Parameters

- `buttonIndex` — The index of the button that was clicked. Button indices start at `0`.

- `animated` — Specify [true](../../swift/true.md) to animate the dismissal of the action sheet or [false](../../swift/false.md) to remove the action sheet without an animation.

## Discussion

You can use this method to dismiss the action sheet programmatically as needed. The action sheet also calls this method itself in response to the user tapping one of the buttons in the action sheet.

In iOS 4.0, you may want to call this method whenever your application moves to the background. An action sheet is not dismissed automatically when an application moves to the background. This behavior differs from previous versions of the operating system, where they were canceled automatically when the application was terminated. Dismissing the action sheet gives your application a chance to save changes or abort the operation and perform any necessary cleanup in case your application is terminated later.
