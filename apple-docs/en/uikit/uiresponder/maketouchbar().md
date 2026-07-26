---
title: makeTouchBar()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/maketouchbar()
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/maketouchbar()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/maketouchbar%28%29.json'
content_hash: 'sha256:0d077591b5dbd560'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# makeTouchBar()

<sub>Instance Method</sub>

Asks the receiving responder to create and configure a Touch Bar object.

<sub>Mac Catalyst</sub>

```swift
func makeTouchBar() -> NSTouchBar?
```

## Return Value

A newly created Touch Bar object.

## Discussion

Override this method in a responder, such as [UIViewController](../uiviewcontroller.md), to create and configure a Touch Bar object for the responder.

```swift
#if targetEnvironment(macCatalyst)
extension RecipeDetailViewController: NSTouchBarDelegate {
    override func makeTouchBar() -> NSTouchBar? {
        let touchBar = NSTouchBar()
        touchBar.delegate = self
    
        touchBar.defaultItemIdentifiers = [
            .flexibleSpace,
            .deleteRecipe,
            .flexibleSpace,
            .editRecipe,
            .toggleRecipeIsFavorite,
            .flexibleSpace
        ]
    
        return touchBar
    }

    func touchBar(_ touchBar: NSTouchBar, makeItemForIdentifier identifier: NSTouchBarItem.Identifier) -> NSTouchBarItem? {
        let touchBarItem: NSTouchBarItem?
        // ...
        return touchBarItem
    }

#endif
```

## See Also

### Managing the Touch Bar

- [touchBar](touchbar.md) — The Touch Bar object for the responder.
