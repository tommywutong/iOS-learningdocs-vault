---
title: titleMenuProvider
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/titlemenuprovider
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/titlemenuprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/titlemenuprovider.json'
content_hash: 'sha256:3007af0de1336d6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# titleMenuProvider

<sub>Instance Property</sub>

A closure that generates the navigation item’s title menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var titleMenuProvider: (([UIMenuElement]) -> UIMenu?)? { get set }
```

## Discussion

UIKit calls this closure to create a context menu that appears when a person taps the title of the navigation item. UIKit passes in a set of menu element suggestions that you can either use directly or modify in this closure to customize the menu.

```swift
// Use suggested menu elements directly.
navigationItem.titleMenuProvider = { suggestions in
    return UIMenu(children: suggestions)
}

// Add a custom menu element to the suggestions.
navigationItem.titleMenuProvider = { suggestions in
    var finalMenuElements = suggestions
    finalMenuElements.append(UICommand(title: "Save", 
                                       image: UIImage(systemName: "square.and.arrow.down"), 
                                      action: #selector(self.save)))
    return UIMenu(children: finalMenuElements)
}
```

Before displaying the title menu, UIKit validates each element in the menu you return by traversing the responder chain, starting with the navigation controller’s [topViewController](../uinavigationcontroller/topviewcontroller.md). For selector-based menu elements, implement your methods on [topViewController](../uinavigationcontroller/topviewcontroller.md) or farther up in the responder chain if you want those elements to appear in the title menu. For more information, see [- canPerformAction:withSender:](<../uiresponder/canperformaction(__withsender_).md>).

> [!tip] Tip
> You don’t need to assign a [titleMenuProvider](titlemenuprovider.md) if you only want to show Rename in your title menu. If you assign a `renameDelegate` without setting a [titleMenuProvider](titlemenuprovider.md), UIKit automatically generates a title menu containing the Rename menu element only.

## See Also

### Customizing the title menu

- [documentProperties](documentproperties.md) — An object that provides the document header for the title menu.
- [UIDocumentProperties](../uidocumentproperties.md) — Information that UIKit uses to generate a document header for a navigation item’s title menu.
