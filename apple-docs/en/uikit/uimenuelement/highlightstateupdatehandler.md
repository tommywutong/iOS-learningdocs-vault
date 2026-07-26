---
title: highlightStateUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uimenuelement/highlightstateupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uimenuelement/highlightstateupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuelement/highlightstateupdatehandler.json'
content_hash: 'sha256:070425462bee7c52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuElement](../uimenuelement.md)

# highlightStateUpdateHandler

<sub>Instance Property</sub>

A closure the system calls when the element’s highlight state changes in a menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var highlightStateUpdateHandler: ((UIMenuElement, Bool) -> Void)? { get set }
```

## Discussion

The system calls this handler whenever a menu element transitions between highlighted and unhighlighted states. Highlight events include pointer hover, touch down, keyboard navigation, and focus changes.

The handler receives two parameters: the affected element and a Boolean that indicates the new state. When `isHighlighted` is [true](../../swift/true.md), the element is highlighted. When it’s [false](../../swift/false.md), the element is unhighlighted.

Use this handler to update your app’s UI in response to the user’s attention on a menu element, such as showing a preview of the action’s effect while the user considers the option.

> [!note] Note
> In visionOS, the system doesn’t call this handler for gaze-based highlight.
