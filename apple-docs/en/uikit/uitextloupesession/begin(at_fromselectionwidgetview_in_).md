---
title: 'begin(at:fromSelectionWidgetView:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextloupesession/begin(at:fromselectionwidgetview:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextloupesession/begin(at:fromselectionwidgetview:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextloupesession/begin%28at%3Afromselectionwidgetview%3Ain%3A%29.json'
content_hash: 'sha256:00181e42ae77c5ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextLoupeSession](../uitextloupesession.md)

# begin(at:fromSelectionWidgetView:in:)

<sub>Type Method</sub>

Creates a new loupe session and displays the loupe at the specified location in your view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class func begin(at point: CGPoint, fromSelectionWidgetView selectionWidget: UIView?, in interactionView: UIView) -> Self?
```

## Parameters

- `point` — The point in your view’s coordinate system that you want to magnify using the loupe. When creating the loupe with a gesture recognizer, specify the location of the gesture.

- `selectionWidget` — The view associated with the insertion point. When using a [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md) object to display selections in your view, specify the view in the interaction object’s [cursorView](../uitextselectiondisplayinteraction/cursorview.md) property for this parameter.

- `interactionView` — The view in which to display the loupe. Specify all coordinate values relative to this view.

## Return Value

A new loupe session for the specified view. The method returns `nil` if showing the loupe is inappropriate in the current context.

## Discussion

Call this method to animate the appearance of the loupe at the specified `point` in `interactionView`.  Store a strong reference to this returned session and use it to update the position of the loupe. To hide the loupe again, call [- invalidate](<invalidate().md>) and then remove your reference to the session.
