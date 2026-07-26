---
title: UIToolTipInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitooltipinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitooltipinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitooltipinteraction.json'
content_hash: 'sha256:79cf7b1b6cb9f133'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIToolTipInteraction

<sub>Class</sub>

An interaction object that makes it possible to show a tooltip when hovering a pointer over a view or control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIToolTipInteraction
```

## Overview

To show a tooltip when the pointer hovers over a view, add a [UIToolTipInteraction](uitooltipinteraction.md) object to the view. For example, the following code listings shows how to add a tooltip to a label:

```swift
let label = UILabel()
label.text = "Label with a tooltip"

let tooltipInteraction = UIToolTipInteraction(defaultToolTip: "The label's tooltip.")
label.addInteraction(tooltipInteraction)
```

If you want your app to determine the tooltip text at a later time — for instance, to reflect the current state of your app — set the interaction’s [delegate](uitooltipinteraction/delegate.md) property to an object that conforms to the [UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md) protocol.

To add a tooltip to a control derived from [UIControl](uicontrol.md), use the convenience property [toolTip](uicontrol/tooltip.md); for example, to add a tooltip to the button:

```swift
let button = UIButton(configuration: configuration, primaryAction: action)
button.toolTip = "Click to buy this item. You'll have a chance to change your mind before confirming your purchase."
```

Setting the [toolTip](uicontrol/tooltip.md) property creates a tooltip interaction for the control, which you can retrieve from the [toolTipInteraction](uicontrol/tooltipinteraction.md) property.

> [!note] Note
> Tooltips appear when your app runs in macOS or visionOS. To show a tooltip in macOS, your app must be an iPhone or iPad app running on a Mac with Apple silicon, or built with Mac Catalyst.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating a tooltip interaction

- [- init](<uitooltipinteraction/init().md>) — Creates a tooltip interaction object.
- [- initWithDefaultToolTip:](<uitooltipinteraction/init(defaulttooltip_).md>) — Creates a tooltip interaction object and sets the default tooltip text.

### Managing the interaction

- [enabled](uitooltipinteraction/isenabled.md) — A Boolean value that indicates whether the tooltip interaction is in the enabled state.
- [defaultToolTip](uitooltipinteraction/defaulttooltip.md) — The text that appears in a tooltip by default.

### Providing tooltip configurations

- [delegate](uitooltipinteraction/delegate.md) — An object that provides text that a tooltip displays instead of the default text.
- [UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md) — An interface that provides tooltip settings to an interaction.

## See Also

### Tooltips

- [Showing help tags for views and controls using tooltip interactions](showing-help-tags-for-views-and-controls-using-tooltip-interactions.md) — Explain the purpose of interface elements by showing a tooltip when a person positions the pointer over the element.
- [UIToolTipInteractionDelegate](uitooltipinteractiondelegate.md) — An interface that provides tooltip settings to an interaction.
