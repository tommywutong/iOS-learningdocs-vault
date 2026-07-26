---
title: 'presentFindNavigator(showingReplace:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindinteraction/presentfindnavigator(showingreplace:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteraction/presentfindnavigator(showingreplace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteraction/presentfindnavigator%28showingreplace%3A%29.json'
content_hash: 'sha256:407000c39c2ecc77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteraction](../uifindinteraction.md)

# presentFindNavigator(showingReplace:)

<sub>Instance Method</sub>

Begins a search, displaying the find panel.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentFindNavigator(showingReplace: Bool)
```

## Parameters

- `showingReplace` — `YES` to display a replace text field in the panel if the delegate supports text replacement. `No` to avoid displaying the replace text field.

## Discussion

You use this method to begin a search and display the find panel. The method calls [- findInteraction:sessionForView:](<../uifindinteractiondelegate/findinteraction(__sessionfor_).md>) on the interaction object’s delegate and updates the UI using the session object the delegate returns.

The following example presents the find panel from a bar button item.

```swift
@objc func findButtonTapped(sender: UIBarButtonItem) {
    self.findInteraction!.presentFindNavigator(showingReplace: false)
}
```

The method has no effect if the find navigator panel is already present.

## See Also

### Managing find interactions

- [delegate](delegate.md) — An object that updates your app’s presentation and provides the session object for managing the interaction’s search.
- [- dismissFindNavigator](<dismissfindnavigator().md>) — Dismisses the find panel, if present.
- [- findNext](<findnext().md>) — Highlights the next found result in the content, relative to the currently highlighted result.
- [- findPrevious](<findprevious().md>) — Highlights the previously found result in the document, relative to the currently highlighted result.
