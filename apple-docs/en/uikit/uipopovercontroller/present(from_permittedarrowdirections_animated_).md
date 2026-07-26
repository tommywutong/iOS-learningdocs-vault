---
title: 'present(from:permittedArrowDirections:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/present(from:permittedarrowdirections:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/present(from:permittedarrowdirections:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/present%28from%3Apermittedarrowdirections%3Aanimated%3A%29.json'
content_hash: 'sha256:9ca96d6c2707c614'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# present(from:permittedArrowDirections:animated:)

<sub>Instance Method</sub>

Displays the popover and anchors it to the specified bar button item.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func present(from item: UIBarButtonItem, permittedArrowDirections arrowDirections: UIPopoverArrowDirection, animated: Bool)
```

## Parameters

- `item` — The bar button item on which to anchor the popover.

- `arrowDirections` — The arrow directions the popover is permitted to use. You can use this value to force the popover to be positioned on a specific side of the bar button item. However, it is generally better to specify [UIPopoverArrowDirectionAny](../uipopoverarrowdirection/any.md) and let the popover decide the best placement. You must not specify [UIPopoverArrowDirectionUnknown](../uipopoverarrowdirection/unknown.md) for this parameter.

- `animated` — Specify [true](../../swift/true.md) to animate the presentation of the popover or [false](../../swift/false.md) to display it immediately.

## Discussion

When presenting the popover, this method adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## See Also

### Presenting and dismissing the popover

- [- presentPopoverFromRect:inView:permittedArrowDirections:animated:](<present(from_in_permittedarrowdirections_animated_).md>) — Displays the popover and anchors it to the specified location in the view. _(deprecated)_
- [- dismissPopoverAnimated:](<dismiss(animated_).md>) — Dismisses the popover programmatically. _(deprecated)_
