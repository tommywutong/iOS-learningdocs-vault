---
title: 'collectionView(_:contextMenuConfigurationForItemsAt:point:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemsat:point:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:contextmenuconfigurationforitemsat:point:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acontextmenuconfigurationforitemsat%3Apoint%3A%29.json'
content_hash: 'sha256:9e028db5124a8e8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:contextMenuConfigurationForItemsAt:point:)

<sub>Instance Method</sub>

Asks the delegate for a context-menu configuration for the items at the specified index paths.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemsAt indexPaths: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration?
```

## Parameters

- `collectionView` — The collection view containing the items.

- `indexPaths` — An array of index paths corresponding to the items the menu acts on. An empty array indicates that a person is invoking the menu from a location that doesn’t map to an item index path, like the space between cells. An array with multiple index paths indicates that a person is invoking the menu on an item in a multiple selection.

- `point` — The location of the interaction in the collection view’s coordinate space.

## Return Value

A contextual menu configuration object describing the menu to present. Returning `nil` prevents the interaction from beginning. Returning an empty configuration causes the interaction to begin, and then end with a cancellation effect. You can use this cancellation effect to indicate to people that it’s possible to present a menu from this element, but that there aren’t any actions currently available.

## Discussion

The system calls this method when a person invokes a context menu from the collection view. Implement this method to build a [UIContextMenuConfiguration](../uicontextmenuconfiguration.md) according to the index paths the system passes in to this method. The following code example shows different context-menu configurations for zero, one, and multiple index paths.

```swift
func collectionView(_ collectionView: UICollectionView, contextMenuConfigurationForItemsAt indexPaths: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration? {
    return UIContextMenuConfiguration(actionProvider: { suggestedActions in
        if indexPaths.count == 0 {
            // Construct an empty-space menu.
            return UIMenu(children: [
                UIAction(title: "New Folder") { _ in /* Implement the action. */ }
            ])
        }
        else if indexPaths.count == 1 {
            // Construct a single-item menu.
            return UIMenu(children: [
                UIAction(title: "Copy") { _ in /* Implement the action. */ },
                UIAction(title: "Delete", attributes: .destructive) { _ in /* Implement the action. */ }
            ])
        }
        else {
            // Construct a multiple-item menu.
            return UIMenu(children: [
                UIAction(title: "New Folder With Selection") { _ in /* Implement the action. */ }
            ])
        }
    })
}
```

## See Also

### Managing context menus

- [Adding context menus in your app](../adding-context-menus-in-your-app.md) — Provide quick access to useful actions by adding context menus to your iOS app.
- [- collectionView:willDisplayContextMenuWithConfiguration:animator:](<collectionview(__willdisplaycontextmenu_animator_).md>) — Informs the delegate when a context menu will appear.
- [- collectionView:willEndContextMenuInteractionWithConfiguration:animator:](<collectionview(__willendcontextmenuinteraction_animator_).md>) — Informs the delegate when a context menu will disappear.
- [- collectionView:willPerformPreviewActionForMenuWithConfiguration:animator:](<collectionview(__willperformpreviewactionformenuwith_animator_).md>) — Informs the delegate when a user triggers a commit by tapping the preview.
- [- collectionView:contextMenuConfiguration:highlightPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_highlightpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [- collectionView:contextMenuConfiguration:dismissalPreviewForItemAtIndexPath:](<collectionview(__contextmenuconfiguration_dismissalpreviewforitemat_).md>) — Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.
