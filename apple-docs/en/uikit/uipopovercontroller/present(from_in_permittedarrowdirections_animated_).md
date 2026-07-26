---
title: 'present(from:in:permittedArrowDirections:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/present(from:in:permittedarrowdirections:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:in:permittedarrowdirections:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/present%28from%3Ain%3Apermittedarrowdirections%3Aanimated%3A%29.json'
content_hash: 'sha256:3ec1bb9dd5b1a524'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# present(from:in:permittedArrowDirections:animated:)

<sub>Instance Method</sub>

Displays the popover and anchors it to the specified location in the view.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func present(from rect: CGRect, in view: UIView, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

## Parameters

- `rect` — The rectangle in view at which to anchor the popover window.

- `view` — The view containing the anchor rectangle for the popover.

- `arrowDirections` — The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the rectangle. However, it is generally better to specify [UIPopoverArrowDirectionAny](../uipopoverarrowdirection/any.md) and let the popover decide the best placement. You must not specify [UIPopoverArrowDirectionUnknown](../uipopoverarrowdirection/unknown.md) for this parameter.

- `animated` — Specify [true](../../swift/true.md) to animate the presentation of the popover or [false](../../swift/false.md) to display it immediately.

## See Also

### Presenting and dismissing the popover

- [- presentPopoverFromBarButtonItem:permittedArrowDirections:animated:](<present(from_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified bar button item. _(deprecated)_
- [- dismissPopoverAnimated:](<dismiss(animated_).md>) — Dismisses the popover programmatically. _(deprecated)_
