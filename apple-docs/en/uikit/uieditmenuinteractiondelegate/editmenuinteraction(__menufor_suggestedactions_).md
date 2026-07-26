---
title: 'editMenuInteraction(_:menuFor:suggestedActions:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction(_:menufor:suggestedactions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteractiondelegate/editmenuinteraction%28_%3Amenufor%3Asuggestedactions%3A%29.json'
content_hash: 'sha256:52e2fcc79b5f6756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteractionDelegate](../uieditmenuinteractiondelegate.md)

# editMenuInteraction(_:menuFor:suggestedActions:)

<sub>Instance Method</sub>

Provides the menu to use when the interaction begins or requires an update.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func editMenuInteraction(_ interaction: UIEditMenuInteraction, menuFor configuration: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu?
```

## Parameters

- `interaction` — The interaction object triggering the menu.

- `configuration` — The object containing the configuration details for the menu.

- `suggestedActions` — The array of suggested actions UIKit gathers from the [UIResponder](../uiresponder.md) chain. You should include these actions in the menu you return.

## Return Value

Returns a menu describing the desired menu hierarchy. To present the default system menu, return `nil`. To avoid presenting a menu, return an empty menu.

## Discussion

UIKit calls this method when the interaction begins or requires an update to the menu’s actions when calling [- reloadVisibleMenu](<../uieditmenuinteraction/reloadvisiblemenu().md>). The interaction displays the menu you provide. When not implemented, the default behavior is the same as returning a menu including the suggestedActions.

The following example returns a menu with an additional actions in a submenu.

```swift
func editMenuInteraction(_ interaction: UIEditMenuInteraction, menuFor configuration: UIEditMenuConfiguration, suggestedActions: [UIMenuElement]) -> UIMenu {
        let indentationMenu = UIMenu(title: "Indentation", image: UIImage(systemName: "list.bullet.indent"), children: [
            UIAction(title: "Increase", image: UIImage(systemName: "increase.indent")) { (action) in
                // Increase indentation action.
                print("increase indent")
            },
            UIAction(title: "Decrease", image: UIImage(systemName: "decrease.indent")) { (action) in
                // Decrease indentation action.
                print("decrease indent")
            }
        ])

        var actions = suggestedActions
        actions.append(indentationMenu)
        return UIMenu(children: actions)
    }
```

## See Also

### Customizing the Menu

- [- editMenuInteraction:targetRectForConfiguration:](<editmenuinteraction(__targetrectfor_).md>) — Provides the target rectangle to position the menu relative to when the interaction begins or requires an update.
- [- editMenuInteraction:willPresentMenuForConfiguration:animator:](<editmenuinteraction(__willpresentmenufor_animator_).md>) — Informs the delegate when the interaction is about to present the menu.
- [- editMenuInteraction:willDismissMenuForConfiguration:animator:](<editmenuinteraction(__willdismissmenufor_animator_).md>) — Informs the delegate when the interaction is about to dismiss the menu.
- [UIEditMenuInteractionAnimating](../uieditmenuinteractionanimating.md) — Methods adopted by system-supplied animator objects when interacting with menus.
