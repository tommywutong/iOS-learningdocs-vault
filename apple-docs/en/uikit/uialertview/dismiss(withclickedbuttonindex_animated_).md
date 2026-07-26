---
title: 'dismiss(withClickedButtonIndex:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（9.0 起废弃）, iPadOS 2.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uialertview/dismiss(withclickedbuttonindex:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertview/dismiss(withclickedbuttonindex:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertview/dismiss%28withclickedbuttonindex%3Aanimated%3A%29.json'
content_hash: 'sha256:f961d269c7ea8616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertView](../uialertview.md)

# dismiss(withClickedButtonIndex:animated:)

<sub>Instance Method</sub>

Dismisses the receiver, optionally with animation.

> [!warning] Deprecated
> For more information, see [UIAlertView](../uialertview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func dismiss(withClickedButtonIndex buttonIndex: Int, animated: Bool)
```

## Parameters

- `buttonIndex` — The index of the button that was clicked just before invoking this method. The button indices start at `0`.

- `animated` — [true](../../swift/true.md) if the receiver should be removed by animating it first; otherwise, [false](../../swift/false.md) if it should be removed immediately with no animation.

## Discussion

In iOS 4.0, you may want to call this method whenever your application moves to the background. An alert view is not dismissed automatically when an application moves to the background. This behavior differs from previous versions of the operating system, where they were canceled automatically when the application was terminated. Dismissing the alert view gives your application a chance to save changes or abort the operation and perform any necessary cleanup in case your application is terminated later.
