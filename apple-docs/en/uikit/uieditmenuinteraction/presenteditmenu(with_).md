---
title: 'presentEditMenu(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteraction/presenteditmenu(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/presenteditmenu(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/presenteditmenu%28with%3A%29.json'
content_hash: 'sha256:d32c2db2ac3e6c95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# presentEditMenu(with:)

<sub>Instance Method</sub>

Presents an edit menu using the object you provide for configuration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentEditMenu(with configuration: UIEditMenuConfiguration)
```

## Parameters

- `configuration` — The object containing the configuration details for the menu.

## Discussion

You use this method to display the edit menu. The method calls [- editMenuInteraction:menuForConfiguration:suggestedActions:](<../uieditmenuinteractiondelegate/editmenuinteraction(__menufor_suggestedactions_).md>) on the interaction object’s delegate and updates the UI with the menu the delegate returns. This method dismisses any active menus before presenting the new menu.

The following example presents the menu from a gesture recognizer and provides the location of the gesture as the location for this interaction.

```swift
    @objc func didLongPress(_ recognizer: UIGestureRecognizer) {
        let location = recognizer.location(in: self.view)
        let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)

        if let interaction = editMenuInteraction {
            // Presenting the edit menu interaction
            interaction.presentEditMenu(with: configuration)
        }
    }
```

## See Also

### Managing edit menu interactions

- [delegate](delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- reloadVisibleMenu](<reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- updateVisibleMenuPositionAnimated:](<updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- dismissMenu](<dismissmenu().md>) — Dismiss the edit menu if present.
- [- locationInView:](<location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.
