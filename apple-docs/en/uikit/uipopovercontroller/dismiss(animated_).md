---
title: 'dismiss(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/dismiss(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/dismiss(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/dismiss%28animated%3A%29.json'
content_hash: 'sha256:36bef44d374f6037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# dismiss(animated:)

<sub>Instance Method</sub>

Dismisses the popover programmatically.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func dismiss(animated: Bool)
```

## Parameters

- `animated` — Specify [true](../../swift/true.md) to animate the dismissal of the popover or [false](../../swift/false.md) to dismiss it immediately.

## Discussion

You can use this method to dismiss the popover programmatically in response to taps inside the popover window. Taps outside of the popover’s contents automatically dismiss the popover.

## See Also

### Presenting and dismissing the popover

- [- presentPopoverFromRect:inView:permittedArrowDirections:animated:](<present(from_in_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified location in the view. _(deprecated)_
- [- presentPopoverFromBarButtonItem:permittedArrowDirections:animated:](<present(from_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified bar button item. _(deprecated)_
